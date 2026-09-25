# B.Tech ECE Projects: A Domain-by-Domain Guide to Choosing, Building, and Presenting Them

A B.Tech Electronics and Communication Engineering (ECE) project is graded less on how exotic the idea is and more on whether the student can identify a real problem, design a solution with defensible engineering choices, verify it, and document it. Indian accreditation now scores the major project explicitly: the National Board of Accreditation's (NBA) January 2025 Self-Assessment Report template gives **25 points** to "Quality of Student Capstone Project" and asks institutions to justify which Program Outcomes each project addresses [[national-board-of-accreditation-2]]. The ideas below span the full breadth of ECE, from analog circuits to 5G antennas, each paired with the tools, difficulty, and evidence base that make it defensible in front of an examiner.

## 1. How to Choose a B.Tech ECE Project

### What examiners actually grade

Department rubrics reveal what matters. Guru Nanak Dev Engineering College's (GNDEC) ECE major-project scheme is typical: **200 marks over five reviews**, split 60% internal (120 marks) and 40% external (80 marks) [[2014-batch-onwards]].

| Review | What is assessed | Weight |
|---|---|---|
| R1 — Synopsis/proposal | Problem identification, study of existing systems, feasibility, objectives and methodology | 9% (18) |
| R2 — Mid-term | Division of the problem into modules, choice of framework, time plan adherence, presentation | 9% (18) |
| R3 — End-semester | Working implementation and demonstration | 15% (30) |
| R4 — Project report | Documentation quality | 15% (30) |
| R5 — Guide evaluation | Supervisor's continuous assessment | 12% (24) |
| External | Final viva/demonstration | 40% (80) |

Two lessons follow. First, nearly a fifth of the marks (R1 + R2) are awarded before anything works, for problem analysis and planning. Second, the report alone is worth as much as the end-semester demo [[2014-batch-onwards]].

### Map the project to Program Outcomes

Under NBA's GAPC v4.0 framework there are now **11 Program Outcomes (POs)**, down from 12. The old "Society" and "Environment and Sustainability" outcomes were merged into PO6 "The Engineer and the World" [[the-11-program-outcomes-pos-of-nba-gapc-v40-explained]]. The official SAR lists them as follows [[national-board-of-accreditation-2]]:

- **PO1** Engineering Knowledge
- **PO2** Problem Analysis
- **PO3** Design/Development of Solutions
- **PO4** Conduct Investigations of Complex Problems
- **PO5** Engineering Tool Usage
- **PO6** The Engineer and the World
- **PO7** Ethics
- **PO8** Individual and Collaborative Team Work
- **PO9** Communication
- **PO10** Project Management and Finance
- **PO11** Life-Long Learning

The SAR measures capstone quality in terms of factors including "environment, sustainability, safety, ethics, cost" and project type [[national-board-of-accreditation-2]]. A separate 20-point criterion (2.7) rewards projects that solve complex engineering problems while targeting UN Sustainable Development Goals [[national-board-of-accreditation-2]]. In practice, a project with an explicit sustainability or social angle (solar MPPT charging, low-cost health monitoring, energy metering) is easier for a department to justify than an equally hard project with no stated beneficiary.

### A selection checklist

- **Problem first, parts second.** R1 grades problem-domain analysis and feasibility against existing systems [[2014-batch-onwards]]. A one-page comparison with two or three published implementations is worth more than a longer component list.
- **Verifiable outcome.** Choose a project with a measurable result (cutoff frequency, efficiency, classification accuracy, return loss) so the report has numbers to defend.
- **Match hardware to budget and lead time.** Parts can take weeks to arrive; ordering late is one of the most common capstone failures [[keep-the-big-picture-in-mind-the-byu-design-review]].
- **Prefer depth over novelty theatre.** Project-selling vendor lists repeat the same titles (GSM automation, smart home, vehicle tracking) across sites [[top-final-year-project-ideas-for-ece-students-20252026]] [[final-year-embedded-system-projects-2025-maven-silicon]]. Taking a common idea and adding real analysis (a measured comparison, an algorithm variant, a simulation-versus-hardware study) differentiates it more than an unusual title does.

