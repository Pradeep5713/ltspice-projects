# Easy but Novel FPGA Verilog Projects for 4th-Year B.Tech ECE Students — and How to Publish Them

**Recommendation in one line:** build an **area-optimised ASCON-128 lightweight-encryption core in Verilog on a Basys-3 (Artix-7) board**, study how the number of permutation rounds per clock cycle trades area against throughput and power, and publish that measured trade-off against earlier Artix-7 results. It needs no multipliers, no memory interfaces and no external hardware. It builds on the algorithm NIST selected in 2023 as its lightweight-cryptography standard [[high-performance-fpga-implementations-of]], and it produces exactly the tables IEEE and Scopus reviewers expect: LUTs, flip-flops, maximum frequency, power, throughput per LUT, and a comparison with published work. The runner-up is a hand-optimised or approximate multiplier applied to an image filter, which is even simpler to code.

## 1. What Makes an FPGA Project Both Easy and Publishable

A paper is accepted when a reviewer can see a clear delta over existing work and trust the evaluation. Lack of novelty is the most common reason IEEE conference papers are rejected. Weak evaluation comes next: flawed methodology, "insufficient comparisons with state-of-the-art methods", or missing significance [[will-ieee-conference-papers-be-rejected]]. The same themes appear in general rejection analyses: originality, methodological flaws and inadequate analysis top the list [[understanding-the-reasons-for-paper-rejection]]. IEEE conference acceptance rates typically range from 20% to 50% [[will-ieee-conference-papers-be-rejected]].

Engineering work faces a structural handicap. As one senior computer-science researcher puts it, building any system requires integrating a lot of prior art. All that prior art looks familiar to the reviewers [[the-toxic-culture-of-rejection-in-computer-science-acm-sigbed]]. A student FPGA paper must therefore **state its delta in one sentence** and back it with numbers.

The easiest publishable FPGA projects share five properties:

1. **Small, well-specified datapath.** Logic built from XOR, AND and shifts (ciphers, small multipliers) is far easier to write and verify than DDR controllers or video pipelines.
2. **A published baseline on the same FPGA family.** Artix-7 papers exist for SIMON [[fpga-implementation-of-simon-128]], ASCON [[high-performance-fpga-implementations-of]] and small multipliers [[hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas]], so the comparison table almost writes itself.
3. **Metrics Vivado reports for free.** LUT and FF utilisation, timing (critical-path delay, Fmax) and on-chip power come straight from the synthesis and implementation reports. Every paper cited here reports them.
4. **One design knob to sweep.** A design-space exploration (rounds per cycle, operand width, approximation level) turns one implementation into a results section with a trade-off curve.
5. **A cheap board with enough on-board I/O to demo.** The Basys-3 has an Artix-7 XC7A35T with 33,280 logic cells in 5,200 slices, 1,800 Kbits of block RAM, 90 DSP slices and internal clocks above 450 MHz. It also carries 16 switches, 16 LEDs, a 4-digit display, VGA and a USB-UART bridge, and designs are built with the free Vivado WebPACK edition [[1300-henley-court]].

## 2. Ranked FPGA Verilog Project Ideas

Scores are 1 (low) to 5 (high). *Ease* means ease for a 3–4 person B.Tech team in two semesters.

