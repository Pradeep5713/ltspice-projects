---
title: Leveraging Inexpensive Lab Tools
id: leveraging-inexpensive-lab-tools
tags:
- btech-ece-projects-259aee
- sdr
- rf-lab-curriculum
- vna
- mimo
created: '2026-09-25T03:20:18.247225Z'
updated: '2026-09-25T03:21:21.820099Z'
source: https://arxiv.org/pdf/2607.23911
source_domain: arxiv.org
fetched_at: '2026-09-25T03:20:18.246372Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'arXiv preprint (physics.ins-det, Jul 2026) by Gonzalez, Zajdel & Carley
  (Carnegie Mellon ECE) describing ''Board-Level RF Systems for the Internet-of-Things,''
  a 12-unit undergraduate/graduate course (18-427/18-727) built around six 2-hour
  lab exercises: (1) VNA/transmission-line network analysis using the open-source
  LibreVNA (100 kHz-6 GHz, 2-port FPGA-based VNA, chosen over the hobbyist NanoVNA
  which tops out at 1 GHz) sweeping 500 MHz-3 GHz; (2) patch antenna design/fabrication;
  (3) patch antenna characterization; (4) RF signal demodulation; (5) antenna array
  modeling/simulation; (6) live RF beam-steering demonstration. Total one-time equipment
  cost for the whole course is under ,000, and the paper reports Fall 2025 student
  survey data on reception of each lab; course materials and lab code are released
  in an open repository. Provides a concrete, costed curriculum blueprint for hands-on
  SDR/RF/MIMO/beam-steering teaching labs relevant to ECE capstone or lab-course design.'
raw_file: raw/leveraging-inexpensive-lab-tools.pdf
doi: arXiv:2607.23911
---

Leveraging Inexpensive Lab Tools
for Hands-on RF Systems Course
B. Joel Gonzalez, Tom J. Zajdel, L. Richard Carley
Department of Electrical and Computer Engineering, Carnegie Mellon University, Pittsburgh, PA, USA
Corresponding author: B. Joel Gonzalez (bgonzale@andrew.cmu.edu)
Abstract—As wireless technologies continue to develop and
reshape our world, teaching students the fundamental building
blocks of RF engineering is paramount. Relatively inexpensive
lab equipment now makes teaching concepts such as the Internet-
of-Things, beam steering, and MIMO accessible. A new course
for students in Electrical and Computer Engineering at Carnegie
Mellon University aims to utilize affordable hardware to teach
core concepts in RF systems design. This is accomplished through
six laboratory exercises, culminating in a live demonstration of
RF beam steering technology for students. The course can be
run for less than $9,000 in one-time costs and is well-received by
students as evidenced by survey data, with lab resources available
in an open repository.
Index Terms—education, laboratory, radio frequency, network
analyzers, transmission lines, antennas, software-defined radio,
beam steering, MIMO
I. INTRODUCTION
A. Motivation
Hands-on learning is a crucial experience for students
learning communications and RF engineering to students in
electrical engineering. In this era of the Internet-of-Things,
wireless sensor networks are growing in size, complexity,
and ubiquity. Lectures remain a core part of the curriculum
to share the theory and background necessary to work in
these fields. However, having students work directly with real
hardware presents them with an opportunity to learn skills
and concepts that will greatly benefit them in future research
and industry work [1] [2]. Unfortunately, the equipment and
tools required for students to learn and apply concepts in
RF engineering have historically been prohibitively expen-
sive. High-performance vector network analyzers (VNAs),
software-defined radios (SDRs), and related simulation soft-
ware tools can cost thousands of dollars each, which may
prohibit their use in an educational setting and limit the
number of students who can use these tools [3] [4]. This
course aims to take advantage of recent developments in RF
measurement hardware and software-defined radio that make
these tools much more affordable for universities and schools
to use in educational curricula.
Our course is titled “Board-Level RF Systems for the
Internet-of-Things”. The context for this course is the fu-
ture in which every device wants to communicate with the
world (i.e., the Internet-of-Things). It aims to teach students
how radios work at a systems level, and the relevant theory
Funded by the Department of Electrical and Computer Engineering at
Carnegie Mellon University.
about RF waves to understand signal interference, multipath
propagation, and other key aspects of RF communications
systems. This allows students to approach next-generation
technologies, namely massive MIMO (multiple input multi-
ple output) networks and their transformative potential, with
an understanding of their fundamental components [5]. The
following is a list of topics that students learn in the course
through lectures and labs:
• Basics of Electromagnetics and RF Waves
• RF Transmission Lines and Impedance Matching
• RF Analysis Tools (Vector Network Analyzers)
• RF Antennas (Monopoles, Dipoles, Patch, etc.)
• RF Transceiver Architectures
• Modulation Techniques (Analog, Digital)
• Information Theory and Digital Communications
• Software-Defined Radios (Point-to-Point)
• Multi-Input Multi-Output RF Antennas
• MIMO Theory and Communications
B. Course Design and Audience
The 12-unit course is offered to undergraduate students
(specifically third and fourth years) as 18-427 and graduate
students as 18-727 at Carnegie Mellon University. The course
is primarily taken by students in the ECE department. The
course requires prerequisite knowledge of circuits and signal
processing at the undergraduate level, in addition to basic
programming experience in Python or MATLAB. Beyond
these requirements, the course material should be approachable
to any student who seeks to expand their understanding of RF
hardware at the systems-level.
This paper provides an overview of the laboratory exercises
that students perform, along with a summary of the costs
to operate the course for a semester. We conclude with an
evaluation of the course via student survey data from the Fall
2025 semester, illustrating how students received each hands-
on laboratory exercise.
II. LABORATORY EXERCISES
This section will describe the laboratory exercises that
students complete, which are designed to complement lectures
and to provide them with direct access to RF hardware that
may otherwise be difficult to obtain and work with. Each
lab session is two hours long, which provides ample time
for students to complete the exercises using the equipment
in groups. Table I presents a summary of the lab exercises
arXiv:2607.23911v1  [physics.ins-det]  27 Jul 2026


