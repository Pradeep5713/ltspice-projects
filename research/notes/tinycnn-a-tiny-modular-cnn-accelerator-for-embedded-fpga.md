---
title: 'TinyCNN: A Tiny Modular CNN Accelerator for Embedded FPGA'
id: tinycnn-a-tiny-modular-cnn-accelerator-for-embedded-fpga
tags:
- fpga-verilog-publishable-project-e0cabb
- cnn-accelerator
- zynq
created: '2026-09-25T03:34:32.072050Z'
updated: '2026-09-25T03:36:13.087357Z'
source: https://arxiv.org/pdf/1911.06777
source_domain: arxiv.org
fetched_at: '2026-09-25T03:34:32.071296Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Ali Jahanshahi (UC Riverside) arXiv preprint proposes TinyCNN, an automated
  framework (Python/Keras software backend + CHISEL hardware backend + Scala-based
  precision-adjustment backend) that generates modular, resource-aware CNN accelerator
  hardware for embedded FPGAs. Evaluated on a PYNQ board (Xilinx Zynq-7000 XC7Z020
  SoC + ARM Cortex-A9) using a small CNN (4 conv layers, 3x3 filters, 292,566 params)
  trained on grayscale CIFAR-10. Reports per-image comparison: software (32-bit float,
  ARM 650MHz) gets 65.54% accuracy at 42.54 ms/image; hardware shared-mode (16-bit
  fixed) gets 62.28% accuracy at 8.12 ms; hardware exclusive-mode (16-bit fixed) gets
  62.28% accuracy at 2.7 ms — i.e., up to 15.75x speedup with only ~3% accuracy loss
  versus floating-point software. Notes convolution units can run in ''shared'' (resource-saving)
  or ''exclusive'' (higher throughput) mode and memory (BRAM) is the binding resource
  constraint on embedded FPGAs. Good template for a B.Tech project on lightweight
  CNN/tiny accelerator design-space tooling with reproducible speedup/accuracy tradeoff
  tables.'
raw_file: raw/tinycnn-a-tiny-modular-cnn-accelerator-for-embedded-fpga.pdf
doi: arXiv:1911.06777
citation_count: 11
venue: arXiv.org
---