## 2. Project Ideas by ECE Domain

Difficulty is rated for a typical B.Tech team: ★ mini-project scale, ★★ solid final-year, ★★★ ambitious final-year or publishable.

### 2.1 Analog circuits and circuit simulation

Analog projects are cheap, simulation-friendly, and teach the fundamentals examiners probe in viva.

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| Active low-pass/high-pass filter design and verification (Sallen-Key, multiple-feedback) | ★ | LTspice, op-amps, R/C | Filter theory, Butterworth/Bessel/Chebyshev trade-offs [[application-note]] |
| Bandpass, notch (Twin-T), state-variable and Tow-Thomas filters on breadboard | ★★ | OP27/OP37, ADALM2000 or bench instruments | Higher-order and multi-output filter topologies [[activity-active-filtering-analog-devices-wiki]] |
| ECG signal-conditioning front end (filter chain simulated then built) | ★★ | LTspice, LT1490-class op-amp | Biomedical signal chain; AC sweep plus transient/FFT verification [[eece-2510-circuits-and-signals-biomedical]] |

TI's application note on active low-pass design gives unity-gain and equal-component Sallen-Key and multiple-feedback topologies, with coefficient tables for Butterworth, Bessel and Chebyshev responses. That is enough to carry a filter project from specification to component values [[application-note]]. Northeastern University's biomedical circuits lab gives a ready methodology. First, build first-order active filters in LTspice and run `.ac dec 100 1 1000000` to find the cutoff, then compare it with the RC-time-constant prediction. Next, drive a 200 Hz pulse and inspect the output spectrum with an FFT [[eece-2510-circuits-and-signals-biomedical]]. The Analog Devices University Program lab extends this to Sallen-Key, state-variable, Tow-Thomas and Twin-T notch filters with exact component values [[activity-active-filtering-analog-devices-wiki]].

**How to make it final-year grade:** design a complete multi-stage filter to a specification (for example, an ECG band of interest with 50 Hz notch), simulate it, build it, and report simulated-versus-measured responses with a tolerance analysis.

### 2.2 Digital design, VLSI and FPGA

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| FSM-based controllers (traffic light, car parking, alarm clock) | ★ | Verilog/VHDL, Basys 3 or similar FPGA | Sequential logic and FSM design [[fpga-projects-fpga4studentcom]] |
| UART, FIFO, PWM generator, FIR filter in HDL | ★–★★ | Verilog, simulator | Protocol and DSP blocks in hardware [[fpga-projects-fpga4studentcom]] |
| Low-power ALU / Booth multiplier with clock and power gating | ★★ | Verilog, synthesis reports | Low-power techniques (DVS, power gating, clock gating) [[comprehensive-guide-to-final-year-vlsi-projects-for-ece-students]] |
| 32-bit RV32I RISC-V processor, 5-stage pipeline with hazard unit | ★★★ | Verilog, ModelSim, FPGA | Computer architecture, forwarding and stalling [[design-and-simulate-risc-v-procesor-using-verilog]] |
| Small RISC-V soft-core SoC on a low-cost FPGA | ★★★ | FemtoRV, open-source FPGA flow | Full-system integration (UART, SPI, display) [[readmemd]] |

fpga4student.com indexes 69 FPGA projects with full Verilog/VHDL source, from adders and FIFOs to single-cycle and pipelined MIPS processors and OV7670 camera interfacing on a Basys 3 board [[fpga-projects-fpga4studentcom]]. That makes it a good reference for implementation detail, though the source should be studied, not copied.