---

that students complete in the course; these labs are available
in an online repository [6].
TABLE I
DESCRIPTION OF COURSE LAB EXERCISES.
Lab Exercise
Lab Description
Lab 1
RF network analysis of transmission lines
Lab 2
Design and fabrication of patch antennas
Lab 3
Characterization of patch antennas
Lab 4
Demodulation of RF signals
Lab 5
Modeling and simulation of antenna arrays
Lab 6
Demonstration of RF beam steering
A. Lab 1: VNAs & Transmission Lines
This lab uses a VNA to demonstrate RF network measure-
ment. Students are provided with a set of PCBs manufactured
by the course staff: A segment of microstrip line, a patch
antenna, and a T-line junction, as shown in Fig. 1. Students
use the LibreVNA to characterize these PCBs. The LibreVNA
is an open-source FGPA-based 2-port vector network ana-
lyzer that can characterize RF systems from 100 kHz to 6
GHz [7], shown in Fig. 2. In comparison to the inexpensive
NanoVNA popular with hobbyists which is limited to 1
GHz, the LibreVNA offers superior performance with a larger
operating frequency range relevant to IoT devices [8], which
is demonstrated as students sweep over frequencies ranging
from 500 MHz up to 3 GHz in the lab exercise. In lecture,
students learn the fundamentals of RF wave propagation and
transmission line theory, which they then visualize through
this lab as they take impedance measurements of each PCB.
Students are asked to observe the phenomena of a T-junction
splitter and to think critically about the impedance presented
by the junction. By working with these physical tools, students
gain a first-hand exposure to concepts such as reflections (i.e.
S-parameters) and impedance matching networks (i.e. quarter-
wave transformers).
Fig. 1. A set of a microstrip, patch antenna, and t-line junction PCBs.
B. Lab 2: Antenna Design & Simulation
This lab has students investigate the design and fabrication
of antennas using MATLAB’s Antenna Toolbox. This package
allows students to quickly and easily prototype, analyze, and
visualize antenna elements without needing to learn a specific
FEA design software [9]. Students gain experience using the
toolbox to design their own dipole and patch antennas, one of
which is shown in Fig. 3, to resonate at specific frequencies.
Primed by a lecture that describes the operation of patch
Fig. 2. The LibreVNA, an open-source vector network analyzer [7].
antennas, students iterate upon their designs in simulation until
they achieve an antenna that reaches the desired specification.
These antennas are then fabricated by the course staff to
be tested in the following lab. In past semesters, the course
staff used an LPKF S63 circuit board plotter (LPKF Laser
& Electronics, Tualatin, OR) to mill out the patch antennas
from a copper-clad FR4 substrate. Nowadays, instructors may
submit the PCB files for inexpensive fabrication through
an external vendor such as JLCPCB or PCBWay with fast
turnaround time.
Fig. 3. A patch antenna designed using MATLAB’s Antenna Toolbox.
C. Lab 3: Patch Antenna Characterization
This lab allows students to see the results of their efforts
from the previous lab as they test their patch antenna. Using
an anechoic chamber housed at Carnegie Mellon University,
students attach their patch antenna to a fixture that faces a
receive antenna. As Fig. 4 illustrates, both the device-under-
test (the patch antenna) and the receive antenna are connected
the LibreVNA. Students map out the azimuth radiation of
their antennas by providing an impulse signal to the transmit
antenna and measuring the resultant forward gain (S21). The
fixture that the antenna is attached to is motorized, allowing
for a Python script to automate the rotation and measurements
of the antenna. An anechoic chamber is not necessary for this
lab; it can be performed outdoors in a spacious environment
to minimize multipath propagation from reflections [10].
D. Lab 4: Software-Defined Radios
This lab presents a shift in the course from an emphasis on
RF network analysis and the physical layer toward a software-
defined approach to RF systems. Students learn about the
fundamental building blocks of radios through lecture, with an