TinyCNN: A Tiny Modular CNN Accelerator for Embedded FPGA
Ali Jahanshahi
ajaha004@ucr.edu
University of California, Riverside
Abstract
In recent years, Convolutional Neural Network (CNN)
based methods have achieved great success in a large num-
ber of applications and have been among the most power-
ful and widely used techniques in computer vision. How-
ever, CNN-based methods are computational-intensive and
resource-consuming, and thus are hard to be integrated into
embedded systems such as smart phones, smart glasses, and
robots. FPGA is one of the most promising platforms for ac-
celerating CNN, but the limited on-chip memory size limit
the performance of FPGA accelerator for CNN.
In this paper, we propose a framework for designing
CNN accelerator on embedded FPGA for image classiﬁca-
tion. The proposed framework provides a tool for FPGA
resource-aware design space exploration of CNNs and au-
tomatically generates the hardware description of the CNN
to be programmed on a target FPGA. The framework con-
sists of three main backends; software, hardware gener-
ation, and simulation/precision adjustment. The software
backend serves as an API to the designer to design the CNN
and train it according to the hardware resources that are
available. Using the CNN model, hardware backend gen-
erates the necessary hardware components and integrates
them to generate the hardware description of the CNN. Fi-
naly, Simulation/precision adjustment backend adjusts the
inter-layer precision units to minimize the classiﬁcation er-
ror.
We used 16-bit ﬁxed-point data in a CNN accelerator
(FPGA) and compared it to the exactly similar software ver-
sion running on an ARM processor (32-bit ﬂoating point
data). We encounter about 3% accuracy loss in classiﬁca-
tion of the accelerated (FPGA) version. In return, we got
up to 15.75× speedup by classifying with the accelerated
version on the FPGA.
1. Introduction
The exponential growth of big data during the last decade
motivates for innovative methods to extract high semantic
information from raw sensor data such as videos, images
and speech sequences. Among the proposed methods, Con-
volutional Neural Networks (CNNs) have become the de-
facto standard by delivering near-human accuracy in many
applications related to machine vision. While CNNs have
been known to researchers for decades, they were popu-
larized after demonstrating high accuracy at the 2012 Ima-
geNet recognition challenge [1]. Subsequently, CNNs have
become the state-of-the-art for image classiﬁcation, detec-
tion, and localization tasks. Research in CNNs and other
areas of deep learning continues at a rapid pace, with hun-
dreds of new papers published each year introducing new
models and techniques.
The CNN’s high performance (at classiﬁcation, detec-
tion, and localization) comes at the price of a large com-
putational cost as they require tens of GOP/s to classify a
single frame. Thus, one challenge to the widespread de-
ployment of CNNs is their signiﬁcant demands for com-
putation and storage capacity. Therefore, dedicated hard-
ware is required to accelerate their execution.
Graphics
Processing Units (GPUs), are the most widely used plat-
form to implement CNNs as they offer the best performance
in terms of pure computational throughput, reaching up to
11 TFLOP/s. Nevertheless, in terms of power consump-
tion, Field-Programmable Gate Array (FPGA) solutions are
known to be more energy efﬁcient (vs GPUs). Recent work
by Microsoft has even explored cost-effective acceleration
of deep learning on FPGAs at datacenter scale [2,3]. There
are also efforts in the academic community on FPGA-based
CNN accelerators [4,5] as well as tools for generating them
automatically [6,7].
We observe two trends which may help overcome im-
plementing CNN on FPGAs. The ﬁrst is a series of recent
papers in the machine learning community regarding very-
low-precision CNNs. Networks with binary weights [8], or
binary weights and activations [9, 10] have in certain cases
demonstrated accuracy comparable to full precision nets.
Such binarized neural net-works (BNNs) may be the key
to efﬁcient deep learning on FPGA. Binarization reduces
storage and memory bandwidth requirements, and replace
FP operations with binary operations which can be very ef-
ﬁciently performed on the LUT-based FPGA fabric. Con-
1
arXiv:1911.06777v1  [cs.LG]  15 Nov 2019


---