The RISC-V processor is the strongest digital project because a complete academic reference exists. A 2023 UTAR dissertation documents a 32-bit RV32I five-stage pipeline (IF-ID-EX-MEM-WB) in Verilog with a hazard unit that implements both forwarding and stalling. The design is verified with ModelSim testbenches, and the dissertation lists its limitations (no ISA extensions, no branch prediction) [[design-and-simulate-risc-v-procesor-using-verilog]]. That list of limitations is itself a menu of extensions a B.Tech team could add. For a lighter entry point, the open learn-fpga material builds FemtoRV, whose smallest RV32I variant is about 400 documented lines of Verilog. Its SoC fits in under 1280 LUTs on a Lattice IceStick [[readmemd]].

Vendor VLSI guides frame the rest of the field: low-power design, ADC design and simulation, DSP algorithms (FFT, filters) in HDL, and FPGA-based encryption or communication blocks [[comprehensive-guide-to-final-year-vlsi-projects-for-ece-students]]. Treat these as a topic map, not as authorities; they are course-marketing pages [[final-year-projects-on-vlsi-for-electronicsece-students]].

### 2.3 Embedded systems and IoT

This is the most common category on Indian project lists, which is both its strength (abundant references) and its weakness (examiners have seen it many times).

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| IoT smart home automation | ★ | NodeMCU/ESP8266, relays, Blynk | Wi-Fi control, cloud dashboards [[final-year-embedded-system-projects-2025-maven-silicon]] |
| Smart irrigation / environmental WSN | ★–★★ | Arduino, soil and weather sensors, GSM | Sensing and actuation loops [[top-final-year-project-ideas-for-ece-students-20252026]] |
| Smart energy meter with theft detection | ★★ | STM32, current sensors, GSM | Metering, anomaly flagging [[final-year-embedded-system-projects-2025-maven-silicon]] |
| Accident detection and GPS/GSM vehicle tracking | ★★ | GPS, GSM, accelerometer | Location services, alerting [[top-final-year-project-ideas-for-ece-students-20252026]] |
| EV battery management system (cell voltage, temperature, charge/discharge monitoring) | ★★–★★★ | STM32/Arduino, voltage/current/temperature sensors | Automotive embedded, safety logic [[final-year-embedded-system-projects-2025-maven-silicon]] |
| Object detection with Raspberry Pi and OpenCV | ★★ | Raspberry Pi, camera, OpenCV | Embedded vision [[final-year-embedded-system-projects-2025-maven-silicon]] |

Maven Silicon singles out the EV battery management system as one of the most in-demand automotive-embedded project types for 2025 [[final-year-embedded-system-projects-2025-maven-silicon]].

**How to lift a common IoT idea:** add a quantitative evaluation such as power consumption per day on battery, end-to-end alert latency, or false-alarm rate, and compare it with a published baseline.

### 2.4 Communication systems, SDR and RF/antennas

Communication projects cover the communication side of ECE and are under-represented in vendor lists, which lean heavily towards IoT.

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| FM broadcast receiver in GNU Radio | ★ | RTL-SDR dongle, GNU Radio Companion | Sampling, filtering, decimation, demodulation [[introductory-tutorial-for-sdr]] [[an-introduction-to-sdrs-and-gnu-radio-using-an-rtl-sdr]] |
| ADS-B aircraft tracking at 1090 MHz, airband reception | ★ | RTL-SDR | Real-world packet decoding [[best-sdr-for-gnu-radio-projects-student-to-research-setups]] |
| BPSK/QPSK/OFDM transceiver | ★★–★★★ | ADALM-Pluto (TX/RX) | Digital modulation, synchronisation [[best-sdr-for-gnu-radio-projects-student-to-research-setups]] |
| Microstrip patch antenna design, fabrication and VNA measurement | ★★ | CST/HFSS, FR4, LibreVNA/NanoVNA | Impedance matching, S11, radiation [[leveraging-inexpensive-lab-tools]] |
| 28 GHz 5G mmWave patch antenna (simulation study) | ★★ | CST Microwave Studio, Rogers substrate | mmWave design, parasitic elements for gain/bandwidth [[2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024]] |
| Antenna array modelling and beam steering | ★★★ | Array simulation, multi-channel SDR | Phased arrays, MIMO basics [[leveraging-inexpensive-lab-tools]] |