---

Fig. 4. Antenna characterization setup diagram. The TX antenna is the device
under test (DUT), while the RX antenna is a horn antenna in the anechoic
chamber pointed towards the DUT. Alternatively, in an outdoors setting, the
RX antenna can also be a half-wavelength dipole antenna.
emphasis on the theory underpinning software-defined radios.
Then, through this lab, students gain experience programming
an SDR using GNU Radio, a free open-source GUI tool to
interface with SDRs. Students use an RTL-SDR (RTL-SDR
Blog, USA), shown in Fig. 5, which is an inexpensive receive-
only SDR that can receive signals up to 1.75 GHz [11]. This
lab exercise has students receive and demodulate live radio
signals from nearby broadcast FM stations. In addition, a
HackRF One (Great Scott Gadgets, Lakewood, CO), a low-
cost RX/TX SDR also shown in Fig. 5, broadcasts QPSK
signals in the classroom [12] so that students may demodulate
them with their SDR receivers using a Costas loop [13].
Subsequent analysis questions encourage students to think
about the mathematics underlying these modulation schemes.
Fig. 5. The RTL-SDR (top) and HackRF (bottom). Each student receives one
of the RTL-SDRs, which is used to receive and demodulate RF signals. The
HackRF is used to broadcast QPSK signals for students to demodulate.
E. Lab 5: Antenna Array Simulation
This lab revisits the MATLAB Antenna Toolbox to explore
antenna arrays, in anticipation of the final beam-steering lab
of the course. Students design and simulate dipole arrays
and patch antenna arrays, as shown in Fig. 6, to better
understand the directionality of these arrays. Drawing from a
mathematical derivation presented in lecture, students calculate
the necessary phase shifts to apply to each antenna element in
order to steer the beams in a particular direction. Through
this exercise, students gain an intuition for the underlying
mechanisms of beam steering, as well as further developing
their skills in using antenna simulation tools.
F. Lab 6: Beam Steering & LoRa
The final lab of the course is a live demonstration of
receive beam steering using the KrakenSDR (KrakenRF Inc,
Fig. 6. Antenna array simulation using MATLAB’s Antenna Array.
Chicago, IL), shown in Fig. 7. This radio system features
the same R820T2 chip as used on the RTL-SDR, but with
a synchronized clock to ensure that the system is temporally
coherent. Students are provided with LoRa Featherwing mi-
crocontrollers (Adafruit, Brooklyn, NY), also shown in Fig. 7,
and antennas which can transmit in the 433MHz or 915MHz
bands. By arranging the whip receive antennas in a linear array
and having students sit in a semi-circle facing the antenna
array, lab groups can take turns transmitting a LoRa signal
to the receive station. As Fig. 8 illustrates, the KrakenSDR
receives and processes the signal using the MUSIC algorithm
on a Raspberry Pi 4 [14], which then transmits the data to
a GUI that shows the direction-of-arrival of the signals [15].
Students can clearly see the lobes that they are generating
from their microcontroller’s signal. Analysis questions then
ask students to reflect upon the experimental setup, including
what improvements could be made to the experiment, and
how the various system components work. Through this lab,
students are well-equipped to set up and perform their own
experiments in wireless design and testing, pursuing their
curiosity with hands-on work.
Fig. 7. The KrakenSDR (left), a receive-only beam steering board, and the
LoRa Featherwing microcontroller (right) that students use to transmit to the
receive antenna array.
Fig. 8.
Diagram showing the direction-of-arrival of a LoRa signal in the
classroom.


