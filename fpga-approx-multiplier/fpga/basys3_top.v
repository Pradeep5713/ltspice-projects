`timescale 1ns/1ps
// Basys-3 demonstration top level.
//
//   sw[15:8]  operand A          sw[7:0]  operand B
//   led[15:0] 16-bit product of the selected multiplier
//   btnU/btnD select the multiplier mode (0 EXACT, 1 AM-L, 2 AM-LM, 3 AM-ALL, 4 TRUNC-L, 5 HYB)
//   7-segment display: digit 3 shows the mode number,
//                      digits 2..0 show |exact - approx| in hex (error magnitude, low 12 bits)
//   btnC      synchronous reset

module basys3_top (
    input  wire        clk,        // 100 MHz
    input  wire [15:0] sw,
    input  wire        btnC,
    input  wire        btnU,
    input  wire        btnD,
    output wire [15:0] led,
    output reg  [6:0]  seg,        // active-low segments {g,f,e,d,c,b,a}
    output wire        dp,
    output reg  [3:0]  an          // active-low digit enables
);
    wire rst = btnC;

    // ---------------- operand registers ----------------
    reg [7:0] a_r, b_r;
    always @(posedge clk) begin
        a_r <= sw[15:8];
        b_r <= sw[7:0];
    end

    // ---------------- all six multipliers ----------------
    wire [15:0] p [0:5];
    mul8x8 #(.MODE(0)) m0 (.a(a_r), .b(b_r), .p(p[0]));
    mul8x8 #(.MODE(1)) m1 (.a(a_r), .b(b_r), .p(p[1]));
    mul8x8 #(.MODE(2)) m2 (.a(a_r), .b(b_r), .p(p[2]));
    mul8x8 #(.MODE(3)) m3 (.a(a_r), .b(b_r), .p(p[3]));
    mul8x8 #(.MODE(4)) m4 (.a(a_r), .b(b_r), .p(p[4]));
    mul8x8 #(.MODE(5)) m5 (.a(a_r), .b(b_r), .p(p[5]));

    // ---------------- button debounce + mode select ----------------
    reg [19:0] div = 20'd0;                    // ~10 ms tick at 100 MHz
    always @(posedge clk) div <= div + 1'b1;
    wire tick = (div == 20'd0);

    reg [1:0] u_sync, d_sync;
    reg       u_prev, d_prev;
    reg [2:0] mode;
    always @(posedge clk) begin
        u_sync <= {u_sync[0], btnU};
        d_sync <= {d_sync[0], btnD};
        if (rst) begin
            mode   <= 3'd0;
            u_prev <= 1'b0;
            d_prev <= 1'b0;
        end else if (tick) begin
            u_prev <= u_sync[1];
            d_prev <= d_sync[1];
            if (u_sync[1] && !u_prev) mode <= (mode == 3'd5) ? 3'd0 : mode + 1'b1;
            if (d_sync[1] && !d_prev) mode <= (mode == 3'd0) ? 3'd5 : mode - 1'b1;
        end
    end

    // ---------------- outputs ----------------
    reg [15:0] prod_r, err_r;
    always @(posedge clk) begin
        prod_r <= p[mode];
        err_r  <= p[0] - p[mode];               // approximate products never exceed exact
    end
    assign led = prod_r;
    assign dp  = 1'b1;

    // ---------------- 7-segment multiplexing ----------------
    reg [1:0] digit;
    always @(posedge clk) if (div[16:0] == 17'd0) digit <= digit + 1'b1;

    reg [3:0] nib;
    always @(*) begin
        case (digit)
            2'd3: begin an = 4'b0111; nib = {1'b0, mode};   end
            2'd2: begin an = 4'b1011; nib = err_r[11:8];     end
            2'd1: begin an = 4'b1101; nib = err_r[7:4];      end
            default: begin an = 4'b1110; nib = err_r[3:0];   end
        endcase
        case (nib)
            4'h0: seg = 7'b1000000; 4'h1: seg = 7'b1111001; 4'h2: seg = 7'b0100100; 4'h3: seg = 7'b0110000;
            4'h4: seg = 7'b0011001; 4'h5: seg = 7'b0010010; 4'h6: seg = 7'b0000010; 4'h7: seg = 7'b1111000;
            4'h8: seg = 7'b0000000; 4'h9: seg = 7'b0010000; 4'hA: seg = 7'b0001000; 4'hB: seg = 7'b0000011;
            4'hC: seg = 7'b1000110; 4'hD: seg = 7'b0100001; 4'hE: seg = 7'b0000110; default: seg = 7'b0001110;
        endcase
    end
endmodule
