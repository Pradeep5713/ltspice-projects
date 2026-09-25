---
title: Hardware-Efficient Accurate 4-bit Multiplier for Xilinx 7 Series FPGAs
id: hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas
tags:
- fpga-verilog-publishable-project-e0cabb
created: '2026-09-25T03:34:13.975963Z'
source: https://arxiv.org/pdf/2510.21533
source_domain: arxiv.org
fetched_at: '2026-09-25T03:34:13.975234Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
raw_file: raw/hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas.pdf
doi: arXiv:2510.21533
---

Hardware-Efficient Accurate 4-bit Multiplier for Xilinx 7 Series FPGAs
Misaki Kida
Shimpei Sato
Graduate School of Science and Technology,
Faculty of Engineering,
Shinshu University
Shinshu University
4-17-1 Wakasato, Nagano-city, Nagano, Japan
4-17-1 Wakasato, Nagano-city, Nagano, Japan
25w6030k@shinshu-u.ac.jp
satos@shinshu-u.ac.jp
Abstract— As IoT and edge inference proliferate,
there is a growing need to simultaneously optimize
area and delay in lookup-table (LUT)–based multipli-
ers that implement large numbers of low-bitwidth op-
erations in parallel. This paper proposes a hardware-
efficient accurate 4-bit multiplier design for AMD
Xilinx 7-series FPGAs using only 11 LUTs and two
CARRY4 blocks. By reorganizing the logic functions
mapped to the LUTs, the proposed method reduces
the LUT count by one compared with the prior 12-
LUT design while also shortening the critical path.
Evaluation confirms that the circuit attains minimal
resource usage and a critical-path delay of 2.750 ns.
I.
Introduction
With the proliferation of the Internet of Things (IoT)
and edge computing, there is growing demand for arith-
metic circuits that deliver near-real-time, high through-
put under tight budgets on power, silicon area, and
memory bandwidth.
Unlike large cloud-side acceler-
ators, edge platforms operate under strict power and
thermal envelopes, and their latency and responsiveness
requirements vary across applications.
Consequently,
field-programmable gate arrays (FPGAs)—which are pro-
grammable yet amenable to specialization that improves
energy efficiency—have become a compelling option.
Deep neural network (DNN) inference is a representa-
tive FPGA-accelerated workload.
Low-bit quantization
(e.g., 8-bit or 4-bit) reduces the bit-width of weights and
activations, simultaneously lowering memory bandwidth
and arithmetic cost and, as a result, enabling both re-
duced data movement and increased parallelism. On FP-
GAs, inference engines typically realize such low-precision
arithmetic by instantiating many small-granularity mul-
tipliers in parallel.
The look-up table (LUT) footprint
and critical-path delay of each multiplier determine the
overall degree of parallelism and the achievable maximum
operating frequency (Fmax).
Therefore, even marginal
per-multiplier improvements in LUT count or delay can
translate into non-negligible system-level gains in perfor-
mance, area, and power when deploying dense arrays of
multipliers.
Although 4-bit and 8-bit multiplications can be im-
plemented using digital signal processing (DSP) blocks
via SIMD-style packing, DSP resources impose strong
constraints due to their limited count, fixed placement,
and the long interconnect they often require. In designs
that pack arithmetic units as densely as DNN acceler-
ators, these constraints can lead to routing congestion
and Fmax saturation.
Moreover, heavy use for multi-
plication can leave insufficient resources for accumulators
and for quantization/activation logic. As a result, there
remains strong demand for LUT-based low-bit multipli-
ers, and area-efficient, high-performance multipliers are of
particular importance.
This work proposes a design for a 4-bit accurate mul-
tiplier with low LUT usage and low latency. Whereas a
commonly used design requires 12 LUTs for a 4-bit mul-
tiplier [1], our design realizes the same function with 11
LUTs, thereby reducing area. In addition, our multiplier
shortens the critical path relative to existing designs, fur-
ther lowering latency. We validate the effectiveness of the
design on AMD Xilinx 7-series FPGAs.
The remainder of this paper is organized as follows.
Section 2 reviews the relevant FPGA logic architecture.
Section 3 summarizes prior accurate multipliers used as
baselines. Section 4 details the structure and operation
of the proposed 4-bit multiplier. Section 5 presents an
empirical evaluation of performance.
Section 6 applies
pipelining to the proposed design and evaluates its im-
pact. Section 7 concludes.
II.
Preliminary
In Xilinx FPGAs, the fundamental logic element is
the slice. Each slice contains four 6-input lookup tables
(LUTs). Figure 1 shows the organization of a LUT6 and a
LUT6 2. A LUT ordinarily operates as a 6-input, single-
output function (referred to as a LUT6). By controling
the final-stage multiplexer, the same resource can also be
used as two 5-input, single-output LUTs that share their
inputs; this mode is exposed as the LUT6 2.
Both LUT6 and LUT6 2 are provided as synthesizable
primitives in Vivado and can be instantiated directly in
HDL. In these primitives, the output for every input com-
bination is specified by initializing the truth table (the
INIT parameter).
arXiv:2510.21533v1  [cs.AR]  24 Oct 2025