cerning the cost and effort of FPGA implementation,we see
a steady improvement in FPGA design automation tools
over the past decade.
High-level synthesis (HLS) tools
such as Xilinx Vivado HLS [11] and LegUp [12] enable a
user to write code in a high-level programming language,
then algorithmically compile that code down to a register-
transfer level (RTL) design speciﬁcation. More recent tools
such as Intel FPGA SDK for OpenCL [13] and Xilinx SD-
SoC [14] offer further automation features for generating
the hardware-software interface and on-chip memory net-
work. In the context of deep learning, these tools have the
potential to critically reduce time-to-market on new acceler-
ator designs and thus reduce the aforementioned innovation
gap.
In this project, we aim to design and implement a CNN
accelerator on an embedded FPGA for image classiﬁcation.
We use [15] as our reference that presents the design of a
BNN accelerator for FPGAs. In contrast to our reference, in
this work, the aim is to provide designers a general frame-
work to enable them design their CNN easily and use it as an
accelerator on an FPGA. Thus, we do not use BNN-based
CNN in this project.
In addition to generality of the framework, we also target
embedded systems that have hardware resource limitation.
Compressing the CNN model is a good choice to address
the resource limitations of the hardware. A straight forward
way to compress a network is to reduce the bit-width for
computing. This utilizes the ﬂexibility of FPGA or ASIC
design compared with GPU or CPU. It is proved to be an
effective way to use 16-bits ﬁxed-point operations in [16]
with small loss in accuracy. In our framework, we use 16-
bits operation and we show that the accuracy loss is very
small.
This work proposes a general framework for design and
implementation of tiny modular CNN accelerators on em-
bedded FPGAs.
Our framework automatically generates
the hardware code for the designed CNN and trained with
the provided software backend.
The framework consists
of three main components that correspond to our contribu-
tions. They are as follows:
• Software backend: Using Python, we provide a tool
for designing and training a CNN architecture. The
model (weights) of the trained network and other
CNN architecture parameters are used in the hardware
framework to generate the hardware description lan-
guage of the CNN, which is going to be implemented
on the FPGA. This back-end also provides the in-
formation needed for Simulation/precision adjustment
backend as well as checking the hardware resources
for the designed CNN model.
• Hardware backend: Using CHISEL [17], we perform
automatic generation and integration of different hard-
ware components needed for the CNN architecture de-
signed in the software backend. The CNN model is
passed to this back-end to be used in HDL generation
of the CNN. The output of this backend is the HDL
code that is ready to be synthesized and programmed
on an FPGA.
• Simulation/precision adjustment backend: Using
Scala testing libraries and the data passed to this back-
end, inter-layer precision of the generated CNN hard-
ware will be adjusted. The CNN output error intro-
duced by varying integer and fractional part of each
layer’s data is minimized by this backend.
The rest of this paper is organized as follows; we ﬁrst de-
scribe the framework overall structure, then we go in de-
tails for each component of the framework. Finally, we pro-
vide the results discussing different aspects of the generated
CNN for our target FPGA.
2. Tiny CNN
CNN is a machine learning classiﬁer that typically takes
in an image and produces the probabilities of that image
belonging to each output class. A typical CNN consists of
a pipeline of connected layers. Each layer takes as input
a set of feature maps (fmaps), performs some computation
on them, and produces a new set of fmaps to be fed into
the next layer. The input fmaps of the ﬁrst layer is the in-
put image. Layers may require conﬁguration values known
as parameters, which must ﬁrst be determined by training
the CNN ofﬂine on pre-classiﬁed data. Once the parame-
ters are ﬁnalized, the CNN can be deployed for inference
the classiﬁcation of new data points. For most practical ma-
chine learning applications, the ﬁrst-class concerns are the
accuracy and execution time of online classiﬁcation. This
project will thus focus on accelerating the inference task
without compromising accuracy. The aim of this project is
to provide a framework that automates implementation of
CNNs on an embedded FPGA for image classiﬁcation. Fig-
ure 1 shows the framework we proposed for this purpose. In
the following subsections, we are going to elaborate more
on each component of our framework.
2.1. Software backend
The software backend is an API by which users are capa-
ble of designing their CNN in the software level. The user
can tune their CNN with the train and test data sets, and
ﬁnally, export their model for further processings. We used
Keras library as the underlying deep learning framework of
the software backend. Keras is a high-level neural networks
API, written in Python and capable of running on top of
TensorFlow, CNTK, or Theano. It was developed with a
focus on enabling fast experimentation. We address three
challenges of designing a CNN by Software backend:
2


---