**Hardware tiers.** SDR hardware scales with ambition [[best-sdr-for-gnu-radio-projects-student-to-research-setups]]:

- **RTL-SDR** (receive-only): FM, ADS-B and DSP lessons.
- **HackRF**: wideband half-duplex work.
- **ADALM-Pluto**: transmit/receive digital-communication teaching (BPSK/QPSK/OFDM).
- **bladeRF and USRP**: MIMO and research testbeds.

GNU Radio itself is a free, block-based real-time signal-processing framework, and the GNU Radio Conference 2023 beginner tutorial packages DSP, SDR and wideband-FM labs as Jupyter notebooks [[introductory-tutorial-for-sdr]].

**Antenna projects are feasible on a budget.** Carnegie Mellon's board-level RF course runs six labs, from transmission-line network analysis through patch antenna design and characterisation to live beam steering, for under $9,000 in one-time equipment. It uses the open-source LibreVNA (100 kHz–6 GHz) rather than the NanoVNA, which is limited to 1 GHz [[leveraging-inexpensive-lab-tools]]. A single team needs only a fraction of that setup.

For a 5G angle, a 2024 conference paper designs a 28 GHz patch with a U-shaped parasitic ground-plane element. In CST it reports −21.4 dB return loss, VSWR 1.18, 2.026 GHz bandwidth and 8.19 dBi gain, and it benchmarks the design against earlier ones [[2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024]]. That benchmarking table is the model to follow: a mmWave antenna is usually a simulation-only project for undergraduates, so comparing against published designs is what makes it defensible.

### 2.5 Signal processing and AI at the edge

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| Keyword spotting / voice commands on ESP32 | ★★ | ESP32, microphone, Edge Impulse, TFLite Micro | MFCC features, quantised inference [[deploying-real-time-speech-recognition-on-esp32-using-tinyml-and-edge-impulse-sp]] |
| Vision wake-word or anomaly detection on a microcontroller | ★★–★★★ | MCU, TFLite Micro | Architecture search, memory-constrained ML [[micronets-neural-network-architectures-for-deploying]] |
| FIR/FFT filter blocks in hardware | ★★ | Verilog/VHDL | DSP-in-hardware [[fpga-projects-fpga4studentcom]] |

A 2025 study deployed keyword recognition on an ESP32 using MFCC features, a subset of the Google Speech Commands dataset, and Edge Impulse's EON compiler. It reports 87.14% test accuracy, 266 ms latency, and 37% RAM and 27% ROM reductions from quantisation [[deploying-real-time-speech-recognition-on-esp32-using-tinyml-and-edge-impulse-sp]]. Those figures double as a baseline for a B.Tech team to compare against. The underlying Speech Commands dataset was released openly (CC BY 4.0) specifically so small on-device models can be compared like-for-like [[arxiv180403209v1-cscl-9-apr-2018]].

Edge Impulse covers the whole workflow of data collection, feature extraction, training and hardware-specific deployment [[edge-impulse-an-mlops-platform-for-tiny-machine-learning]], so it lowers the barrier. That also means the report must explain what the team did beyond clicking through the pipeline, such as dataset curation, a noise-robustness test, or a model-size-versus-accuracy sweep. MicroNets shows that model latency on microcontrollers scales roughly linearly with operation count, a useful principle for a project that compares model variants [[micronets-neural-network-architectures-for-deploying]].

### 2.6 Power electronics and energy

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| DC-DC buck converter designed from first principles | ★★ | LTspice, MOSFET, inductor, controller IC | Duty cycle, ripple, component sizing [[application-note-2]] |
| Buck converter with Type-III compensation and efficiency measurement | ★★★ | Controller IC, bench instruments | Loop stability, loss budgeting [[application-report]] |
| Arduino MPPT solar charge controller (Perturb & Observe) | ★★ | Arduino, PV panel, 12 V battery | Maximum power point tracking [[niu-journal-of-humanities]] |
| Catalogue topics: inverters, BLDC drives, wireless power transfer, LLC converters | ★★–★★★ | varies | Broader topic menu [[top-100-power-electronics-projects-for-engineering-students]] |

