---
title: FPGA Implementation of SIMON-128
id: fpga-implementation-of-simon-128
tags:
- fpga-verilog-publishable-project-e0cabb
created: '2026-09-25T03:34:24.806641Z'
source: https://arxiv.org/pdf/2301.01889
source_domain: arxiv.org
fetched_at: '2026-09-25T03:34:24.805750Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
raw_file: raw/fpga-implementation-of-simon-128.pdf
doi: arXiv:2301.01889
---

FPGA Implementation of SIMON-128
Cryptographic Algorithm Using Artix-7
Ridha Ghayoula1,2, Jaouhar Fattahi3, Amor Smida4, Issam El Gmati5, Emil Pricop6 and Marwa Ziadia3
1Unit of Research in High Frequency Electronic Circuits and Systems, University of Tunis El Manar- 2092, Tunis, Tunisia.
2Department of Electrical and Computer Engineering, Laval University, Quebec, Canada.
3Department of Computer Science and Software Engineering, Laval University, Quebec, Canada.
4Department of Medical Equipment Technology, College of Applied Medical Sciences, Majmaah University,
Majmaah, 11952, KSA.
5College of Engineering at al Gunfudha Umm Al Qura University, KSA.
6Automatic Control, Computers and Electronics Department. Petroleum-Gas University of Ploiesti, Romania.
Abstract—FPGA is a hardware architecture based on a matrix
of programmable and conﬁgurable logic circuits thanks to which
a large number of functionalities inside the device can be modiﬁed
using a hardware description language. These functionalities
must often be secured especially when the context is sensitive
(military, banking, medical, legal, etc.). In this paper, we put
forward an efﬁcient implementation of SIMON’s block cipher
algorithm using Xilinx Vivado 2018.2. The proposed design is
analyzed through simulation on Xilinx Artix-7. A prototype of
our design is implemented using the xc7a35tcsg324-1 FPGA chip.
Performance and results are discussed.
Index Terms—Artix-7, SIMON-128, FPGA, Security, Cryptog-
raphy.
I. INTRODUCTION
Cryptography [1] has been used for thousands of years.
Nowadays, it is more and more present in our daily life.
Contemporary cryptography is mainly interested in, but not
limited to, the six following properties:
1) Secrecy (or conﬁdentiality): the property that ensures
that secret or sensitive information is not discovered by
an unauthorized party;
2) Authentication: the property that ensures that a stake-
holder or service requester is who they claim to be, by
presenting something they have, something they are, or
something they know.
3) Integrity: the property that ensures that the information
has not been modiﬁed in a malicious, accidental, or
intentional way by a third party;
4) Authenticity: authentication and integrity usually results
in authenticity, which is the guarantee that the informa-
tion is authentic and comes really from its purported
source as it is sent;
5) Non-repudiation: the property that ensures that a stake-
holder cannot deny his action, or his partial participation
in an action. This results in the fact that one can always
establish irrefutable proof of an stakeholder’s action;
6) Availability [2]: the property that ensures that the infor-
mation or service has not ceased to exist in a malicious
way.
The ability to keep an encrypted message secret is based
not on the encryption algorithm but on a secret piece of
information called a key that must be used with the algorithm
to produce the encrypted message. The size of the key,
expressed in number of bits, is a key element and plays a
crucial role in the security of the cryptographic algorithm.
Depending on whether the key used for encryption and
decryption is the same or not, we speak of a symmetric or
asymmetric cryptographic system. Symmetric cryptography,
also known as secret key cryptography, uses a unique key
to encrypt and decrypt data. This key must be shared with
the recipient. The advantage of symmetric cryptography is
that it is easy to implement. Its disadvantage is that the
secret key must be shared with the recipient, which adds a
key management burden. Unlike symmetric cryptography,
asymmetric cryptography requires two keys for its operation:
ﬁrst, a so-called public key that must be made public to
recipients; second, a private key that must be kept secret.
The public key and the private key are two totally different
things, nevertheless, they are linked by mathematical bonds.
The advantage of asymmetric cryptography is that one does
not manage the security of key sharing, but its disadvantage
is that it takes a lot of time. Also, encrypted messages are
much larger than those encrypted using symmetric keys.
Cryptographic protocols, using symmetric or asymmetric
cryptographic algorithms, [3], [4], [5], [6] are rules of
exchange between network points whose role is precisely
to secure communications. They are used for example in
e-commerce, when a customer enters his credit card number
to pay for a purchase. But they are also used in a multitude of
other situations, such as when connecting to a computer in a
secure manner, when sending e-mails if one wishes to prevent
an eavesdropper from reading them, or when checking one’s
bank account balance. They are used for any use of the bank
card, such as withdrawing money from an ATM or paying
in a restaurant. They have also been used for a long time
in the decoders of pay TV channels to allow the customer
to have access to the channels to which he has subscribed
and to prevent him from accessing other channels, while
arXiv:2301.01889v1  [cs.CR]  5 Jan 2023