---

TABLE II
LAB SURVEY DATA, SHOWING MEAN (SCALE OF 1 TO 7) AND STANDARD DEVIATION IN PARENTHESIS.
Question
Lab 1
(n=12)
Lab 2
(n=14)
Lab 3
(n=13)
Lab 4
(n=14)
Lab 5
(n=12)
Lab 6
(n=12)
This lab experience was interesting to me.
6.33 (0.78)
6.42 (0.67)
6.50 (0.67)
6.25 (0.97)
6.33 (0.89)
6.25 (0.87)
This lab was easy to complete.
5.58 (1.08)
5.25 (1.36)
6.08 (1.16)
5.83 (1.11)
6.08 (1.00)
6.66 (0.65)
This lab was valuable to me in
developing my understanding of what VNAs are used for.
6.08 (0.79)
This lab was useful in teaching me
the fundamental equations governing transmission line theory.
5.83 (1.03)
This lab was valuable in teaching me
how to design a variety of antennas.
6.00 (1.04)
This lab was useful in explaining
the process that goes into fabricating patch antennas.
5.83 (1.34)
This lab helped improved my understanding
of how an antenna is characterized.
6.42 (0.79)
This lab helped elucidate
the fundamental equations of antenna theory.
6.08 (1.38)
This lab helped me understand
how to use a software-defined radio.
5.92 (1.38)
This lab strengthened my understanding of
how demodulation works.
5.83 (1.64)
This lab helped me understand
how to simulate beam-steering phenomena.
6.25 (0.86)
This lab improved my understanding of
the equations that govern the physics of beam-steering.
6.08 (1.51)
This lab improved my understanding of
how a beam-steering SDR works.
6.33 (0.78)
This lab helped me understand
how I could set up my own beam-steering experiments in the future.
6.08 (1.16)
III. RESULTS
A. Assessment
To assess the quality of our course’s labs, students com-
pleted an anonymous feedback form. Students answered a
number of questions on a 7-point Likert scale, anchored
by Strongly Disagree (1) and Strongly Agree (7). Table II
shows the results of this survey for each Lab from the Fall
2025 academic semester. Additionally, to assess whether we
reached our educational objectives set at the beginning of
the course, students completed a survey before and after the
course asking a number of questions about RF systems and
wireless communications. This survey asked their self-efficacy
in explaining a number of concepts regarding RF systems and
wireless communications. Each response item asked students
to rate their ability on a scale of 1 to 10. Students completed
this survey at the beginning and end of the course, and these
results are illustrated in Fig. 9.
B. Cost
Table III summarizes the total cost of the course materials.
Considering a class size of 20 students with teams of 2,
the total one-time expenditure for course hardware is $8,838.
This sum excludes shipping costs, the cost of access to
MATLAB, and the recurring cost of PCB manufacturing. Note
that open-source software such as openEMS can be used to
substitute the use of MATLAB with Python to eliminate this
cost [16]. In comparison, to teach a course of this caliber,
similar VNA and SDR options often found in the fields of
wireless communications and RF engineering research can
cost over $2,000 per SDR and $10,000 per VNA, dramatically
increasing the cost of operating the course as the number
of students grows [17] [18]. Therefore, Table V presents a
most affordable means of teaching RF systems in a hands-on
manner.
3.7
8.6
4.9
9.3
4.1
9.4
4.2
9.3
3.2
9.3
4.1
8.9
Pre
Post
I can describe how MIMO is
useful for wireless networks.
I can describe how RF waves
propagate through different
materials and environments.
I can explain how 5G works to
a family member.
I can explain how each of the
building blocks of a radio
transceiver works.
I can explain the differences
between a digital modulation
scheme and an analog
modulation scheme.
I understand how antennas
work to transmit and receive
signals.
1
2
3
4
5
6
7
8
9
10
Fig. 9. Results from pre-course (n=10) and post-course (n=7) self-efficacy
surveys. Number by each point is the mean of responses across students.
Prompts for all questions started with “I am confident that...” All pre-post
response differences were significant as measured by unpaired t-test (p <0.001
for all questions).
TABLE III
ESTIMATE OF THE HARDWARE COST FOR THE COURSE,
ASSUMING 10 GROUPS OF STUDENTS.
Item
Cost
LibreVNA (x10)
$700 (x10)
HackRF
$350
RTL-SDR (x10)
$48 (x10)
LoRa Featherwing Microcontrollers and Antennas (x10)
$20 (x10)
Raspberry Pi 4
$110
KrakenSDR
$499
Kraken Antenna Array
$199
Total
$8,838