Texas Instruments' application notes give an unusually complete design path:

- **SLVA477** provides the step-by-step power-stage equations: maximum duty cycle D = VOUT/(VIN(max) × η), inductor sizing for 20–40% ripple current, diode and capacitor selection [[application-note-2]].
- **SLVA432** walks through Type-III compensation for a synchronous buck converter, targeting a crossover near fSW/5 with about 60° phase margin, with measured efficiency up to 95% on its reference design [[application-report]].
- **SLVA057**, the classic reference, derives the buck power stage's steady-state and small-signal behaviour in both continuous and discontinuous conduction [[note-3973e022]].

A team can simulate the converter in LTspice from these equations, build it, and report predicted-versus-measured ripple and efficiency.

For a renewable-energy angle, a 2024 paper documents an Arduino Uno MPPT charge controller using the Perturb & Observe algorithm for a 12 V battery bank. It cites prior work showing MPPT lifts PV power-extraction efficiency to about 97% [[niu-journal-of-humanities]], and it maps naturally onto NBA's sustainability criterion [[national-board-of-accreditation-2]].

### 2.7 Biomedical electronics

| Project | Difficulty | Key tools / parts | What it demonstrates |
|---|---|---|---|
| Portable ECG monitor with Bluetooth/Wi-Fi streaming | ★★ | AD8232, ESP32, electrodes | Biopotential acquisition, IoT [[iot-enabled-hemodynamic-surveillance-system-ad8232]] |
| Cardiac monitor with cloud alerts | ★★ | Arduino, heartbeat and temperature sensors | Real-time telemetry [[heart-disease-detection-by-using-machine-learning-algorithms-and-a-real-time-car]] |
| Heart-disease risk classifier (ML on open datasets) plus sensor prototype | ★★–★★★ | WEKA/Python, Arduino | Classification, sensitivity/specificity [[heart-disease-detection-by-using-machine-learning-algorithms-and-a-real-time-car]] |
| Remote patient-monitoring architecture with LSTM classification (simulation) | ★★★ | MATLAB, LSTM | Cloud analytics for health data [[remote-patient-monitoring-and-classifying-using-the-internet-of-things-platform]] |

A 2025 preprint builds an ECG and vital-signs monitor around the AD8232 front end and an ESP32, streaming to a Blynk dashboard with display and GSM alerts [[iot-enabled-hemodynamic-surveillance-system-ad8232]]. It pairs well with the LTspice ECG filter chain above [[eece-2510-circuits-and-signals-biomedical]]: simulate the analog front end, then build the digital back end. On the analytics side, an open-access 2018 study reports SVM as the best heart-disease classifier on open datasets (97.53% accuracy, 97.50% sensitivity, 94.94% specificity). The same study also builds an Arduino telemetry prototype [[heart-disease-detection-by-using-machine-learning-algorithms-and-a-real-time-car]]. Biomedical projects must be framed as prototypes: none of these devices is a certified medical instrument, and the report should say so. Doing so also scores under the ethics and safety factors NBA lists [[national-board-of-accreditation-2]].

## 3. Mini Projects vs Final-Year Major Projects

NBA assesses these as separate categories. The major (capstone) project has its own 25-point criterion, while seminars and mini/micro projects share a 10-point criterion, as do internships [[national-board-of-accreditation-2]]. The difference in expectation follows from that weighting.

