# Significance-Driven Hybrid Approximate 8×8 Multiplier (Verilog, FPGA)

A complete B.Tech ECE final-year project: Verilog RTL, testbenches, simulation waveforms, FPGA synthesis, image-processing evaluation, an IEEE two-column conference paper and a full project report (thesis).

| Deliverable | File |
|---|---|
| IEEE conference paper (two-column, IEEEtran) | [`paper/paper.pdf`](paper/paper.pdf) · source [`paper/paper.tex`](paper/paper.tex) |
| B.Tech project report / thesis (53 pages) | [`thesis/thesis.pdf`](thesis/thesis.pdf) · source [`thesis/thesis.tex`](thesis/thesis.tex) |
| Verilog RTL | [`rtl/`](rtl) |
| Testbenches | [`tb/`](tb) |
| Basys-3 demo, pin constraints, Vivado script | [`fpga/`](fpga) |
| Results (CSV, figures, images) | [`results/`](results) |

## The idea in one paragraph

An 8×8 product splits into four 4×4 partial products with weights 2⁸, 2⁴, 2⁴ and 2⁰, and each 4×4 splits again into 2×2 blocks. Errors in the lowest-weight partial product hardly matter, so approximation is applied there first. Two techniques are used:
- the under-designed 2×2 block of Kulkarni et al., which returns 7 instead of 9 for 3×3 and so needs one fewer output bit;
- removing the lowest 4×4 partial product altogether (truncation).

The proposed **HYB** design removes `A_L·B_L` and approximates the two middle partial products.

| MODE | Design | Idea |
|---|---|---|
| 0 | EXACT | all blocks exact |
| 1 | AM-L | lowest 4×4 block approximate |
| 2 | AM-LM | lowest + middle blocks approximate |
| 3 | AM-ALL | all blocks approximate |
| 4 | TRUNC-L | lowest block removed |
| 5 | **HYB** | lowest removed + middle approximate |

## Key results (all reproducible with `./run_all.sh`)

| Design | LUTs (Artix-7) | LUT saving | NMED | WCE | PSNR (3 image kernels) |
|---|---|---|---|---|---|
| EXACT | 112 | — | 0 | 0 | exact |
| AM-L | 108 | 3.6% | 0.0048% | 50 | 60.9–64.8 dB (Gaussian identical) |
| AM-LM | 100 | 10.7% | 0.159% | 1650 | 49.4–56.2 dB |
| AM-ALL | 96 | 14.3% | 1.389% | 14450 | 34.2–35.3 dB |
| TRUNC-L | 88 | 21.4% | 0.087% | 225 | 51.5–55.7 dB |
| **HYB** | **80** | **28.6%** | 0.240% | 1825 | 46.7–50.1 dB |

- **Verification:** all 65,536 input pairs are simulated for every design. The exact designs have 0 mismatches, and no approximate design over-estimates.
- **LUT counts:** from Yosys `synth_xilinx -family xc7 -nodsp` with hierarchy preserved. A fully flattened ABC9 flow gives 62 LUTs for HYB versus 103 for EXACT (−39.8%).
- **Main finding:** TRUNC-L is both smaller and more accurate than AM-LM and AM-ALL. On LUT-based FPGAs it pays to remove the lowest partial product before approximating the higher ones.
- **Limitation:** TRUNC-L and HYB return 0 when both operands are below 16. They suit image data, not kernels dominated by small numbers.

## How to run

Requirements: `iverilog`, `yosys`, and Python 3 with `numpy`, `matplotlib` and `scikit-image` (on Ubuntu: `sudo apt install iverilog yosys`, then `pip install numpy matplotlib scikit-image`).

```bash
./run_all.sh          # simulation + waveforms + synthesis + metrics + figures
cd paper  && latexmk -pdf paper.tex     # needs texlive-publishers (IEEEtran)
cd thesis && latexmk -pdf thesis.tex
```

To see the waveform interactively, open `sim/wave.vcd` in GTKWave.

### On the Basys-3 board (Vivado)

```bash
vivado -mode batch -source fpga/vivado_build.tcl
```

The script writes a bitstream plus post-route utilisation, timing and power reports for every multiplier to `fpga/vivado_out/`. Controls on the board:
- **Switches:** SW15–8 set operand A and SW7–0 set operand B.
- **LEDs:** show the product.
- **BTNU / BTND:** change the multiplier mode.
- **7-segment display:** shows the mode and the error `exact − approx` in hex.

Check `fpga/basys3.xdc` against the Digilent master XDC for your board revision.

## Before you submit the paper

1. **Put in your details:** replace the placeholder names, college and e-mails in `paper.tex`, and every red placeholder in `thesis.tex`.
2. **Add Vivado numbers:** run the Vivado script and add the post-route LUT, Fmax and power figures to the paper and thesis. The current numbers come from open-source synthesis (Yosys), and reviewers will expect vendor figures.
3. **Check novelty:** search IEEE Xplore and Google Scholar for "hybrid approximate multiplier truncation FPGA" and cite anything close. Then state your contribution relative to it.
4. **Keep the AI disclosure:** IEEE requires AI-generated content to be disclosed in the acknowledgments. The paper includes such a sentence, so keep it or adapt it truthfully.
5. **Verify the venue:** check the conference or journal on the Scopus source list by ISSN or ISBN before submitting.
