// Exhaustive self-checking testbench.
//
// Applies all 256 x 256 = 65,536 input pairs to every design variant and
//   1. checks that the behavioural and recursive exact multipliers equal a*b,
//   2. checks that every approximate variant never over-estimates (p_apx <= a*b),
//   3. writes every product to sim/products.txt for error / image analysis:
//        a b p_beh p_exact p_am_l p_am_lm p_am_all p_trunc_l p_hyb

`timescale 1ns/1ps

module tb_exhaustive;
    reg  [7:0]  a, b;
    wire [15:0] p_beh, p_ex, p_l, p_lm, p_all, p_tr, p_hy;

    mul8x8_beh          u_beh (.a(a), .b(b), .p(p_beh));
    mul8x8 #(.MODE(0))  u_ex  (.a(a), .b(b), .p(p_ex));
    mul8x8 #(.MODE(1))  u_l   (.a(a), .b(b), .p(p_l));
    mul8x8 #(.MODE(2))  u_lm  (.a(a), .b(b), .p(p_lm));
    mul8x8 #(.MODE(3))  u_all (.a(a), .b(b), .p(p_all));
    mul8x8 #(.MODE(4))  u_tr  (.a(a), .b(b), .p(p_tr));
    mul8x8 #(.MODE(5))  u_hy  (.a(a), .b(b), .p(p_hy));

    integer i, j, fd;
    integer err_exact, err_over, n;
    reg [15:0] ref;

    initial begin
        fd = $fopen("sim/products.txt", "w");
        err_exact = 0;
        err_over  = 0;
        n         = 0;
        for (i = 0; i < 256; i = i + 1) begin
            for (j = 0; j < 256; j = j + 1) begin
                a = i;
                b = j;
                #1;
                ref = i * j;
                if (p_beh !== ref || p_ex !== ref) begin
                    err_exact = err_exact + 1;
                    if (err_exact <= 5)
                        $display("EXACT MISMATCH a=%0d b=%0d beh=%0d rec=%0d ref=%0d", i, j, p_beh, p_ex, ref);
                end
                if (p_l > ref || p_lm > ref || p_all > ref || p_tr > ref || p_hy > ref)
                    err_over = err_over + 1;
                $fdisplay(fd, "%0d %0d %0d %0d %0d %0d %0d %0d %0d", i, j, p_beh, p_ex, p_l, p_lm, p_all, p_tr, p_hy);
                n = n + 1;
            end
        end
        $fclose(fd);
        $display("Vectors applied            : %0d", n);
        $display("Exact-design mismatches    : %0d", err_exact);
        $display("Approx over-estimations    : %0d", err_over);
        if (err_exact == 0 && err_over == 0)
            $display("RESULT: PASS");
        else
            $display("RESULT: FAIL");
        $finish;
    end
endmodule