---

allowing possible changes in the subscription. Nowadays,
it is possible to implement a cryptographic algorithm in a
software or hardware way. The hardware implementation of
a cryprographic algorithm consists of the use of computer
hardware (e.g. processors, dedicated chips, etc.) in the data
encryption process. In general, this implementation is put
integrated in the instruction set of the processor, which means
that a part of the processor is dedicated to the cryptographic
mission. This also means that a signiﬁcant increase in speed
will be observed. By the same stream of ideas, parallel
architectures of modern processors are capable of executing
other instructions at the same time. A secure cryptoprocessor
is a processor optimized for cryptographic tasks (modular
exponentiation,
DES
encryption,
etc.)
incorporated
with
multiple physical security measures, giving it some resistance
to tampering. It can be realized in various ways depending
on the proﬁle of the use: FPGA, ASIC or microcontroller.
The reconﬁguration capabilities of FPGAs allow considerable
optimization of operations and correction of implementations
if necessary. Some encryption algorithms are less suitable
than others for modern hardware. DES, for example, is based
on permutations between bits, which may not be suitable for
some types of hardware.
In this paper, we propose a hardware implementation of the
SIMON-128 cryptographic algorithm[7], [8], [9], [10]. The
architecture we are putting forward is designed using Xilinx
Vivado 2018.2. It is implemented on the xc7a35tcsg324-1
Artix-7 FPGA board. Artix-7[11], [12] is a development
platform designed around the Xilinx in-situ programmable
gate array. It is designed entirely for use as a MicroBlaze
softcore processor system. The Artix-7 FPGA is optimized
for high-performance logic and offers better performance as
well as more capacity than old designs.
The methodology including the SIOMON algorithm de-
scription is presented in section II. Design, synthesis, imple-
mentation, and experimental results are presented in section
III. Discussion is made in section IV. Finally, section V makes
conclusions.
II. METHODOLOGY
The algorithm we implement in this paper is the SIMON
encryption algorithm. It was proposed by researchers in cryp-
tography at the NSA. One of SIMON’s security goals was
to keep a reasonable level of security in an environment
where power, memory and processors are severely limited.
The detailed description of the algorithm is freely available
on the web. SIMON is a symmetric block cipher algorithm.
The computation scheme used is a Feistel network[13], [14].
Feistel’s process 1 hinges on the idea that repeating judiciously
chosen simple operations enough times allows good security.
Encryption is a succession of similar steps (called rounds) each
using a subkey. This process is characterized by:
1) An iterative and modular construction;
2) Subkeys are derived from the secret key;
3) The functions used by a lathe must be optimized and
are generally simple operations.
These simple operations are generally:
1) Permutation: the symbols of the plain text are exchanged
between them. Permutation adds diffusion;
2) Substitution: a symbol is replaced by another symbol.
Substitution adds confusion.
Figure 1.
Feistel round.
The encryption is decomposed into several rounds. In each
round, two blocks are exchanged and one block is combined
with a transformed version of the second block and a key.
The transformation function is a non-linear bijection while the
combination function is usually the exclusive function (XOR).
The rotating key is generated from an initial secret key. The
key generation mechanism is usually called a key program.
This scheme thus provides the two properties of diffusion and
confusion necessary in an encryption algorithm. SIMON is
an algorithm intended to be physically implemented in highly
constrained embedded systems. For this the following design
choices have been made [15], [16], [17]:
• The size of the block and the key are conﬁgurable;
• The number of laps required for encryption then varies;
• The nonlinear function used at each turn is very simple;
• The complexity of decryption grows exponentially with
the number of rounds.
SIMON respects the symmetry operation regarding the
circular shift operation on n-bit words. The key schedule uses
a succession of 1-bit round constants devised for the sliding
properties and circular shift symmetry.
Table I sums up all conﬁgurations of SIMON-128.
Let Sj denote a j-bit-left circular shift. The key schedule
is mathematically described as:
The key schedule structure can be either balanced or
unbalanced. The number of keywords m is used to establish
the key expansion structure, yielding a total bit width of


