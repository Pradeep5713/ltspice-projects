`timescale 1ns/1ps
// 8x8 unsigned multipliers.
//
// mul8x8_beh : behavioural reference, p = a * b (lets the synthesis tool choose).
// mul8x8     : recursive 8x8 multiplier built from four 4x4 blocks,
//
//   a = {aH, aL}, b = {bH, bL}   (4-bit halves)
//   p = (aH*bH << 8) + ((aH*bL + aL*bH) << 4) + aL*bL
//
// The MODE parameter chooses where approximation is applied. Approximation is
// placed in the least-significant partial products first, because an error there
// is multiplied by a smaller weight (significance-driven placement).
//
//   MODE 0  EXACT   : all 4x4 blocks exact                        (accurate)
//   MODE 1  AM-L    : aL*bL approximate                            (lowest weight 2^0)
//   MODE 2  AM-LM   : aL*bL, aH*bL, aL*bH approximate; aH*bH exact
//   MODE 3  AM-ALL  : all four blocks approximate (fully under-designed multiplier)
//   MODE 4  TRUNC-L : aL*bL block removed (forced to zero)
//   MODE 5  HYB     : aL*bL removed + aH*bL, aL*bH approximate; aH*bH exact (hybrid)

module mul8x8_beh (
    input  wire [7:0]  a,
    input  wire [7:0]  b,
    output wire [15:0] p
);
    assign p = a * b;
endmodule

module mul8x8 #(
    parameter MODE = 0
) (
    input  wire [7:0]  a,
    input  wire [7:0]  b,
    output wire [15:0] p
);
    localparam LL_APX = (MODE == 1) || (MODE == 2) || (MODE == 3);
    localparam MID_APX = (MODE == 2) || (MODE == 3) || (MODE == 5);
    localparam HH_APX = (MODE == 3);

    wire [7:0] pp_ll, pp_lh, pp_hl, pp_hh;

    generate
        if (MODE == 4 || MODE == 5) begin : g_trunc
            assign pp_ll = 8'd0;
        end else begin : g_ll
            mul4x4 #(.APPROX(LL_APX)) u_ll (.a(a[3:0]), .b(b[3:0]), .p(pp_ll));
        end
    endgenerate

    mul4x4 #(.APPROX(MID_APX)) u_lh (.a(a[3:0]), .b(b[7:4]), .p(pp_lh));
    mul4x4 #(.APPROX(MID_APX)) u_hl (.a(a[7:4]), .b(b[3:0]), .p(pp_hl));
    mul4x4 #(.APPROX(HH_APX))  u_hh (.a(a[7:4]), .b(b[7:4]), .p(pp_hh));

    assign p = ({8'b0, pp_hh} << 8) + ({8'b0, pp_lh} << 4) + ({8'b0, pp_hl} << 4) + {8'b0, pp_ll};
endmodule