Figure 1: Tiny CNN framework.
CNN designing, training, and model generation: In our
framework, using Keras API, we provide a template Python
class to the designers to design their CNN. Then, the de-
signer’s CNN is trained and the model is saved in order to
be used by the hardware backend. Essentially, the model is
the CNN weights that are going to be used as initial values
of ROMs.
Veriﬁcation data: The software backend also inputs some
random data from test dataset to CNN and captures the out-
put of all layers of CNN with respect to that input. The
collected dataset is called veriﬁcation data and is used in
hardware backend for precision adjustment and veriﬁcation
purposes.
Hardware resource check: As mentioned before, we are
targeting embedded FPGA in this work. Thus, we want to
squeez the whole CNN model in FPGA BRAMs. Thus,
one step for designing the CNN would be checking if the
CNN model (weights) ﬁt in FPGA BRAMs. Software back-
end uses the target FPGA spec to check if the model ﬁts in
FPGA or not. In case the model does not ﬁt on the tar-
get FPGA, the software backend throws an exception that
shows not enough space for the model. In such cases, the
designer should play around the CNN hyper parameters and
make it smaller to ﬁt on the FPGA. Fully-connected layers,
due to their high number of parameters contributes to the
most of the memory (BRAM) usage.
2.2. Hardware backend
Hardware backend generates the hardware of the CNN
which is designed in the software backend according to
the inputs that are provided to this backend. We imple-
mented all basic hardware components that are needed for
CNNs. The developed hardware components are modular
and highly conﬁgurable. They can be conﬁgured based on
the CNN speciﬁcations including: data bit-width, shared or
exclusive components, and number of DSPs available for
components. All of the implemented hardware components
are modular that means we can simply attach them together
with few lines of code just like we do in designing CNNs in
software.
2.2.1
Convolution unit
This unit is the most critical component of the accelera-
tor, as it will take up the vast majority of the runtime. The
unit must maintain high throughput and resource efﬁciency.
Convolution operation has multiplication and addition in its
core. Since multiplication is a very expensive operation,
we used the built-in DSPs on FPGA board that are spe-
cialized for digital signal processing purposing – mainly in-
clude multiplication and addition.
The challenge with using the FPGA DSPs is that there
are a limited number of them on every FPGA board. The
implemented Convolution unit hardware is conﬁgurable in
such a way that the designer determines the number of DSPs
for this layer, and the hardware generator framework gener-
ates the convolver state machine in a way that it uses only
the speciﬁed number of DSPs. Apparently, the more DSPs
we allot to this hardware unit, the more throughput we get.
The maximum number of DSPs is the input image pixels,
and the minimum is one.
Since we are targeting embedded systems, in our frame-
work, this unit can be used by the designer of the CNN in
two modes:
• Shared mode: in the this mode, the convolution unit
is shared among all layers of CNN. Sharing this units
results in using less hardware resources of the FPGA,
but it introduces throughput degradation. If this mode
is chosen by the designer, a wrapper is generated au-
tomatically by the hardware generator backend. The
wrapper acts as a resource manager for this unit by ar-
bitrating different layers requesting to use convolution
unit.
• Exclusive mode: in the exclusive mode, for each con-
volution layer in the CNN a convolution unit hardware
is generated, which results in higher throughput and
FPGA resource usage.
3


---