---

TABLE I
SIMON-128 PARAMETERS
Bloc size (bits)
key size
key word (m)
Round constant
Rounds
124
2
z2
68
128
192
3
z3
69
256
4
z4
72









c ⊕zji ⊕ki ⊕ i ⊕S−1 S−3Ki+1

, with m = 2
c ⊕zji ⊕ki ⊕ i ⊕S−1 S−3Ki+2

, with m = 3
c ⊕zji ⊕ki ⊕ i ⊕S−1 S−3Ki+3 ⊕Ki+1

, with m = 4
m ∗n. The keyword expansion consists of a right shift, an
XOR and a constant sequence, zx. The zx bit operates on the
lowest bit of the keyword once every round [18], [19].
The SIMON-128 encryption is expressed by Equation 1:
R (l, r, k) =
  S1 (l) &S8 (l)

⊕S2 (l) ⊕r ⊕k, l

(1)
The SIMON-128 decryption is expressed by Equation 2:
R−1 (l, r, k) =
 r,
 S1 (r) &S8 (r)

⊕S2 (r) ⊕l ⊕k

(2)
Where l is the left-most word of a block, r the right-most
word and k the corresponding round key [20].
III. IMPLEMENTATION AND EXPERIMENTAL RESULTS
We assume that the block of data to be encrypted as well
as the key are presented at the same time. A pulse of the
”start” signal indicates that the encryption can start. Once the
encryption is ﬁnished, the ”done” signal goes to one indicating
that the value presented on the output ”ciphertext” is valid. In
addition to these signals, we also have an input for the clock
signal ”clk” and reset ”nrst”. The module is divided into three
parts:
• SIMONdp: for encrypting data blocks;
• SIMONks: for generating the turn key;
• SIMONctrl: for generating control signals.
The architecture of the SIMON cipher block consists of a
parallel cipher that uses round functions and key generation
blocks.
The SIMON-128 architecture is implemented on a Xilinx
Arty board which is a Artix-7 Pro-based embedded develop-
ment platform. The xc7a35tcsg324−1 FPGA contains 20800
LUT, 4600 Flip Flip and 9600 LUTRAM modules. We used
Xilinx Vivado 2018.2 Softwares to implement our architecture
on the board. All VHDL modules are extensively simulated
Figure 2.
SIMON Design.
using Vivado 2018.2 and synthesized using Xilinx synthesis
technologies. Figure 3 shows the experimental setup for the
SIMON-128 architecture. Table II presents the implementation
resources (Post-synthesis and post-implementation).
Figure 3.
SIMON-Code application using Artix-7.
Summary of on-Chip static and dynamic power are shown
in Table III using xc7a35tcsg324 −1 device of Artix-7
family. Table III and Table IV present the thermal and power
characteristics of this implementation.
IV. DISCUSSION
Table V gives the performance of our implementation and
compares it with the results obtained with Zynq-7000 and
Virtex-7 presented in [21]. Our implementation presents sig-
niﬁcant improvement over both of them regarding all metrics.


