// Clocked testbench that produces sim/wave.vcd for the waveform figure.
// The exact (MODE 0) and five approximate pipelines receive the same
// operand stream; the product appears two clock cycles after the operands.

`timescale 1ns/1ps

module tb_wave;
    reg         clk = 1'b0;
    reg         rst = 1'b1;
    reg  [7:0]  a = 8'd0, b = 8'd0;
    wire [15:0] p_exact, p_am_l, p_am_lm, p_am_all, p_trunc_l, p_hyb;

    always #5 clk = ~clk;   // 100 MHz clock (Basys-3 oscillator frequency)

    mul8x8_pipe #(.MODE(0)) u0 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_exact));
    mul8x8_pipe #(.MODE(1)) u1 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_am_l));
    mul8x8_pipe #(.MODE(2)) u2 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_am_lm));
    mul8x8_pipe #(.MODE(3)) u3 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_am_all));
    mul8x8_pipe #(.MODE(4)) u4 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_trunc_l));
    mul8x8_pipe #(.MODE(5)) u5 (.clk(clk), .rst(rst), .a(a), .b(b), .p(p_hyb));

    // Operand stream: small values, the 3x3 corner case, and large values.
    reg [7:0] va [0:9];
    reg [7:0] vb [0:9];
    integer k;

    initial begin
        va[0] = 8'd12;  vb[0] = 8'd10;
        va[1] = 8'd3;   vb[1] = 8'd3;
        va[2] = 8'd15;  vb[2] = 8'd15;
        va[3] = 8'd100; vb[3] = 8'd25;
        va[4] = 8'd127; vb[4] = 8'd2;
        va[5] = 8'd170; vb[5] = 8'd85;
        va[6] = 8'd200; vb[6] = 8'd150;
        va[7] = 8'd255; vb[7] = 8'd255;
        va[8] = 8'd64;  vb[8] = 8'd64;
        va[9] = 8'd51;  vb[9] = 8'd77;

        $dumpfile("sim/wave.vcd");
        $dumpvars(0, tb_wave);

        repeat (2) @(posedge clk);
        rst <= 1'b0;
        for (k = 0; k < 10; k = k + 1) begin
            @(posedge clk);
            a <= va[k];
            b <= vb[k];
        end
        repeat (4) @(posedge clk);
        $finish;
    end

    // Console log of each result (printed when it leaves the pipeline).
    always @(posedge clk)
        if (!rst)
            $display("t=%0d ns  exact=%0d  AM-L=%0d  AM-LM=%0d  AM-ALL=%0d  TRUNC-L=%0d  HYB=%0d",
                     $time, p_exact, p_am_l, p_am_lm, p_am_all, p_trunc_l, p_hyb);
endmodule