| Rank | Project | Ease | Novelty headroom | Publishability | Why |
|---|---|---|---|---|---|
| **1** | **ASCON-128 lightweight AEAD core, rounds-per-cycle design-space study on Basys-3** | 4 | 4 | 5 | NIST standard since 2023; published Artix-7 baselines to compare against; pure XOR/AND/rotate logic [[high-performance-fpga-implementations-of]] |
| 2 | Hand-optimised or approximate 8-bit multiplier, applied to an image filter or tiny neural network | 5 | 3 | 4 | Tiny Verilog; manual LUT-level design beats `a*b` inference [[hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas]]; approximate variants save 64–67% LUTs [[arxiv231010053v1-csar-16-oct-2023]] |
| 3 | FP8 L-Mul (addition-based multiplication) unit ported to low-cost Artix-7 | 3 | 5 | 4 | Recent algorithm with only one FPGA realisation so far, on an UltraScale+ board [[a-power-efficient-hardware-implementation-of-l-mul]] [[addition-is-all-you-need]] |
| 4 | SIMON-128 cipher with a UART encryption demo | 5 | 2 | 3 | Only 45 LUTs on the same XC7A35T chip, but that exact result is already published [[fpga-implementation-of-simon-128]] |
| 5 | Hand-coded RTL LeNet-5 / MNIST accelerator | 2 | 3 | 4 | A Scopus-journal precedent exists: 97.59% accuracy at 12-bit fixed point [[a-hardware-accelerator-for-the-inference-of-a-convolutional-neural-network]]; but 150 parallel DSP multipliers exceed the Basys-3's 90 DSPs |
| 6 | RISC-V core with a custom-instruction accelerator | 1 | 4 | 4 | Strong results (59.3× speedup) but a 20,922-LUT design on a larger Artix-7 [[risc-v-based-tinyml-accelerator-for]] [[cfu-playground-full-stack-open-source]] |
| 7 | Classic FSM and processor demos (traffic light, MIPS, UART) | 5 | 1 | 1 | Good for learning and mini projects, with source widely available [[fpga-projects-fpga4studentcom]]; nothing new to publish |

**Why SIMON ranks below ASCON despite being easier.** A 2023 paper already reports SIMON-128 on an Artix-7 XC7A35T at 45 LUTs, 27 FFs, 0.072 W and 4.020 ns [[fpga-implementation-of-simon-128]]. Repeating it on the same chip family has no delta. ASCON, by contrast, was standardised in 2023. The most recent high-performance Artix-7 study targets the large xc7a200t part with multi-round unrolled datapaths [[high-performance-fpga-implementations-of]]. That leaves room for a low-cost, area-first study on the entry-level XC7A35T.

**Why the CNN accelerator ranks lower.** It is the most publishable-looking topic, and the LeNet-5 RTL paper appeared in the journal *Ciencia e Ingeniería Neogranadina* [[a-hardware-accelerator-for-the-inference-of-a-convolutional-neural-network]]. But its math engine performs 150 multiplications in parallel on 150 DSP slices [[a-hardware-accelerator-for-the-inference-of-a-convolutional-neural-network]], and the Basys-3 has 90 [[1300-henley-court]]. The design would need time-multiplexing, which is doable but not easy.

## 3. Recommended Project: Scope, Tools, and Novelty Angle

### Working title

*Area-Efficient ASCON-128 Authenticated Encryption on a Low-Cost Artix-7 FPGA: A Rounds-per-Cycle Design-Space Exploration.*

### What ASCON is

ASCON is a family of authenticated-encryption and hashing algorithms that was declared winner of the NIST Lightweight Cryptography competition in February 2023. The official NIST standard was published on 16 June 2023 [[high-performance-fpga-implementations-of]]. Its designers' specification defines the 320-bit state, the substitution layer and the linear diffusion layer that the permutation applies each round [[submission-to-nist]]. That specification is the reference for the Verilog. A 2023 ACM Computing Surveys paper reviews its hardware implementations, side-channel attacks and countermeasures. It is the starting point for the literature review [[arxiv230406222v1-cscr-13-apr-2023]].

### Scope (deliberately small)

| Item | Choice |
|---|---|
| Algorithm | ASCON-128 encryption and decryption with tag generation (optionally ASCON-128a) |
| HDL | Verilog; one permutation-round module instantiated k times |
| Design knob | k = 1, 2, 3, 6 rounds per clock cycle (the prior Artix-7 paper uses 6 for ASCON-128 and 4 for ASCON-128a [[high-performance-fpga-implementations-of]]) |
| Board | Basys-3, XC7A35T [[1300-henley-court]] |
| Tools | Vivado WebPACK (free) for synthesis, implementation, timing and power reports [[1300-henley-court]] |
| Verification | Verilog testbench comparing outputs with a software reference implementation of the specification [[submission-to-nist]] |
| Demo | Plaintext sent over the USB-UART bridge, ciphertext and tag returned; status on LEDs and 7-segment display [[1300-henley-court]] |