---

Figure 4.
SIMON-128 XDC ﬁle.
TABLE II
IMPLEMENTATION RESOURCES (POST-SYNTHESIS AND
POST-IMPLEMENTATION)
Resource
Utilization
Available
Utilization (%)
LUT
45
20800
0.22
LUTRAM
12
9600
0.13
FF
27
4600
0.06
IO
5
210
2.38
BUFG
1
32
3.13
TABLE III
ON-CHIP DYNAMIC AND STATIC POWER
Dynamic
Static
Power (W)
Percentage
Power (W)
Percentage
Signals
< 0.001
10%
Logic
< 0.001
13%
PL Static
0.070
97%
I/O
0.001
46%
Clocks
0.001
31%
TABLE IV
THERMAL AND POWER CHARACTERISTICS
Power
Total On-Chip Power
0.072 w
Junction Temperature
25.3◦
Thermal margin
59.7◦(12.) w
Effective JA
4.8◦c/w
Power Supplied to off-hip devices
0 w
Conﬁdence level
Medium
We note a gain in power consumption of 69.87% compared to
Zynq-7000 and 70.56% compared to Virtex-7, a gain in delay
of 26.69% compared to Zynq-7000 and 8.95% compared to
Virtex-7. SIMON Artix-7 also uses less area of lookup table
(e.g. 45 LUT) compared to both Zynq-7000 and Virtex-7 (73
LUT). Artix-7 conﬁrms its reputation of being quicker and
low-cost than other models.
Other
recent
work
comparable
to
our
present
implementation is worthy of mention. For instance, Rashidi in
TABLE V
PERFORMANCE AND COMPARISON OF OUR IMPLEMENTATION WITH
ZYNQ-7000 AND SIMON VIRTEX-7
Metric
SIMON Zynq-7000
[21]
SIMON Virtex-7
[21]
SIMON Artix-7
Power (mW)
239
248
72
Delay (ns)
5.448
4.415
4.020
Area (LUT)
73
73
45
[22] presented an ASIC implementation of several sizes of the
SIMON algorithm using Sklansky adder. Encouraging results
were observed regarding critical path delay. In the same vein,
Sheikhpour et al. in [23] presented a ﬂexible implementation
of SIOMON with various key sizes, which has capabilities
for various kinds of attacks. In [24], Abed et al. presented
several types of SIMON implementations (pipelined, scalar,
etc.) and showed a comparison between these families in
terms of throughput and drew up an implementation guideline
depending on the technological need.
Despite the good performance of our implementation, it
requires very sharp knowledge of the hardware and tools and
the design is sometimes tedious to set up.
V. CONCLUSION
In this paper, we have presented an implementation of
SIMON-128 algorithm using Artix-7of with low-cost FPGA
platform. The Feistel feature of SIMON is chosen to reduce
the hardware impact of encryption without sacriﬁcing software
performance. Such a structure has the advantage that the
encryption and decryption operations are very similar, which
is enough to reverse the operation of the key manager to obtain
the decryption operation. We used circular offsets (just hard-
ware cabling) and bit-to-bit operations. The implementation
led to a good performance that we discussed in this paper
compared to other implementations in the state of the art.


---

