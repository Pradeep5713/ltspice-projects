"""Post-simulation analysis for the approximate 8x8 multiplier project.

Inputs (produced by the Verilog flow):
  sim/products.txt          exhaustive RTL simulation output (65,536 rows)
  sim/wave.vcd              clocked testbench waveform
  synth/reports/*.stat/ltp  Yosys synthesis reports

Outputs:
  results/error_metrics.csv, results/synthesis.csv, results/image_quality.csv,
  results/summary.json, results/fig_*.pdf / .png, results/img_*.png

All image-application results use the product tables produced by RTL simulation,
i.e. every multiplication in the image kernels is looked up from the Verilog output.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.metrics import peak_signal_noise_ratio, structural_similarity
from skimage.transform import resize

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results"
RES.mkdir(exist_ok=True)

DESIGNS = ["EXACT", "AM_L", "AM_LM", "AM_ALL", "TRUNC_L", "HYB"]
LABEL = {"BEH": "Behavioural a*b", "EXACT": "EXACT", "AM_L": "AM-L", "AM_LM": "AM-LM",
         "AM_ALL": "AM-ALL", "TRUNC_L": "TRUNC-L", "HYB": "HYB"}
COLS = {"EXACT": 3, "AM_L": 4, "AM_LM": 5, "AM_ALL": 6, "TRUNC_L": 7, "HYB": 8}
PMAX = 255 * 255

plt.rcParams.update({"font.family": "serif", "font.size": 8, "axes.titlesize": 8,
                     "axes.labelsize": 8, "legend.fontsize": 7, "figure.dpi": 150})


# ---------------------------------------------------------------- products
def load_products() -> dict[str, np.ndarray]:
    raw = np.loadtxt(ROOT / "sim/products.txt", dtype=np.int64)
    assert raw.shape == (65536, 9), raw.shape
    a, b = raw[:, 0], raw[:, 1]
    assert np.array_equal(raw[:, 2], a * b), "behavioural model mismatch"
    tables = {}
    for d, c in COLS.items():
        t = np.zeros((256, 256), dtype=np.int64)
        t[a, b] = raw[:, c]
        tables[d] = t
    tables["REF"] = np.outer(np.arange(256), np.arange(256)).astype(np.int64)
    return tables


def python_model(mode: int) -> np.ndarray:
    """Independent bit-accurate Python model of mul8x8 (cross-checks the RTL)."""
    def m2(a, b, apx):
        if apx and a == 3 and b == 3:
            return 7
        return a * b

    def m4(a, b, apx):
        al, ah, bl, bh = a & 3, a >> 2, b & 3, b >> 2
        return (m2(ah, bh, apx) << 4) + ((m2(ah, bl, apx) + m2(al, bh, apx)) << 2) + m2(al, bl, apx)

    ll = mode in (1, 2, 3)
    mid = mode in (2, 3, 5)
    hh = mode == 3
    t = np.zeros((256, 256), dtype=np.int64)
    for a in range(256):
        for b in range(256):
            al, ah, bl, bh = a & 15, a >> 4, b & 15, b >> 4
            pll = 0 if mode in (4, 5) else m4(al, bl, ll)
            t[a, b] = (m4(ah, bh, hh) << 8) + ((m4(ah, bl, mid) + m4(al, bh, mid)) << 4) + pll
    return t


def error_metrics(t: np.ndarray, ref: np.ndarray) -> dict:
    ed = (ref - t).astype(np.float64)            # approximations never over-estimate (checked in RTL)
    nz = ref > 0
    red = np.zeros_like(ed)
    red[nz] = np.abs(ed[nz]) / ref[nz]
    return {
        "ER_%": 100.0 * np.count_nonzero(ed) / ed.size,
        "MED": float(np.mean(np.abs(ed))),
        "NMED_%": 100.0 * float(np.mean(np.abs(ed))) / PMAX,
        "MRED_%": 100.0 * float(np.mean(red[nz])),
        "WCE": int(np.max(np.abs(ed))),
        "WCE_%": 100.0 * float(np.max(np.abs(ed))) / PMAX,
        "bias": float(np.mean(-ed)),
    }


# ---------------------------------------------------------------- synthesis
def parse_stat(path: Path) -> dict:
    txt = path.read_text()
    cells = {m.group(1): int(m.group(2)) for m in re.finditer(r"^\s+([A-Z][A-Z0-9_]+)\s+(\d+)\s*$", txt, re.M)}
    lut = sum(v for k, v in cells.items() if re.fullmatch(r"LUT[1-6]", k))
    return {"LUT": lut, "CARRY4": cells.get("CARRY4", 0), "MUXF7": cells.get("MUXF7", 0),
            "MUXF8": cells.get("MUXF8", 0), "DSP48E1": cells.get("DSP48E1", 0),
            "LUT6": cells.get("LUT6", 0)}


def parse_depth(path: Path) -> int:
    m = re.search(r"length=(\d+)", path.read_text())
    return int(m.group(1)) - 2 if m else -1          # minus input + output buffer


# ---------------------------------------------------------------- images
def approx_mul(t: np.ndarray, x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return t[x.astype(np.int64), y.astype(np.int64)]


def image_multiply(t, i1, i2):
    return (approx_mul(t, i1, i2) >> 8).astype(np.uint8)      # (A*B)/256


GAUSS = np.array([[20, 32, 20], [32, 48, 32], [20, 32, 20]], dtype=np.int64)  # sum = 256


def gaussian(t, img):
    p = np.pad(img.astype(np.int64), 1, mode="edge")
    h, w = img.shape
    acc = np.zeros((h, w), dtype=np.int64)
    for dy in range(3):
        for dx in range(3):
            acc += approx_mul(t, p[dy:dy + h, dx:dx + w], np.full((h, w), GAUSS[dy, dx]))
    return np.clip(acc >> 8, 0, 255).astype(np.uint8)


def blend(t, i1, i2, alpha=179):   # alpha/255 ~ 0.70
    return ((approx_mul(t, i1, np.full(i1.shape, alpha)) + approx_mul(t, i2, np.full(i2.shape, 255 - alpha))) >> 8).astype(np.uint8)


# ---------------------------------------------------------------- VCD
def parse_vcd(path: Path, names: list[str]):
    ids, series, t = {}, {n: [] for n in names}, 0
    scope = []
    for line in path.read_text().splitlines():
        s = line.split()
        if not s:
            continue
        if s[0] == "$scope":
            scope.append(s[2])
        elif s[0] == "$upscope":
            scope.pop()
        elif s[0] == "$var" and len(scope) == 1 and s[4] in names:
            ids[s[3]] = s[4]
        elif s[0].startswith("#"):
            t = int(s[0][1:])
        elif s[0][0] == "b" and len(s) == 2 and s[1] in ids:
            v = s[0][1:]
            series[ids[s[1]]].append((t, int(v, 2) if set(v) <= {"0", "1"} else None))
        elif s[0][0] in "01xz" and s[0][1:] in ids:
            series[ids[s[0][1:]]].append((t, int(s[0][0]) if s[0][0] in "01" else None))
    return series


def plot_waveform(path_out: Path):
    sigs = ["clk", "rst", "a", "b", "p_exact", "p_am_l", "p_am_lm", "p_am_all", "p_trunc_l", "p_hyb"]
    ser = parse_vcd(ROOT / "sim/wave.vcd", sigs)
    tend = max(tt for v in ser.values() for tt, _ in v) + 1
    fig, ax = plt.subplots(figsize=(7.16, 3.4))
    for row, name in enumerate(sigs):
        y0 = len(sigs) - 1 - row
        ch = ser[name] + [(tend, None)]
        if name in ("clk", "rst"):
            xs, ys = [], []
            for (t0, v0), (t1, _) in zip(ch[:-1], ch[1:]):
                xs += [t0, t1]
                ys += [y0 + 0.1 + 0.6 * (v0 or 0)] * 2
            ax.plot(xs, ys, color="#0b3d6b", lw=0.8)
        else:
            for (t0, v0), (t1, _) in zip(ch[:-1], ch[1:]):
                if t1 <= t0:
                    continue
                ax.fill([t0 + 150, t0, t0 + 150, t1 - 150, t1, t1 - 150],
                        [y0 + 0.1, y0 + 0.4, y0 + 0.7, y0 + 0.7, y0 + 0.4, y0 + 0.1],
                        facecolor="#e8eef5", edgecolor="#0b3d6b", lw=0.6)
                if v0 is not None and t1 - t0 >= 8000:
                    ax.text((t0 + t1) / 2, y0 + 0.4, str(v0), ha="center", va="center", fontsize=5.6)
    ax.set_yticks([len(sigs) - 1 - i + 0.4 for i in range(len(sigs))])
    ax.set_yticklabels([s.replace("_", "\\_") if False else s for s in sigs], fontsize=6.5)
    ax.set_xlim(0, tend)
    ax.set_ylim(-0.1, len(sigs))
    ax.set_xticks(range(0, tend + 1, 20000))
    ax.set_xticklabels([f"{x // 1000}" for x in range(0, tend + 1, 20000)])
    ax.set_xlabel("Time (ns)")
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    fig.savefig(path_out.with_suffix(".pdf"))
    fig.savefig(path_out.with_suffix(".png"), dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------- main
def main():
    tables = load_products()
    ref = tables["REF"]

    # Cross-check RTL against the independent Python model
    for mode, d in enumerate(DESIGNS):
        assert np.array_equal(python_model(mode), tables[d]), f"Python model mismatch for {d}"
    print("RTL products match the independent Python model for all 5 designs")

    # Error metrics
    em = {d: error_metrics(tables[d], ref) for d in DESIGNS}
    with open(RES / "error_metrics.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["design", "ER_%", "MED", "NMED_%", "MRED_%", "WCE", "WCE_%", "bias"])
        for d in DESIGNS:
            m = em[d]
            w.writerow([LABEL[d], f"{m['ER_%']:.2f}", f"{m['MED']:.2f}", f"{m['NMED_%']:.4f}",
                        f"{m['MRED_%']:.3f}", m["WCE"], f"{m['WCE_%']:.2f}", f"{m['bias']:.2f}"])

    # Synthesis
    syn = {}
    for d in ["BEH"] + DESIGNS:
        s = parse_stat(ROOT / f"synth/reports/{d}.stat")
        s["depth"] = parse_depth(ROOT / f"synth/reports/{d}.ltp")
        s["LUT_flat"] = parse_stat(ROOT / f"synth/reports/{d}_flat.stat")["LUT"]
        syn[d] = s
    syn["BEH_DSP"] = parse_stat(ROOT / "synth/reports/BEH_DSP.stat")
    syn["BASYS3_TOP"] = parse_stat(ROOT / "synth/reports/BASYS3_TOP.stat")
    base = syn["EXACT"]["LUT"]
    with open(RES / "synthesis.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["design", "LUT", "LUT6", "CARRY4", "MUXF7", "MUXF8", "logic_depth", "LUT_saving_vs_EXACT_%", "LUT_flat_abc9"])
        for d in ["BEH"] + DESIGNS:
            s = syn[d]
            w.writerow([LABEL[d], s["LUT"], s["LUT6"], s["CARRY4"], s["MUXF7"], s["MUXF8"], s["depth"],
                        f"{100 * (base - s['LUT']) / base:.1f}", s["LUT_flat"]])

    # Images
    cam = data.camera().astype(np.uint8)
    moon = data.moon().astype(np.uint8)
    coins = (resize(data.coins(), (512, 512), anti_aliasing=True, preserve_range=True)).astype(np.uint8)
    apps = {
        "Image multiplication": lambda t: image_multiply(t, cam, moon),
        "Gaussian smoothing": lambda t: gaussian(t, cam),
        "Image blending": lambda t: blend(t, cam, coins),
    }
    iq = {}
    outs = {}
    for app, fn in apps.items():
        exact = fn(ref)
        iq[app] = {}
        outs[app] = {"EXACT": exact}
        for d in DESIGNS[1:]:
            o = fn(tables[d])
            outs[app][d] = o
            iq[app][d] = {
                "PSNR": float(peak_signal_noise_ratio(exact, o, data_range=255)) if not np.array_equal(exact, o) else float("inf"),
                "SSIM": float(structural_similarity(exact, o, data_range=255)),
            }
    with open(RES / "image_quality.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["application"] + [f"{LABEL[d]} PSNR (dB)" for d in DESIGNS[1:]] + [f"{LABEL[d]} SSIM" for d in DESIGNS[1:]])
        for app in apps:
            w.writerow([app] + [f"{iq[app][d]['PSNR']:.2f}" for d in DESIGNS[1:]] + [f"{iq[app][d]['SSIM']:.4f}" for d in DESIGNS[1:]])

    # ---------------- figures
    # 1. Area vs accuracy trade-off
    fig, ax = plt.subplots(figsize=(3.4, 2.3))
    for d in DESIGNS:
        x, y = em[d]["NMED_%"], syn[d]["LUT"]
        ax.scatter(max(x, 1e-4), y, s=22, color="#0b3d6b" if d != "EXACT" else "#b22222", zorder=3)
        ax.annotate(LABEL[d], (max(x, 1e-4), y), textcoords="offset points", xytext=(4, 3), fontsize=6.5)
    ax.set_xscale("log")
    ax.set_xlabel("NMED (%)  [EXACT plotted at 1e-4]")
    ax.set_ylabel("LUTs (Artix-7, hierarchical)")
    ax.grid(True, which="both", lw=0.3, alpha=0.5)
    fig.tight_layout()
    fig.savefig(RES / "fig_tradeoff.pdf")
    fig.savefig(RES / "fig_tradeoff.png", dpi=200)
    plt.close(fig)

    # 2. Error-distance histograms
    fig, axs = plt.subplots(1, 5, figsize=(7.16, 1.7), sharey=True)
    for ax, d in zip(axs, DESIGNS[1:]):
        ed = (ref - tables[d]).ravel()
        nzed = ed[ed > 0]
        ax.hist(nzed, bins=40, color="#23527c")
        ax.set_title(f"{LABEL[d]} (ER {em[d]['ER_%']:.1f}%)")
        ax.set_xlabel("Error distance")
        ax.set_yscale("log")
    axs[0].set_ylabel("Count (log)")
    fig.tight_layout()
    fig.savefig(RES / "fig_error_hist.pdf")
    fig.savefig(RES / "fig_error_hist.png", dpi=200)
    plt.close(fig)

    # 3. Error heat maps (relative error over the operand space)
    fig, axs = plt.subplots(1, 5, figsize=(7.16, 1.75))
    for ax, d in zip(axs, DESIGNS[1:]):
        red = np.where(ref > 0, (ref - tables[d]) / np.maximum(ref, 1), 0) * 100
        im = ax.imshow(red, origin="lower", cmap="viridis", vmin=0, vmax=25)
        ax.set_title(LABEL[d])
        ax.set_xlabel("B")
        first = d == DESIGNS[1]
        ax.set_xticks([0, 255] if first else [])
        ax.set_yticks([0, 255] if first else [])
    axs[0].set_ylabel("A")
    fig.subplots_adjust(wspace=0.15)
    fig.colorbar(im, ax=axs, shrink=0.8, label="Rel. error (%)")
    fig.savefig(RES / "fig_error_map.pdf", bbox_inches="tight")
    fig.savefig(RES / "fig_error_map.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    # 4. Image outputs grid
    fig, axs = plt.subplots(3, 6, figsize=(7.16, 3.9))
    for r, app in enumerate(apps):
        for c, d in enumerate(DESIGNS):
            ax = axs[r, c]
            ax.imshow(outs[app][d], cmap="gray", vmin=0, vmax=255)
            ax.set_xticks([])
            ax.set_yticks([])
            if r == 0:
                ax.set_title(LABEL[d])
            if c == 0:
                ax.set_ylabel(app, fontsize=7)
            if d != "EXACT":
                q = iq[app][d]
                ax.set_xlabel(f"{q['PSNR']:.1f} dB / {q['SSIM']:.3f}", fontsize=6.5)
    fig.tight_layout()
    fig.savefig(RES / "fig_images.pdf")
    fig.savefig(RES / "fig_images.png", dpi=200)
    plt.close(fig)
    for app in apps:
        for d in DESIGNS:
            key = {"Image multiplication": "multiply", "Gaussian smoothing": "gaussian", "Image blending": "blend"}[app]
            plt.imsave(RES / f"img_{key}_{d}.png", outs[app][d], cmap="gray", vmin=0, vmax=255)

    # 5. Waveform
    plot_waveform(RES / "fig_waveform")

    summary = {"error_metrics": em, "synthesis": syn, "image_quality": iq}
    (RES / "summary.json").write_text(json.dumps(summary, indent=2, default=float))
    print(json.dumps(summary, indent=1, default=float)[:4000])


if __name__ == "__main__":
    main()
