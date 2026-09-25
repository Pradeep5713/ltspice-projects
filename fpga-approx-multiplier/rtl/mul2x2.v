`timescale 1ns/1ps
// 2x2 unsigned multiplier building blocks.
//
// mul2x2_exact  : accurate 2x2 multiplier, 4-bit product (3*3 = 9 = 4'b1001).
// mul2x2_approx : under-designed 2x2 multiplier of Kulkarni et al. (VLSI Design 2011).
//                 The only erroneous case is 3*3, which returns 7 (3'b111) instead of 9,
//                 so the product fits in 3 bits and the carry logic disappears.

module mul2x2_exact (
    input  wire [1:0] a,
    input  wire [1:0] b,
    output wire [3:0] p
);
    assign p[0] = a[0] & b[0];
    assign p[1] = (a[1] & b[0]) ^ (a[0] & b[1]);
    assign p[2] = (a[1] & b[1]) ^ (a[1] & b[0] & a[0] & b[1]);
    assign p[3] =  a[1] & b[1] & a[0] & b[0];
endmodule

module mul2x2_approx (
    input  wire [1:0] a,
    input  wire [1:0] b,
    output wire [3:0] p
);
    assign p[0] = a[0] & b[0];
    assign p[1] = (a[1] & b[0]) | (a[0] & b[1]);   // OR replaces XOR: 1+1 -> 1 (no carry)
    assign p[2] = a[1] & b[1];
    assign p[3] = 1'b0;                              // MSB never set
endmodule
