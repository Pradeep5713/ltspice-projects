# Vivado batch flow for the Basys-3 demo and per-design reports.
#
#   vivado -mode batch -source fpga/vivado_build.tcl
#
# Produces, in fpga/vivado_out/:
#   basys3_top.bit                     bitstream for the Basys-3 board
#   util_basys3_top.rpt, timing_*.rpt, power_*.rpt
#   util_mul8x8_MODE<n>.rpt            out-of-context utilisation for each multiplier
#   timing_mul8x8_MODE<n>.rpt          (registered wrapper, 100 MHz constraint)
# Add these Vivado numbers to the paper/thesis tables next to the Yosys results.

set part  xc7a35tcpg236-1
set here  [file dirname [file normalize [info script]]]
set root  [file dirname $here]
set out   $here/vivado_out
file mkdir $out

set rtl [list $root/rtl/mul2x2.v $root/rtl/mul4x4.v $root/rtl/mul8x8.v $root/rtl/mul8x8_pipe.v]

# ---------------- per-design out-of-context runs (registered wrapper) ----------------
foreach mode {0 1 2 3 4 5} {
    read_verilog $rtl
    synth_design -top mul8x8_pipe -part $part -mode out_of_context -generic MODE=$mode -flatten_hierarchy rebuilt
    create_clock -name clk -period 10.0 [get_ports clk]
    opt_design
    place_design
    route_design
    report_utilization     -file $out/util_mul8x8_MODE$mode.rpt
    report_timing_summary  -file $out/timing_mul8x8_MODE$mode.rpt
    report_power           -file $out/power_mul8x8_MODE$mode.rpt
    close_design
}

# ---------------- full Basys-3 demo ----------------
read_verilog [concat $rtl [list $here/basys3_top.v]]
read_xdc $here/basys3.xdc
synth_design -top basys3_top -part $part
opt_design
place_design
route_design
report_utilization    -file $out/util_basys3_top.rpt
report_timing_summary -file $out/timing_basys3_top.rpt
report_power          -file $out/power_basys3_top.rpt
write_bitstream -force $out/basys3_top.bit
