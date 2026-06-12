"""
RC High-Pass Filter: LTspice batch simulation + Bode plot + verification.
Uses PyLTSpice 5.x API.
"""

import subprocess
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── paths ────────────────────────────────────────────────────────────────────
LTSPICE_EXE = r"C:\Users\Pradeep\AppData\Local\Programs\ADI\LTspice\LTspice.exe"
SCRIPT_DIR  = Path(__file__).parent.resolve()
NET_FILE    = SCRIPT_DIR / "rc_highpass.net"
RAW_FILE    = SCRIPT_DIR / "rc_highpass.raw"
RESULTS_DIR = SCRIPT_DIR / "results"
BODE_PNG    = RESULTS_DIR / "bode.png"

RESULTS_DIR.mkdir(exist_ok=True)

# ── theory ────────────────────────────────────────────────────────────────────
R = 1e3
C = 159e-9
f_theory = 1.0 / (2 * np.pi * R * C)
print(f"Theoretical cutoff: {f_theory:.1f} Hz")

# ── run LTspice batch ─────────────────────────────────────────────────────────
if RAW_FILE.exists():
    RAW_FILE.unlink()

cmd = [LTSPICE_EXE, "-b", str(NET_FILE)]
print(f"Running: {' '.join(cmd)}")
result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
print("Return code:", result.returncode)
if result.stdout:
    print("STDOUT:", result.stdout[:500])
if result.stderr:
    print("STDERR:", result.stderr[:500])

if not RAW_FILE.exists():
    print(f"ERROR: {RAW_FILE} not created.")
    sys.exit(1)

print(f"RAW file size: {RAW_FILE.stat().st_size} bytes")

# ── parse with PyLTSpice ──────────────────────────────────────────────────────
from PyLTSpice import RawRead

raw = RawRead(str(RAW_FILE))
print("Trace names:", raw.get_trace_names())

freq   = raw.get_wave("frequency").real
vout   = raw.get_wave("V(vout)")
mag_db = 20 * np.log10(np.abs(vout))

# ── find -3 dB point ──────────────────────────────────────────────────────────
# High-pass: reference is the high-frequency passband (last point)
ref_db    = mag_db[-1]
target_db = ref_db - 3.0
idx = np.argmin(np.abs(mag_db - target_db))
f_sim = freq[idx]
print(f"Simulated -3 dB cutoff: {f_sim:.1f} Hz  (ref={ref_db:.2f} dB)")

# ── Bode plot ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogx(freq, mag_db, "b-", linewidth=2, label="Simulated")
ax.axhline(target_db,   color="r",      linestyle="--", alpha=0.8, label="-3 dB line")
ax.axvline(f_sim,       color="g",      linestyle=":",  label=f"f_c sim   = {f_sim:.0f} Hz")
ax.axvline(f_theory,    color="orange", linestyle=":",  alpha=0.7,
           label=f"f_c theory = {f_theory:.0f} Hz")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude (dB)")
ax.set_title("RC High-Pass Filter — Bode Magnitude")
ax.legend()
ax.grid(True, which="both", alpha=0.4)
fig.tight_layout()
fig.savefig(str(BODE_PNG), dpi=150)
print(f"Plot saved: {BODE_PNG}")

# ── verify ────────────────────────────────────────────────────────────────────
error_pct     = abs(f_sim - f_theory) / f_theory * 100
tolerance_pct = 10
passed        = error_pct <= tolerance_pct

print()
print("=" * 58)
print("  VERIFICATION RESULT")
print("=" * 58)
print(f"  Theoretical f_c  : {f_theory:>10.1f} Hz")
print(f"  Simulated   f_c  : {f_sim:>10.1f} Hz")
print(f"  Error            : {error_pct:>10.2f} %")
print(f"  Tolerance        : {tolerance_pct:>10d} %")
print(f"  Result           : {'PASS' if passed else 'FAIL'}")
print("=" * 58)

# ── README ────────────────────────────────────────────────────────────────────
readme = f"""# RC High-Pass Filter

## Circuit

| Component | Value |
|-----------|-------|
| R1 | 1 kΩ |
| C1 | 159 nF |
| V1 | AC 1 V |

Topology: C1 in series (Vin → Vout), R1 from Vout to GND.

## Calculated vs Simulated

| Parameter | Calculated | Simulated | Error |
|-----------|-----------|-----------|-------|
| Cutoff frequency (f_c) | {f_theory:.1f} Hz | {f_sim:.1f} Hz | {error_pct:.2f}% |
| Magnitude at f_c | −3.0 dB | {mag_db[idx] - ref_db:.2f} dB | — |

## Verification

**Result: {"PASS" if passed else "FAIL"}** — simulated cutoff is within {tolerance_pct}% of theoretical value.

## Bode Plot

![Bode Magnitude](results/bode.png)

## Theory

$$f_c = \\frac{{1}}{{2\\pi R C}} = \\frac{{1}}{{2\\pi \\times 1\\,\\text{{k}}\\Omega \\times 159\\,\\text{{nF}}}} \\approx {f_theory:.0f}\\,\\text{{Hz}}$$

At frequencies above f_c the filter passes the signal (0 dB); below f_c it attenuates at −20 dB/decade.
"""

readme_path = SCRIPT_DIR / "README.md"
readme_path.write_text(readme, encoding="utf-8")
print(f"README written: {readme_path}")

sys.exit(0 if passed else 1)