---

IV. DISCUSSION AND CONCLUSIONS
A course exploring the design and implementation of RF
systems is proposed, providing students with access to low-
cost equipment and tools to apply these concepts. The course
budget is less than $9,000. The lab exercises in the course
were positively received by students. Through the adoption
of low-cost and open-source electronics, RF engineering may
become more accessible to students of all backgrounds.
REFERENCES
[1] R. H. Caverly, “Use of low cost vector network analyzers in undergradu-
ate rf and wireless circuit laboratories,” in Middle Atlantic ASEE Section
Spring 2021 Conference, 2021.
[2] M. Carminati, “Soak your pcb: a design activity for hands-on learning
of the electrochemical interface impedance,” in 2023 IEEE International
Symposium on Circuits and Systems (ISCAS).
IEEE, 2023, pp. 1–5.
[3] D. Derickson, X. Jin, and C. C. Bland, “The nanovna vector network
analyzer: This new open-source electronic test and measurement device
will change both remote and in-person educational delivery of circuits,
electronics, radio frequency and communication laboratory course de-
livery,” in 2021 ASEE Pacific Southwest Conference-” Pushing Past
Pandemic Pedagogy: Learning from Disruption”, 2021.
[4] B. Pejcinovic, “Teaching high-frequency circuit design in online en-
vironment,” in 2021 44th International Convention on Information,
Communication and Electronic Technology (MIPRO), 2021, pp. 1559–
1564.
[5] E. G. Larsson, D. Danev, M. Olofsson, and S. Sorman, “Teaching
the principles of massive mimo: Exploring reciprocity-based multiuser
mimo beamforming using acoustic waves,” IEEE Signal Processing
Magazine, vol. 34, no. 1, pp. 40–47, 2017.
[6] J.
W.
B.
Joel
Gonzalez,
Tom.
J.
Zajdel,
“18-427-727
labs,”
2026,
last
accessed
26
July
2026.
[Online].
Available:
https:
//github.com/b-joel-gonzalez/18-427-727-Labs
[7] J. K¨aberich, “Librevna,” 2025, last accessed 13 July 2025. [Online].
Available: https://github.com/jankae/LibreVNA
[8] N. Hunt, J. Scott, and L. Streeter, “Nano versus commercial [educator’s
corner],” IEEE Microwave Magazine, vol. 24, no. 4, pp. 88–95, 2023.
[9] MathWorks, “Antenna toolbox,” 2025, last accessed 13 July 2025.
[Online]. Available: https://www.mathworks.com/products/antenna.html
[10] O. Safety and H. Administration, “Electromagnetic radiation: Field
memo,”
1990,
last
accessed
13
July
2025.
[Online].
Avail-
able:
https://www.osha.gov/radiofrequency-and-microwave-radiation/
electromagnetic-field-memo
[11] RTL-SDR, “About rtl-sdr,” 2025, last accessed 13 July 2025. [Online].
Available: https://www.rtl-sdr.com/about-rtl-sdr/
[12] G. S. Gadgets, “Hackrf one,” 2025, last accessed 13 July 2025.
[Online]. Available: https://greatscottgadgets.com/hackrf/one/
[13] J. P. Costas, “Synchronous communications,” Proceedings of the IRE,
vol. 44, no. 12, pp. 1713–1718, 1956.
[14] R. O. Schmidt, “Multiple emitter location and signal parameter estima-
tion,” IEEE Transactions on Antennas and Propagation, vol. 34, no. 3,
pp. 276–290, 1986.
[15] K. Inc, “What is krakensdr?” 2025, last accessed 13 July 2025.
[Online]. Available: https://www.krakenrf.com/about-krakensdr
[16] T. Liebig. openems - open electromagnetic field solver. General and
Theoretical Electrical Engineering (ATE), University of Duisburg-Essen.
[Online]. Available: https://www.openEMS.de
[17] E. Research, “Usrp b210,” 2025, last accessed 21 August 2025.
[Online]. Available: https://www.ettus.com/all-products/ub210-kit/
[18] C.
M.
Technologies,
“V0902
2-port
9
ghz
vec-
tor
network
analyzer,”
2025,
last
accessed
21
August
2025.
[Online].
Available:
https://coppermountaintech.com/vna/
2-port-9-ghz-vector-network-analyzer-v0902/
