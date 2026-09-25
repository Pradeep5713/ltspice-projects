#!/usr/bin/env bash
# Reproduce every result in the paper and thesis:
#   1. exhaustive RTL simulation (65,536 vectors x 7 designs, self-checking)
#   2. clocked waveform simulation (sim/wave.vcd)
#   3. Yosys synthesis for Xilinx 7-series (Artix-7 / Basys-3 family)
#   4. error metrics, image-quality metrics and all figures (results/)
# Requirements: iverilog, yosys, python3 with numpy, matplotlib, scikit-image.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
mkdir -p sim results
RTL="rtl/mul2x2.v rtl/mul4x4.v rtl/mul8x8.v"

echo "== 1. exhaustive simulation"
iverilog -g2005 -o sim/tb_exhaustive.vvp tb/tb_exhaustive.v $RTL
vvp -n sim/tb_exhaustive.vvp | tee sim/tb_exhaustive.log
grep -q "RESULT: PASS" sim/tb_exhaustive.log

echo "== 2. waveform simulation"
iverilog -g2005 -o sim/tb_wave.vvp tb/tb_wave.v $RTL rtl/mul8x8_pipe.v
vvp -n sim/tb_wave.vvp | tee sim/tb_wave.log

echo "== 3. synthesis"
./synth/synth.sh

echo "== 4. analysis and figures"
$PY analysis/analyze.py > results/analysis.log
cat results/error_metrics.csv results/synthesis.csv results/image_quality.csv
