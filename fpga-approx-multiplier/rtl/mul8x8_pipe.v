`timescale 1ns/1ps
// Registered wrapper used for the clocked waveform testbench and the FPGA top:
// inputs and outputs are registered, so the multiplier sits between two
// flip-flop stages (latency = 2 clock cycles).

module mul8x8_pipe #(
    parameter MODE = 0
) (
    input  wire        clk,
    input  wire        rst,
    input  wire [7:0]  a,
    input  wire [7:0]  b,
    output reg  [15:0] p
);
    reg  [7:0]  a_r, b_r;
    wire [15:0] p_w;

    mul8x8 #(.MODE(MODE)) u_mul (.a(a_r), .b(b_r), .p(p_w));

    always @(posedge clk) begin
        if (rst) begin
            a_r <= 8'd0;
            b_r <= 8'd0;
            p   <= 16'd0;
        end else begin
            a_r <= a;
            b_r <= b;
            p   <= p_w;
        end
    end
endmodule