### The novelty angle (the one-sentence delta)

State the delta like this: *we report the first rounds-per-cycle area/throughput/power trade-off of ASCON-128 on the entry-level XC7A35T used in teaching boards, and identify the configuration with the best throughput per LUT and energy per bit on this device.* The claim is modest, testable and useful for IoT designers on cheap FPGAs. Before claiming to be first, the team must check the literature (IEEE Xplore, the IACR ePrint archive, Google Scholar). If the claim does not survive, narrow it: a specific k, a power measurement, a different board, or ASCON-Hash.

**Strong extensions, if time allows:**

- **Energy per bit and throughput per LUT** as headline metrics. The prior study reports throughput-to-area, for example 3535.91 Mbps at 1.19 Mbps/LUT for ASCON-128 on Artix-7 [[high-performance-fpga-implementations-of]].
- **A three-cipher benchmark on one board**: SIMON [[fpga-implementation-of-simon-128]] versus ASCON versus a small AES variant, all under identical synthesis settings.
- **A countermeasure add-on**: a simple masking or fault-detection variant, informed by the attack literature [[arxiv230406222v1-cscr-13-apr-2023]].

### Runner-up: approximate multiplier plus application

If the team prefers arithmetic to cryptography, reproduce and extend the multiplier line of work. Kida and Sato show that a hand-built exact 4-bit multiplier on 7-series FPGAs needs only 11 LUTs and 2 CARRY4 blocks with a 2.750 ns critical path. They also show that Vivado does not infer this structure from `p = a*b`, which makes the manual design the contribution [[hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas]]. DyRecMul shows approximate 8-bit multipliers saving 64% of LUTs for signed multiplication with under 0.29% average accuracy loss on deep-learning benchmarks [[arxiv231010053v1-csar-16-oct-2023]].

A B.Tech paper could compose an 8-bit multiplier from optimised 4-bit blocks and add one approximation. It would then report the LUT and delay savings together with output quality on an image-smoothing filter or small network, all on the Basys-3.

## 4. Writing the Research Paper

### Structure (IEEE conference format, typically 4–6 pages, two columns)

1. **Abstract (150–200 words):** problem, method, the headline number and the delta.
2. **Introduction:** why lightweight cryptography matters for IoT, and the gap addressed.
3. **Related work:** a table of prior FPGA implementations with device, LUTs, FFs, frequency and throughput, drawing on the ASCON [[high-performance-fpga-implementations-of]] and SIMON [[fpga-implementation-of-simon-128]] papers and the survey [[arxiv230406222v1-cscr-13-apr-2023]].
4. **Algorithm background:** a brief summary of the ASCON permutation from the specification [[submission-to-nist]].
5. **Proposed architecture:** a block diagram of the datapath and control FSM, and how k rounds per cycle are unrolled.
6. **Implementation and verification:** tool version, device, constraints, testbench and demo.
7. **Results:** resource, timing and power tables for each k, trade-off plots, and a comparison table against prior work.
8. **Conclusion and future work.**

### Results tables reviewers expect

Every FPGA paper cited here reports resources and timing in the same shape. The SIMON paper's comparison row is a good template: power 72 mW versus 239 mW and 248 mW, delay 4.020 ns versus 5.448 ns and 4.415 ns, and area 45 LUTs versus 73 LUTs against Zynq-7000 and Virtex-7 implementations [[fpga-implementation-of-simon-128]].