REFERENCES
[1] H. C. v. Tilborg, Encyclopedia of Cryptography and Security.
Berlin,
Heidelberg: Springer-Verlag, 2005.
[2] E. Pricop, S. F. Mihalache, N. Paraschiv, J. Fattahi, and F. Zamﬁr, “Con-
siderations regarding security issues impact on systems availability,”
in 2016 8th International Conference on Electronics, Computers and
Artiﬁcial Intelligence (ECAI), 2016, pp. 1–6.
[3] J. Fattahi, “Analyse des protocoles cryptographiques par les fonctions
t´emoins,” Ph.D. dissertation, Laval University, Quebec, Canada, 2 2016.
[4] J. Fattahi, M. Mejri, M. Ziadia, E. Ghayoula, O. Samoud, and
E. Pricop, “Cryptographic protocol for multipart missions involving
two
independent
and
distributed
decision
levels
in
a
military
context,”
in
2017
IEEE
International
Conference
on
Systems,
Man, and Cybernetics, SMC 2017, Banff, AB, Canada, October
5-8,
2017.
IEEE,
2017,
pp.
1127–1132.
[Online].
Available:
https://doi.org/10.1109/SMC.2017.8122763
[5] J. Fattahi, M. Mejri, M. Ziadia, T. Omrani, and E. Pricop, “Witness-
functions versus interpretation-functions for secrecy in cryptographic
protocols: What to choose?” in 2017 IEEE International Conference
on Systems, Man, and Cybernetics, SMC 2017, Banff, AB, Canada,
October 5-8, 2017.
IEEE, 2017, pp. 2649–2654. [Online]. Available:
https://doi.org/10.1109/SMC.2017.8123025
[6] J. Fattahi, M. Mejri, R. Ghayoula, and E. Pricop, “Formal reasoning
on authentication in security protocols,” in 2016 IEEE International
Conference on Systems, Man, and Cybernetics, SMC 2016, Budapest,
Hungary, October 9-12, 2016.
IEEE, 2016, pp. 282–289. [Online].
Available: https://doi.org/10.1109/SMC.2016.7844255
[7] A. S. Omar and O. Basir, “SIMON 32/64 and 64/128 block cipher:
Study of cross correlation and linear span attack immunity,” in
28th IEEE Annual International Symposium on Personal, Indoor, and
Mobile Radio Communications, PIMRC 2017, Montreal, QC, Canada,
October 8-13, 2017.
IEEE, 2017, pp. 1–6. [Online]. Available:
https://doi.org/10.1109/PIMRC.2017.8292209
[8] D. Le, S. L. Yeo, and K. Khoo, “Algebraic differential fault analysis
on SIMON block cipher,” IACR Cryptol. ePrint Arch., p. 436, 2021.
[Online]. Available: https://eprint.iacr.org/2021/436
[9] S. M. Dehnavi, “Further observations on SIMON and SPECK block
cipher families,” Cryptogr., vol. 3, no. 1, p. 1, 2019. [Online]. Available:
https://doi.org/10.3390/cryptography3010001
[10] R. Beaulieu, D. Shors, J. Smith, S. Treatman-Clark, B. Weeks, and
L. Wingers, “The SIMON and SPECK lightweight block ciphers,” in
Proceedings of the 52nd Annual Design Automation Conference, San
Francisco, CA, USA, June 7-11, 2015.
ACM, 2015, pp. 175:1–175:6.
[Online]. Available: https://doi.org/10.1145/2744769.2747946
[11] C. Fibich, M. Horauer, and R. Obermaisser, “Device- and temperature
dependency of systematic fault injection results in artix-7 and ice40
fpgas,” in Design, Automation & Test in Europe Conference &
Exhibition, DATE 2021, Grenoble, France, February 1-5, 2021.
IEEE,
2021, pp. 1600–1605. [Online]. Available: https://doi.org/10.23919/
DATE51398.2021.9474161
[12] J. Wang, C. Feng, W. Dong, Z. Shen, and S. Liu, “A high precision
time-to-digital converter based on multi-chain interpolation with a low
cost artix-7 FPGA,” in 7th International Conference on Event-Based
Control, Communication, and Signal Processing, EBCCSP 2021,
Krakow, Poland, June 22-25, 2021.
IEEE, 2021, pp. 1–5. [Online].
Available: https://doi.org/10.1109/EBCCSP53293.2021.9502368
[13] S. Chen, Y. Fan, L. Sun, Y. Fu, H. Zhou, Y. Li, M. Wang,
W. Wang, and C. Guo, “SAND: an AND-RX feistel lightweight
block cipher supporting s-box-based security evaluations,” Des. Codes
Cryptogr., vol. 90, no. 1, pp. 155–198, 2022. [Online]. Available:
https://doi.org/10.1007/s10623-021-00970-9
[14] C. Guo and G. Zhang, “Beyond-birthday security for permutation-based
feistel networks,” Des. Codes Cryptogr., vol. 89, no. 3, pp. 407–440,
2021. [Online]. Available: https://doi.org/10.1007/s10623-020-00820-0
[15] R. Beaulieu, D. Shors, J. Smith, S. Treatman-Clark, B. Weeks, and
L. Wingers, “The SIMON and SPECK families of lightweight block
ciphers,” IACR Cryptol. ePrint Arch., p. 404, 2013. [Online]. Available:
http://eprint.iacr.org/2013/404
[16] R. Beaulieu, D. Shors, J. Smith, S. Treatman-Clark, B. Weeks, and
L. Wingers, “The simon and speck lightweight block ciphers,” in
Proceedings of the 52nd Annual Design Automation Conference, ser.
DAC ’15. New York, NY, USA: Association for Computing Machinery,
2015. [Online]. Available: https://doi.org/10.1145/2744769.2747946
[17] L. M. A. Qassem, T. Stouraitis, E. Damiani, and I. M. Elfadel,
“Fpgaaas: A survey of infrastructures and systems,” IEEE Trans. Serv.
Comput., vol. 15, no. 2, pp. 1143–1156, 2022. [Online]. Available:
https://doi.org/10.1109/TSC.2020.2976012
[18] A.
Shahverdi,
M.
Taha,
and
T.
Eisenbarth,
“Lightweight
side
channel resistance: Threshold implementations of simon,” IEEE Trans.
Computers, vol. 66, no. 4, pp. 661–671, 2017. [Online]. Available:
https://doi.org/10.1109/TC.2016.2614504
[19] A. Aysu, E. Gulcan, and P. Schaumont, “SIMON says, break the area
records for symmetric key block ciphers on fpgas,” IACR Cryptol. ePrint
Arch., p. 237, 2014. [Online]. Available: http://eprint.iacr.org/2014/237
[20] R. Beaulieu, S. Treatman-Clark, D. Shors, B. Weeks, J. Smith, and
L. Wingers, “The simon and speck lightweight block ciphers,” in 2015
52nd ACM/EDAC/IEEE Design Automation Conference (DAC), 2015,
pp. 1–6.
[21] P. Ahir, M. Mozaffari-Kermani, and R. Azarderakhsh, “Lightweight
architectures
for
reliable
and
fault
detection
simon
and
speck
cryptographic algorithms on fpga,” ACM Trans. Embed. Comput.
Syst.,
vol.
16,
no.
4,
may
2017.
[Online].
Available:
https:
//doi.org/10.1145/3055514
[22] B. Rashidi, “High-throughput and ﬂexible ASIC implementations of
SIMON and SPECK lightweight block ciphers,” Int. J. Circuit Theory
Appl., vol. 47, no. 8, pp. 1254–1268, 2019. [Online]. Available:
https://doi.org/10.1002/cta.2645
[23] S.
Sheikhpour,
M.
H.
Sadi,
and
A.
Mahani,
“High-throughput
conﬁgurable SIMON architecture for ﬂexible security,” Microelectron.
J., vol. 113, p. 105085, 2021. [Online]. Available: https://doi.org/10.
1016/j.mejo.2021.105085
[24] S.
Abed,
R.
Jaffal,
B.
J.
Mohd,
and
M.
Alshayeji,
“FPGA
modeling and optimization of a SIMON lightweight block cipher,”
Sensors, vol. 19, no. 4, p. 913, 2019. [Online]. Available: https:
//doi.org/10.3390/s19040913
NOTICE
©2022 IEEE. Personal use of this material is permitted.
Permission from IEEE must be obtained for all other uses, in
any current or future media, including reprinting/republishing
this material for advertising or promotional purposes, creating
new collective works, for resale or redistribution to servers or
lists, or reuse of any copyrighted component of this work in
other works.