Figure 2: FeedForward unit architecture.
2.2.2
FeedForward unit
The input to convolution unit hardware is three lines of the
input fmap and the ﬁlter that is going to be applied on the
fmaps. Also, the output of the convolution unit hardware is
one line that its size equal to the input fmap size and it goes
through activation, max pooling, and precision adjustment
layer to get to the next layer. Such inter-layer data should
be handled and stored in a hardware unit.
FeedForward unit is responsible for handling accumula-
tion of the input fmaps in an inter-layer RAM by a state ma-
chine (SM), and output them to the convolution unit three
line at a time in conjunction with the ﬁlter that should be
applied to the fmap. Figure 2 shows the structure of this
hardware unit.
As it is shown in Figure 2, one state machine (SM) is
responsible for buffering the feature maps (fmap) that are
input to this layer. This state machine is generated for each
layer according to the size and number of fmaps that are
inputted to the layer. On the output side, another state ma-
chine is responsible for feeding three lines of fmaps to the
convolution unit as well as the ﬁlter that is going to applied
to that. The state machine is also generated speciﬁc to the
layer. Also, the RAM and ROM in Figure 2 are generated
according to the fmaps that are going to buffered in this
layer and number of that layer ﬁlters. ROMs are initialized
with the CNN model (weights) provided by the Software
backend.
2.2.3
Activation and Max pooling units
In our framework, we implemented a max pooling unit and
an activation hardware unit. The activation unit performs
a Rectiﬁed Linear ReLU function. The max pooling unit
is conﬁgurable and is generated to perform M × M max
pooling in which M is speciﬁed by the designer.
2.2.4
Inter-layer precision adjustment unit
As we mentioned before, we are using ﬁxed-point numbers
and operations in our framework. Using ﬁxed-point instead
of ﬂoating-point introduced error to the CNN. This error
propagates through the network and affects the ﬁnal results
adversely. Since the error propagated through the early lay-
ers has more negative effects on the output anf the range
of the data propagated through the network varies from one
layer to the other, we need to adjust the proportion of in-
teger part and fractional part at the end of each layer of
the network. For doing so, we inser an Inter-layer preci-
sion adjustment unit at the end of each layer. This unit is
responsible for adjusting the integer and fractional part of
the output data of each layer before propagating to the rest
of the network. The adjustment of this unit is done by the
Simulation/precision adjustment backend.
2.2.5
Dense or fully-connected (FC) unit
Dense or fully-connected is also implemented as a conﬁg-
urable hardware unit.
Since this unit mainly consists of
multiplication and addition, it needs DSP resources. In our
framework, the number of DSPs and the size of the FC unit
is adjustable according to the designer needs. The weights
for this layer are stored in ROMs. So, they are generated
based on the weights provided by Software backend and
used in the synthesis phase of the generate hardware.
2.3. Simulation and Precision Adjustment Backend
In order to adjust the ﬁxed-point precision of the CNN,
we need to propagate several test inputs to the CNN im-
plemented in the hardware. The test points are generated by
software backend based on the user’s input dataset for train-
ing the CNN. The data consists of the input to the CNN and
the output of all layers that are produced for that image. The
simulation backend uses Scala language testing libraries to
input the veriﬁcation data to the generated hardware. Then
all the data from the output of each layer of the generated
CNN hardware is collected, and the difference of the col-
lected data and the data provided by the software backend
are calculated. Then, this backend adjusts the bit-width of
the Inter-layer precision adjustment unit of each layer based
to minimize the error generated by each layer.
This sequence of propagating data, collecting data, cal-
culating error, and adjusting the precision units is performed
until the network merges to a minimum output error. At the
end, the Simulation and precision adjustment backend ad-
justs all integer and fractional parts of the layers based on
the veriﬁcation data that are provided by the Software back-
end.
3. Experimental Results
We evaluate our design on a PYNQ board [18] that is an
open-source project from Xilinx that makes it easy to design
embedded systems with Xilinx Zynq SoC. PYNQ uses a low-
cost Xilinx Zynq-7000 SoC containing an XC7Z020 FPGA
alongside an ARM Cortex-A9 embedded processor. On the
4


---