| Design | Device | LUT | FF | Fmax (MHz) | Throughput (Mbps) | Mbps/LUT | Power (mW) |
|---|---|---|---|---|---|---|---|
| This work, k = 1 | XC7A35T | … | … | … | … | … | … |
| This work, k = 6 | XC7A35T | … | … | … | … | … | … |
| Prior ASCON-128 [cite] | xc7a200t | … | … | … | 3535.91 | 1.19 | … |

Fill the prior-work row only with numbers the cited paper actually reports. The two prior figures shown are from the high-performance Artix-7 study [[high-performance-fpga-implementations-of]].

### Rules that prevent rejection

- **Follow the template exactly.** Wrong templates, page overruns or missing abstracts and keywords can cause desk rejection without technical review [[will-ieee-conference-papers-be-rejected]].
- **Compare with the state of the art.** Insufficient comparison is a common rejection reason [[will-ieee-conference-papers-be-rejected]].
- **Make it reproducible.** State the device part number, tool version, synthesis settings and clock constraint, as the multiplier paper does with Vivado 2024.2 [[hardware-efficient-accurate-4-bit-multiplier-for-xilinx-7-series-fpgas]].
- **Write your own text.** Plagiarism and self-plagiarism are listed rejection reasons [[will-ieee-conference-papers-be-rejected]]. Cite every borrowed idea.

## 5. Where to Publish: IEEE Conferences and Scopus Journals

**IEEE conferences.** Target IEEE-sponsored or technically co-sponsored conferences whose proceedings are published in IEEE Xplore. For a conference claiming Scopus indexing, remember that Scopus indexes the **publication series** (for example IEEE conference proceedings), not the event website. Ask the organiser for the ISBN or last year's volume [[how-to-verify-scopus-indexing-step-by-step-guide-2026]].

**Scopus journals.** Verify every journal yourself before submitting:

- **Search by ISSN, not title,** in the free Scopus Preview source list [[how-to-verify-scopus-indexing-step-by-step-guide-2026]].
- **Check the coverage range.** A range ending in a past year means the title has likely been discontinued, so do not submit there [[how-to-verify-scopus-indexing-step-by-step-guide-2026]].
- **Re-check at acceptance, not only at submission.** Scopus re-evaluates titles continually through an independent selection board and discontinues journals flagged for poor practice [[the-guardians-of-scopus]].

**Predatory red flags** [[how-to-verify-scopus-indexing-step-by-step-guide-2026]]:

- Guaranteed acceptance before peer review.
- Acceptance promised within days.
- Organisers using free email domains rather than institutional ones.
- Unclear or escalating fees.

Elsevier itself notes there is no universally agreed definition of a predatory journal, so check the evidence, not the marketing [[the-guardians-of-scopus]].

## 6. Timeline for a 4th-Year Team

Map the work onto the department's review schedule. GNDEC's major-project scheme, for example, runs proposal, mid-term, end-semester, report and guide reviews worth 200 marks in total [[2014-batch-onwards]].

| Month | Milestone | Review deliverable |
|---|---|---|
| 1 | Literature survey of FPGA ASCON/SIMON papers and prior-work table; read the specification | R1 synopsis: problem, feasibility, objectives [[2014-batch-onwards]] |
| 2 | Single-round (k = 1) ASCON permutation in Verilog; testbench against reference outputs | — |
| 3 | Full ASCON-128 encryption/decryption with tag; simulation passing | R2 mid-term: modular design, time plan [[2014-batch-onwards]] |
| 4 | Implement on Basys-3; UART demo; collect Vivado resource, timing and power reports | — |
| 5 | Sweep k = 1, 2, 3, 6; build trade-off plots and comparison table | R3 end-semester demo |
| 6 | Write the IEEE-format paper; internal review by guide; submit to a verified venue | R4 report, R5 guide evaluation |

**This scope also serves accreditation.** NBA's January 2025 self-assessment template scores capstone project quality at 25 points. It also asks institutions to justify the Program Outcomes each project addresses [[national-board-of-accreditation-2]]. A project that designs, verifies, measures and publishes covers design, investigation, tool usage and communication outcomes in one piece of work.
