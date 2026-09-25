#!/usr/bin/env bash
# Synthesise every multiplier variant for the Xilinx 7-series fabric (Artix-7,
# the Basys-3 device family) with Yosys and save one report per design.
#
# Primary flow   (reports/<NAME>.stat)      : hierarchy-preserving synthesis. Each 2x2 /
#                  4x4 block is technology-mapped on its own, so the LUT count reflects
#                  the structural design; the netlist is flattened only for counting.
# Secondary flow (reports/<NAME>_flat.stat) : fully flattened with ABC9, where the tool
#                  re-optimises across block boundaries (sensitivity check).
#
#   -nodsp : map multipliers into LUTs + CARRY4 instead of a DSP48E1 slice.
#   ltp    : longest topological path through mapped cells (logic depth, delay proxy).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p synth/reports

RTL="rtl/mul2x2.v rtl/mul4x4.v rtl/mul8x8.v"

run() {  # name top mode
  local name=$1 top=$2 mode=$3
  local chp=""
  [ "$mode" != "-" ] && chp="chparam -set MODE $mode $top;"
  yosys -q -p "read_verilog $RTL; $chp synth_xilinx -family xc7 -nodsp -top $top; flatten; \
               tee -o synth/reports/$name.stat stat; tee -o synth/reports/$name.ltp ltp -noff" >/dev/null
  yosys -q -p "read_verilog $RTL; $chp synth_xilinx -family xc7 -nodsp -flatten -abc9 -top $top; \
               tee -o synth/reports/${name}_flat.stat stat" >/dev/null
  echo "synthesised $name"
}

run BEH       mul8x8_beh -
run EXACT     mul8x8     0
run AM_L      mul8x8     1
run AM_LM     mul8x8     2
run AM_ALL    mul8x8     3
run TRUNC_L   mul8x8     4
run HYB       mul8x8     5

# Behavioural multiplier with DSP inference allowed (what Vivado does by default)
yosys -q -p "read_verilog $RTL; synth_xilinx -family xc7 -top mul8x8_beh; \
             tee -o synth/reports/BEH_DSP.stat stat" >/dev/null
echo "synthesised BEH_DSP"

# FPGA demo top (checks that the Basys-3 design synthesises cleanly)
yosys -q -p "read_verilog $RTL fpga/basys3_top.v; synth_xilinx -family xc7 -nodsp -top basys3_top; \
             tee -o synth/reports/BASYS3_TOP.stat stat" >/dev/null
echo "synthesised BASYS3_TOP"