Table 1: The CNN architecture generated by the framework.
Layer type
Output size
Output fmaps
Param #
Conv
(32, 32)
32
320
Activation
(32, 32)
32
0
Max pool
(16, 16)
32
0
Conv
(16, 16)
64
18496
Activation
(16, 16)
64
0
Max pool
(8, 8)
64
0
Conv
(8, 8)
128
73856
Activation
(8, 8)
128
0
Max pool
(4, 4)
128
0
Conv
(4, 4)
128
147584
Activation
(4, 4)
128
0
Max pool
(2, 2)
128
0
Dense
(1, 100)
51300
Activation
(1, 100)
0
Dense
(1, 10)
1010
Activation
(1, 10)
0
Total
292,566
software side of PYQN, using the Python language and li-
braries, designers can exploit the beneﬁts of programmable
logic and microprocessors in Zynq to build more capable
and exciting embedded systems. We make use of Xilinx
SDSoC 2016.4 as the primary design tool, which leverages
Vivado HLS and Vivado to perform the actual synthesis and
programming the FPGA implementation. We used CIFAR-
10 dataset to train and test the CNN. We converted the im-
ages to grey to have one-channel input due to our a small
FPGA board.
Using the software backend we designed and trained a
CNN. Table 1 shows the architecture of the CNN we tar-
geted for classifying CIFAR-10 dataset. We used 3×3 ﬁlters
for convolutions. The reason behind choosing such a small
CNN is that we are targeting a small FPGA as our hardware
platform and any larger CNN would not pass the checking
resource limitation phase of the Software backend. Also,
we wanted to show the accuracy difference between the ac-
celerated version on FPGA and the software version.
In order to compare the software version and the ver-
sion implemented on FPGA, we classiﬁed CIFAR-10 test
dataset for both software model on ARM Cortex-A9 which
is the embedded processor of our FPGA and on the Tiny-
CNN accelerator with two modes. Table 2 shows the com-
parison averaged results per image.
SW is the Python-
based software classiﬁer ran on ARM processor of the board
(650MHz). HW-SM is the CNN accelerator generated in
shared mode (sharing one convolution unit among all lay-
ers), and HW-EM is the CNN accelerator generated in ex-
clusive mode (one convolution for each layer).
We see that the effect of using 16-bit ﬁxed-point data
Figure 3: Hardware resource utilization of the Table 1 CNN
implemented on FPGA.
Table 2: Software vs. TinyCNN accelerator.
version
Accuracy
(%)
Runtime
(ms)
Data type
SW
65.54
42.54
32-b ﬂoating
HW-SM
62.28
8.12
16-b ﬁxed
HW-EM
62.28
2.7
16-b ﬁxed
on the precision of the classiﬁcation is negligible. We can
also see that using exclusive convolution hardware units im-
proves the runtime by avoiding stalls due to access con-
tention for using convolution layer by different layers.
Figure 3 shows the resource usage of the CNN hardware
implemented in PYNQ board. As we expected, memory
(BRAM) is the hardware resource limitation that we en-
counter while implementing a CNN on an embedded FPGA.
In the software backend, the CNN architecture is designed
in such a way that it utilized the FPGA BRAM to the high-
est.
4. Conclusion
In this paper, we proposed a framework that enables the
designers to design a CNN accelerator for an embedded
FPGA fast. The framework provides a software API that
makes designers capable of exploring the CNN design space
considering the hardware resource limitations. Then, the
CNN hardware is generated and tuned to have a low accu-
racy loss by inter-layer precision adjustment. Our results
show that we can reach up to 15.75% speedup compared to
the software implementation with 16-bit ﬁxed-point data.
As future work, we are going to automate the software
CNN design space exploration part in the software backend
to make the CNN design even more easily. Since the only
supported activation function is ReLU, we are going to add
more activation units to the framework.
5


---