| Dimension | Mini project (2nd–3rd year) | Final-year major project |
|---|---|---|
| Scope | One well-defined function or circuit | A system with several interacting modules |
| Duration | Weeks to one semester | Typically two semesters with staged reviews [[2014-batch-onwards]] |
| Evidence expected | Working demo plus short report | Proposal, mid-term, demo, report, external viva [[2014-batch-onwards]] |
| Typical examples | Active filter bank, FSM controller, FM receiver, smart-home relay control | RISC-V pipeline, buck converter with compensation, TinyML keyword spotter, ECG monitor with analytics, patch antenna designed and measured |
| Novelty bar | Reproducing a known design correctly | Extending, comparing or optimising a known design with measurements |

A good strategy is to make the mini project a stepping stone:

- **Analog:** an LTspice filter mini project becomes the analog front end of a final-year ECG system.
- **Digital:** an FSM mini project grows into a RISC-V core.
- **Communication:** an FM receiver becomes an ADALM-Pluto digital link.

Each final-year review then builds on work the student already understands.

## 4. Tools, Platforms, and Simulation Software

| Domain | Simulation / design | Hardware platforms |
|---|---|---|
| Analog | LTspice (AC sweep, transient, FFT) [[eece-2510-circuits-and-signals-biomedical]] | Breadboard, op-amps, ADALM2000 [[activity-active-filtering-analog-devices-wiki]] |
| Digital / VLSI | Verilog/VHDL, ModelSim testbenches [[design-and-simulate-risc-v-procesor-using-verilog]] | Basys 3, Lattice IceStick [[fpga-projects-fpga4studentcom]] [[readmemd]] |
| Embedded / IoT | Arduino IDE, Blynk cloud [[final-year-embedded-system-projects-2025-maven-silicon]] | Arduino, NodeMCU, ESP32, STM32, Raspberry Pi |
| Communication / SDR | GNU Radio Companion, Jupyter [[introductory-tutorial-for-sdr]] | RTL-SDR, HackRF, ADALM-Pluto, USRP [[best-sdr-for-gnu-radio-projects-student-to-research-setups]] |
| RF / antennas | CST Microwave Studio, HFSS [[2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024]] | LibreVNA, NanoVNA [[leveraging-inexpensive-lab-tools]] |
| Edge AI | Edge Impulse, TensorFlow Lite Micro [[edge-impulse-an-mlops-platform-for-tiny-machine-learning]] | ESP32, ESP32-S3, ESP32-CAM |
| Power | LTspice, TI design equations [[application-note-2]] | MOSFETs, controller ICs, Arduino for MPPT [[niu-journal-of-humanities]] |
| Biomedical | LTspice for front ends, WEKA/Python for ML [[heart-disease-detection-by-using-machine-learning-algorithms-and-a-real-time-car]] | AD8232, ESP32 [[iot-enabled-hemodynamic-surveillance-system-ad8232]] |

Simulation-first workflows cost little and generate the quantitative results examiners want. LTspice in particular covers analog, filter and switching-converter projects before any parts are bought [[eece-2510-circuits-and-signals-biomedical]] [[application-note-2]].

## 5. Trending Areas and Future-Proof Topics

- **Edge AI / TinyML.** Edge Impulse's authors cite forecasts of more than 5 billion edge-AI-chipset devices by 2025 [[edge-impulse-an-mlops-platform-for-tiny-machine-learning]]. Keyword spotting and anomaly detection on ESP32-class hardware are now practical undergraduate projects with published baselines [[deploying-real-time-speech-recognition-on-esp32-using-tinyml-and-edge-impulse-sp]].
- **Open hardware: RISC-V on FPGA.** Open, readable cores like FemtoRV [[readmemd]] and documented pipelined designs [[design-and-simulate-risc-v-procesor-using-verilog]] make processor design accessible, and it is relevant to semiconductor careers.
- **EV and battery electronics.** BMS projects are flagged as one of the most in-demand automotive-embedded types [[final-year-embedded-system-projects-2025-maven-silicon]], and buck-converter design underpins them [[application-note-2]].
- **Renewable energy.** MPPT solar charging [[niu-journal-of-humanities]] aligns directly with NBA's sustainability-goal criterion [[national-board-of-accreditation-2]].
- **5G and mmWave antennas.** 28 GHz patch designs are an active publication area [[2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024]], and low-cost VNAs now put antenna measurement within reach up to 6 GHz [[leveraging-inexpensive-lab-tools]].
- **SDR-based communication.** SDR scales from an FM receiver to 5G/O-RAN research, so one skill set spans mini and major projects [[best-sdr-for-gnu-radio-projects-student-to-research-setups]].
- **Connected health.** AD8232-plus-ESP32 systems combine analog front ends, IoT and analytics in one project [[iot-enabled-hemodynamic-surveillance-system-ad8232]] [[remote-patient-monitoring-and-classifying-using-the-internet-of-things-platform]].