---

I₅
I₄
I₃
I₂
I₁
I₀
O₆
LUT5
LUT5
LUT6
MUX
1
0
1
I₄
I₃
I₂
I₁
I₀
O₆
LUT5
LUT5
LUT6_2
MUX
1
0
O₅
Fig. 1. Configuration of LUT6 and LUT6 2. Xilinx LUTs
can be configured to operate as either a 6-input 1-output or
a 5-input 2-output device by setting the MUX behavior.
DI(3:0)
S(3:0)
CYINIT
CI
O(3:0)
CO(3:0)
0
0
1
1
CARRY4
0
1
0
1
0
1
Fig. 2. CARRY4 configuration. The result of adding the values
input via DI and S, including the carry, is output to O.
A slice also includes dedicated carry logic called
CARRY4, which allows the outputs of the LUTs to feed
the carry chain directly. Figure 2 illustrates the structure
of CARRY4.
CARRY4 computes four bits of carry in
one block, enabling addition with significantly lower de-
lay than a carry chain implemented solely with LUTs. As
with the LUTs, CARRY4 is available as a synthesizable
primitive in Vivado and can be instantiated in HDL.
The most significant carry output of a CARRY4, CO[3],
is hard-wired to the Cin of the adjacent slice. This permits
long carry chains to be built without traversing the gen-
eral routing fabric. On the other hand, when this carry
output is used as an input to a LUT, it must traverse
the neighboring CARRY4 and the general routing fabric,
which increases the routing delay.
III.
Related Works
This section reviews prior work on 4-bit multipliers for
FPGAs.
Yao et al. [1] proposed 4-bit and 8-bit approximate mul-
tipliers for FPGAs and, as the basis of their designs, de-
veloped an exact 4-bit multiplier. Their exact design is
implemented with 12 LUTs and one CARRY4.
Ullah et al. [2] presented exact and approximate multi-
pliers of sizes 4×2, 4×4, and 8×8. In their work, the exact
4×4 multiplier is built from two exact 4×2 multipliers and
two CARRY4s.
Ullah et al. [3] proposed a design-space exploration
method to generate approximate multipliers of arbi-
trary bit widths, and—for comparison—also provided a
methodology for exact multipliers of arbitrary widths.
The 4-bit exact multiplier shown in their paper uses 12
LUTs and three CARRY4s.
Rehman et al. [4] proposed an ASIC-oriented architec-
tural exploration framework to generate multipliers with
a wide range of approximation levels. In that context, the
4-bit exact multiplier used for comparison is composed of
four exact 2-bit multipliers.
Wang et al. [5] introduced unsigned approximate multi-
pliers that combine the Booth algorithm with probabilis-
tic error correction, achieving substantial area reductions
for larger bit-widths. The 4-bit exact multiplier employed
in their evaluation uses 13 LUTs and four CARRY4s.
Guo et al. [6] proposed hardware-efficient FPGA-based
approximate multipliers featuring LUT sharing and carry
switching, together with a library of 8-bit approximate
multipliers supporting multiple multiplication modes. To
illustrate the methodology of LUT sharing and carry
switching, they show a 4-bit exact multiplier implemented
with 13 LUTs and one CARRY4.
All of the above works primarily focus on proposing ap-
proximate multipliers. In each case, an exact multiplier is
also provided either as a baseline for the approximate de-
signs or as a comparison point. Compared with these ex-
act baselines, the exact multiplier proposed in this paper
uses fewer resources and exhibits a shorter critical-path
delay.
IV.
Proposed Design
This section describes the architecture of the proposed
4-bit multiplier and explains how we achieve low latency
and low resource usage using a combination of LUTs and
a CARRY4 carry chain.
Using Fig. 3, we first illustrate 4-bit multiplication.
Given the multiplicand A = (a3, a2, a1, a0) and the multi-
plier B = (b3, b2, b1, b0), we generate sixteen partial prod-
ucts (PPs) by ANDing every bit of A with every bit of
B. These PPs are then accumulated by addition.
The
additions proceed column-wise from the least significant
bit (LSB) upward while propagating carries.
The final
product is an 8-bit word P = A × B.
Fig. 4 shows the overall organization of the proposed
multiplier. The design uses 11 LUTs in total together with
2 CARRY4 blocks. In the figure, LUTs are numbered 1
through 11, and the CARRY4 blocks are labeled Carry
Chain A and Carry Chain B. For each LUT, the inputs
are listed above the symbol and the outputs below it.
Xilinx FPGAs provide two types of 6-input LUT prim-
itives: a single-output LUT (LUT6) and a dual-output
LUT (LUT6 2).
Our implementation uses three dual-
output LUTs (LUTs 1, 5, and 7) and eight single-output
LUTs. To realize a fast carry-propagate adder, the out-
put bits P3 through P7 are produced using the CARRY4