References
[1] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Im-
agenet classiﬁcation with deep convolutional neural
networks,” in Advances in neural information process-
ing systems, pp. 1097–1105, 2012.
[2] K. Ovtcharov, O. Ruwase, J.-Y. Kim, J. Fowers,
K. Strauss, and E. S. Chung, “Accelerating deep con-
volutional neural networks using specialized hard-
ware,” Microsoft Research Whitepaper, vol. 2, no. 11,
pp. 1–4, 2015.
[3] A. Jahanshahi, M. K. Taram, and N. Eskandari,
“Blokus duo game on fpga,” in The 17th CSI Interna-
tional Symposium on Computer Architecture & Digi-
tal Systems (CADS 2013), pp. 149–152, IEEE, 2013.
[4] C. Zhang, P. Li, G. Sun, Y. Guan, B. Xiao, and
J. Cong, “Optimizing fpga-based accelerator design
for deep convolutional neural networks,” in Proceed-
ings of the 2015 ACM/SIGDA International Sympo-
sium on Field-Programmable Gate Arrays, pp. 161–
170, ACM, 2015.
[5] J. Qiu, J. Wang, S. Yao, K. Guo, B. Li, E. Zhou, J. Yu,
T. Tang, N. Xu, S. Song, et al., “Going deeper with
embedded fpga platform for convolutional neural net-
work,” in Proceedings of the 2016 ACM/SIGDA In-
ternational Symposium on Field-Programmable Gate
Arrays, pp. 26–35, ACM, 2016.
[6] N. Suda, V. Chandra, G. Dasika, A. Mohanty, Y. Ma,
S. Vrudhula, J.-s. Seo, and Y. Cao, “Throughput-
optimized opencl-based fpga accelerator for large-
scale convolutional neural networks,” in Proceedings
of the 2016 ACM/SIGDA International Symposium on
Field-Programmable Gate Arrays, pp. 16–25, ACM,
2016.
[7] Y. Wang, J. Xu, Y. Han, H. Li, and X. Li, “Deepburn-
ing: automatic generation of fpga-based learning ac-
celerators for the neural network family,” in Proceed-
ings of the 53rd Annual Design Automation Confer-
ence, p. 110, ACM, 2016.
[8] M. Courbariaux, Y. Bengio, and J.-P. David, “Bina-
ryconnect: Training deep neural networks with binary
weights during propagations,” in Advances in neural
information processing systems, pp. 3123–3131, 2015.
[9] M. Courbariaux, I. Hubara, D. Soudry, R. El-Yaniv,
and Y. Bengio, “Binarized neural networks: Train-
ing deep neural networks with weights and ac-
tivations constrained to+ 1 or-1,” arXiv preprint
arXiv:1602.02830, 2016.
[10] M. Rastegari, V. Ordonez, J. Redmon, and A. Farhadi,
“Xnor-net: Imagenet classiﬁcation using binary con-
volutional neural networks,” in European Conference
on Computer Vision, pp. 525–542, Springer, 2016.
[11] J. Cong, B. Liu, S. Neuendorffer, J. Noguera, K. Vis-
sers, and Z. Zhang, “High-level synthesis for fpgas:
From prototyping to deployment,” IEEE Transactions
on Computer-Aided Design of Integrated Circuits and
Systems, vol. 30, no. 4, pp. 473–491, 2011.
[12] A. Canis, J. Choi, M. Aldham, V. Zhang, A. Kam-
moona, T. Czajkowski, S. D. Brown, and J. H. An-
derson, “Legup: An open-source high-level synthe-
sis tool for fpga-based processor/accelerator systems,”
ACM Transactions on Embedded Computing Systems
(TECS), vol. 13, no. 2, p. 24, 2013.
[13] T. S. Czajkowski, U. Aydonat, D. Denisenko, J. Free-
man, M. Kinsner, D. Neto, J. Wong, P. Yiannacouras,
and D. P. Singh, “From opencl to high-performance
hardware on fpgas,” in 22nd international conference
on ﬁeld programmable logic and applications (FPL),
pp. 531–534, IEEE, 2012.
[14] V. Kathail, J. Hwang, W. Sun, Y. Chobe, T. Shui, and
J. Carrillo, “Sdsoc: A higher-level programming envi-
ronment for zynq soc and ultrascale+ mpsoc,” in Pro-
ceedings of the 2016 ACM/SIGDA International Sym-
posium on Field-Programmable Gate Arrays, pp. 4–4,
ACM, 2016.
[15] R. Zhao, W. Song, W. Zhang, T. Xing, J.-H. Lin,
M. Srivastava, R. Gupta, and Z. Zhang, “Accel-
erating Binarized Convolutional Neural Networks
with Software-Programmable FPGAs,” Int’l Symp. on
Field-Programmable Gate Arrays (FPGA), Feb 2017.
[16] L. Cavigelli and L. Benini, “Origami: A 803-gop/s/w
convolutional network accelerator,” IEEE Transac-
tions on Circuits and Systems for Video Technology,
vol. 27, no. 11, pp. 2461–2475, 2016.
[17] J. Bachrach, H. Vo, B. Richards, Y. Lee, A. Water-
man, R. Aviˇzienis, J. Wawrzynek, and K. Asanovi´c,
“Chisel: constructing hardware in a scala embedded
language,” in DAC Design Automation Conference
2012, pp. 1212–1221, IEEE, 2012.
[18] “Pynq:
Python productivity for zynq.” http://
www.pynq.io/. Accessed: 04/21/2019.
6