A study of capstone projects in the Industry 4.0 era finds that the capstone's structure has barely changed in decades, with most change limited to the project topics rather than the process [[the-european-educational-researcher]]. The same study says industry wants attention to non-functional requirements (user experience, innovation) and methods such as Agile and Lean, which traditional capstones underweight [[the-european-educational-researcher]]. A trendy topic delivered with an old-fashioned process is therefore not automatically industry-relevant, because how the team plans, iterates and tests matters as much.

## 6. Executing and Documenting the Project

### Follow the standard project arc

Capstone projects generally move through theme selection, literature and market review, alternative designs, prototype, testing and analysis, conclusions, and final presentation [[the-european-educational-researcher]]. The GNDEC reviews map onto these stages: proposal (problem and feasibility), mid-term (modular design and planning), end-semester (working system), report, and guide assessment [[2014-batch-onwards]].

### Avoid the classic failure modes

A long-serving BYU capstone coach lists the recurring mistakes [[keep-the-big-picture-in-mind-the-byu-design-review]]:

- **Ignoring one requirement** because others seem more urgent, so the customer is disappointed.
- **Ordering parts too late** ("We forget to order parts early when they may take weeks to arrive").
- **Leaving no time for things to fail**, even though debugging unseen failures is part of the process.
- **Building only one prototype**, then having nothing to show after destructive testing, and not photographing it first.
- **Over-researching** trivial component choices.

The countermeasures from the same source [[keep-the-big-picture-in-mind-the-byu-design-review]]:

- Review requirements as a team monthly.
- Keep a year-long schedule plus a rolling few-week plan, updated weekly with explicit slack for failure.
- Time-box routine decisions.
- Write a prototype test plan with photo and video documentation.

### Make results measurable

A five-year study of a capstone course concluded that the course has curricular merit but fails as an outcomes-assessment tool, because findings tend to stay anecdotal rather than measurable [[the-capstone-design-course-and-its-failure-to-serve-as]]. For a student, the fix is simple: state quantitative targets at R1 and report measured values against them in the final report. Examples by project type:

| Project type | Quantitative targets to state and measure |
|---|---|
| Filters | Cutoff frequency, attenuation |
| Converters | Efficiency, ripple |
| TinyML | Accuracy, latency |
| Antennas | S11, gain |
| Processors | Pipeline CPI or maximum clock frequency |

### Report structure that scores

Given that the report is weighted equally with the end-semester demo [[2014-batch-onwards]], a strong report includes:

1. **Problem statement** and a survey of existing systems, with at least two or three published comparators.
2. **Specifications** with numeric targets.
3. **Design alternatives** considered and the reason for the chosen one.
4. **Simulation results** (LTspice, ModelSim, CST/HFSS, Edge Impulse) before hardware.
5. **Hardware implementation**, with photographs of each prototype iteration.
6. **Test results** against the specifications, including failures and fixes.
7. **A PO mapping**, covering sustainability, safety, ethics and cost as the NBA criteria expect [[national-board-of-accreditation-2]].
8. **Limitations and future work**, modelled on the RISC-V dissertation's explicit list of missing features [[design-and-simulate-risc-v-procesor-using-verilog]].
