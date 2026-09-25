`timescale 1ns/1ps
// 4x4 unsigned multiplier built from four 2x2 blocks.
//
//   a = {aH, aL}, b = {bH, bL}   (2-bit halves)
//   p = (aH*bH << 4) + ((aH*bL + aL*bH) << 2) + aL*bL
//
// APPROX = 0 : all four 2x2 blocks are accurate  -> exact 4x4 product
// APPROX = 1 : all four 2x2 blocks are approximate (Kulkarni-style)

module mul4x4 #(
    parameter APPROX = 0
) (
    input  wire [3:0] a,
    input  wire [3:0] b,
    output wire [7:0] p
);
    wire [3:0] pp_ll, pp_lh, pp_hl, pp_hh;

    generate
        if (APPROX) begin : g_approx
            mul2x2_approx u_ll (.a(a[1:0]), .b(b[1:0]), .p(pp_ll));
            mul2x2_approx u_lh (.a(a[1:0]), .b(b[3:2]), .p(pp_lh));
            mul2x2_approx u_hl (.a(a[3:2]), .b(b[1:0]), .p(pp_hl));
            mul2x2_approx u_hh (.a(a[3:2]), .b(b[3:2]), .p(pp_hh));
        end else begin : g_exact
            mul2x2_exact  u_ll (.a(a[1:0]), .b(b[1:0]), .p(pp_ll));
            mul2x2_exact  u_lh (.a(a[1:0]), .b(b[3:2]), .p(pp_lh));
            mul2x2_exact  u_hl (.a(a[3:2]), .b(b[1:0]), .p(pp_hl));
            mul2x2_exact  u_hh (.a(a[3:2]), .b(b[3:2]), .p(pp_hh));
        end
    endgenerate

    assign p = ({4'b0, pp_hh} << 4) + ({4'b0, pp_lh} << 2) + ({4'b0, pp_hl} << 2) + {4'b0, pp_ll};
endmodule