---

A3B3
A2B3
A1B3
A0B3
A3B2
A2B2
A1B2
A0B2
A3B1
A2B1
A1B1
A0B1
A3B0
A2B0
A1B0
A0B0
A3       A2       A1       A0
B3       B2       B1       B0
P0
P1
P2
P3
P4
P5
P6
P7
×
+
Fig. 3. Partial Product Accumulation for 4-bit multiply
block.
Table I presents, for each LUT in Fig. 4, the Boolean
function it implements together with its inputs and out-
puts. Column 1 lists the LUT indices corresponding to
Fig. 4. Column 2 gives the Boolean expression realized
by each LUT; the term set in boldface denotes the LUT
output signal. Column 3 lists the input signals fed to each
LUT. Inputs are ordered as I0–I6, and unused inputs are
tied to logic ‘1’. Column 4 indicates the output signal(s):
when a single output is used we instantiate LUT6, and
when two outputs are used we instantiate the dual-output
primitive LUT6 2. Column 5 provides the INIT value that
defines the LUT function, given in hexadecimal notation.
A key aspect of the proposal is the reduction in required
signals for the carry computation in the addition stage by
algebraically simplifying the carry logic.
In particular,
the signal C1 (implemented in the LUT #6), which is the
carry produced in the S1 column, would naively be written
as: C1 = (A1B2·A2B1) ∥(A1B2·(A1B1·A0B2·A2B0)) ∥
(A2B1 · (A1B1 · A0B2 · A2B0)).
By observing logical
dominance, this can be simplified to C1 = A1B2 · A2B1,
thereby reducing the number of required signals and, in
turn, the number of LUTs.
The proposed design uses two CARRY4 units to imple-
ment a four-digit carry chain. This is because Xilinx FP-
GAs have a structure where the most significant output
of a CARRY4 is directly input to the adjacent CARRY4.
Implementing this with an one CARRY4 would cause
significant wiring delay for the most significant output,
increasing critical path delay.
If the design allows the
top-level output to be input directly into an adjacent
CARRY4, then a single CARRY4 can be used for im-
plementation.
Finally,
we
note
that
in
Xilinx’s
Vivado
2024.2
toolchain, an RTL description written simply as a prod-
uct (e.g., p = a ∗b) does not infer our proposed structure.
A central contribution of this work is to show that a care-
fully manually designed 4-bit multiplier achieves higher
performance than the automatically synthesized counter-
part.
V.
Experimental Results
We compare the proposed multiplier with related work
and existing IP introduced in Chapter 3.
We evaluate
Carry Chain B
P7
P6
P5
P4
P3
11
B3
A3
B2
A2
B1
A1
PropB[2]
10
B3
A3
B2
A2
B1
A1
GenB[2]
9
B3
A3
B2
A2
B1
A1
PropB[1]
8
B3
A3
B2
A2
B1
A1
GenB[1]
7
1 1 S3
S1
A3
B0
PropB[0]
GenB[0]
6
B3
A3
B2
A2
B1
A1
S3
5
1
S1
B3
A3
B0
A0
PropA[3]
GenA[3]
4
B2
A2
B1
A1
B0
A0
S1
2
B2
A2
B1
A1
B0
A0
P2
3
B2
A2
B1
A1
B0
A0
PropA[2]
1
1 1 B1
A1
B0
A0
P1
P0
Carry Chain A
0
0
0
1
1
CO_B[2]
O_A[3]
O_B[0]
O_B[1]
O_B[2]
0 1
Fig. 4. Block diagram of proposed accurate 4-bit multiplier.
resource utilization and critical path delay to demonstrate
the advantages of the proposed 4-bit multiplier.
All multipliers under evaluation are described in Verilog
HDL and synthesized using Vivado 2024.2. The target
FPGA for implementation is the Arty A7 equipped with
an Artix 7 35T. Unless otherwise stated, we employ area-
oriented synthesis settings (e.g., Area Optimized high) to
minimize resource utilization. Functional correctness is
verified by exhaustive simulation over all input combina-
tions, confirming that each design computes the product
exactly.
Below, we describe the multipliers used as baselines in
addition to those in the references. “Proposed” denotes
the multiplier introduced in this paper. “Exact” is ob-
tained by describing the product as (A × B) and synthe-
sizing it directly. “Vivado IP” refers to a multiplier gen-
erated with the multiplier IP included in Vivado 2024.2.
Furthermore, we include the 4-bit multipliers reported in
the works surveyed in Chapter 3 as additional compara-
tors.
Table II summarizes the resource utilization of each
multiplier. The reported metrics are the number of LUTs
and the number of CARRY4 primitives. The compari-
son set includes the Proposed design, the 4-bit multipli-
ers LM [1] and Acc [2], the designs in [3], [4], [5], [6], as
well as Exact and Vivado IP. For Exact and Vivado IP, we
evaluate two synthesis strategies: an area-oriented setting
(Area Opt high) and a delay-oriented setting (Perf Opt).
Table III reports the critical path delay (CPD) of each
multiplier.
These values are post–place-and-route esti-
mates. The comparison set includes the Proposed design;
the 4-bit multipliers LM [1] and Acc [2]; the design in [6];
as well as Exact and Vivado IP. We report the breakdown
of CPD into logic delay and routing (net) delay, together
with their sum (Total CPD).
From Tab. II and Tab. III, the proposed multiplier con-
sists of 11 LUTs and 2 CARRY4 units, exhibiting the low-
est resource usage compared to other multipliers. Regard-
ing delay, the critical path delay of the proposed multiplier
is 2.750 ns, the second smallest after both Exact config-
urations. Although the Exact attains a slightly shorter
delay, it uses more LUTs than the proposed design and,
in terms of slice resources, consumes more slices as well.
Fig. 5 is a scatter plot of all multipliers, with LUT count


---

TABLE I
Implementation details for all LUTs of proposed accurate 4-bit multiplier. Shows the logic functions implemented in the
LUT, input/output signals, and INIT values.
LUT
Function
Input
Output
INIT Value
1
P0 = A0B0
P1 = A1B0 ⊕A0B1
A0, B1, B0, A1, 1, 1
P0, P1
0x78887888A0A0A0A0
2
P2 = A2B0 ⊕A1B1 ⊕A0B2 ⊕(A0B1 · A1B0)
A2, B0, A0, B1, A1, B2
P2
0xF8808080C8000000
3
C0 = A1B1 · A0B2 ∥A2B0 · A1B1 ∥A2B0 · A0B2 ∥(A0B1 · A1B0)
B2, A2, B0, A0, B1, A1
C0
0x653F6AC06AC06AC0
4
S1 = A1B2 ⊕A2B1 ⊕(A1B1 · A0B2 · A2B0)
A1, B2, A2, A0, B1, B0
S1
0xF878888878788888
5
Prop0 = (S1 ⊕A3B0) ⊕A0B3
Gen0 = (S1 ⊕A3B0) A0B3
B3, A0, S1, A3, B0, 1
Prop0, Gen0
0x8778787808808080
6
S2 = A3B1 ⊕A2B2 ⊕A1B3
C1 = A1B2 · A2B1
S3 = S2 ⊕C1
B3, A1, B1, A3, B2, A2
S3
0x47B7788878887888
7
Prop1 = S3 ⊕(S1 · A3B0)
Gen1 = S3 · (S1 · A3B0)
B0, S1, A3, B3, 1, 1
Prop1, Gen1
0x7F807F8080008000
8
C2 = A3B1 · A2B2 ∥A1B3 · A2B2 ∥A3B1 · A1B3
C3 = S2 · C1
S4 = A3B2 ⊕A2B3 ⊕C2
Prop2 = S4 ⊕C3
A2, B1, B3, A1, B2, A3
Prop2
0x8000000000000000
9
Gen2 = S4 · C3
A2, B1, B3, A1, B2, A3
Gen2
0x37D760A008A0A0A0
10
C4 = A3B2 · A2B3 ∥A3B2 · C2 ∥A2B3 · C2
Prop3 = A3B3 ⊕C4
B2, B1, A3, A1, A2, B3
Prop3
0xE0A0800000000000
11
Gen3 = A3B3 · C4
A2, B1, B2, A1, B3 A
Gen3
0x175F8080A0000000
proposed
LM[1]
Acc[2]
LOAM[6]
Exact(AreaOptimized_high)
Exact(PerformanceOptimized)
Vivado IP(AreaOptimized_high)
Vivado IP(PerformanceOptimized)
Fig. 5. Performance comparison of 4-bit multipliers.
on the x-axis and critical path delay (CPD) on the y-axis.
Both axes are oriented so that smaller values lie toward
the origin at the lower left; accordingly, points closer to
the lower-left corner indicate better designs.
From the
figure, the proposed multiplier is seen to achieve both low
resource usage and short delay simultaneously.
VI.
Conclusion
In this paper, we propose an exact 4-bit multiplier for
AMD Xilinx 7-series FPGAs that achieves a small hard-
ware footprint and low latency. By carefully organizing
the logic functions mapped to LUTs, the multiplier is re-
alized using only 11 LUTs and two CARRY4 primitives.
Our evaluation shows that, compared with existing mul-
TABLE II
Comparison of hadoware resource for 4-bit multipliers.
Multiplier
LUTs
CARRY4
Proposed
11
2
LM [1]
12
1
Acc [2]
15
3
[3]
12
3
[4]
16
0
[5]
13
4
LOAM [6]
13
1
Exact(Area Opt high)
15
2
Exact(Perf Opt)
20
2
Vivado IP(Area Opt high)
13
2
Vivado IP(Perf Opt)
15
2
tipliers and those produced by automatic logic synthesis,
the proposed design uses fewer resources and attains a
critical-path delay of 2.750 ns, demonstrating strong per-
formance.
References
[1] Shangshang Yao and Liang Zhang.
Hardware-efficient fpga-
based approximate multipliers for error-tolerant computing. In
2022 International Conference on Field-Programmable Technol-
ogy (ICFPT), pages 1–8, 2022.
[2] Salim Ullah, Semeen Rehman, Muhammad Shafique, and Akash
Kumar. High-performance accurate and approximate multipli-
ers for fpga-based hardware accelerators.
IEEE Transactions
on Computer-Aided Design of Integrated Circuits and Systems,
41(2):211–224, 2022.
[3] Salim Ullah, Sanjeev Sripadraj Murthy, and Akash Kumar.
Smapproxlib: Library of fpga-based approximate multipliers. In
2018 55th ACM/ESDA/IEEE Design Automation Conference
(DAC), pages 1–6, 2018.


---

TABLE III
Comparison of CPD for 4-bit multipliers
Multiplier Name
CPD [ns]
Total
Logic
Net
Proposed
2.750
1.302
1.448
LM [1]
3.299
1.910
1.389
Acc [2]
3.979
1.978
2.001
LOAM [6]
3.301
1.555
1.746
Exact(Area Opt high)
2.728
1.259
1.469
Exact(Per Opt)
2.533
1.224
1.309
Vivado IP(Area Opt high)
3.739
1.607
2.132
Vivado IP(Per Opt)
3.393
1.586
1.807
[4] Semeen Rehman, Walaa El-Harouni, Muhammad Shafique,
Akash Kumar, Jorg Henkel, and J¨org Henkel.
Architectural-
space
exploration
of
approximate
multipliers.
In
2016
IEEE/ACM International Conference on Computer-Aided De-
sign (ICCAD), pages 1–8, 2016.
[5] Haonan Wang, Ke Chen, Chenggang Yan, Bi Wu, and Weiqiang
Liu. Hardware-efficient accurate and approximate fpga multi-
pliers for error-tolerant applications. In 2023 IEEE 66th Inter-
national Midwest Symposium on Circuits and Systems (MWS-
CAS), pages 977–981, 2023.
[6] Yi Guo, Qilin Zhou, Xiu Chen, and Heming Sun. High-efficiency
fpga - based approximate multipliers with lut sharing and carry
switching. In 2024 Design, Automation & Test in Europe Con-
ference & Exhibition (DATE), pages 1–2, 2024.
