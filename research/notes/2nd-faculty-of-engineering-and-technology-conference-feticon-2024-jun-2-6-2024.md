---
title: 2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2
  - 6, 2024,
id: 2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024
tags:
- btech-ece-projects-259aee
created: '2026-09-25T03:15:15.010992Z'
source: https://arxiv.org/pdf/2412.20400
source_domain: arxiv.org
fetched_at: '2026-09-25T03:15:15.010268Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
raw_file: raw/2nd-faculty-of-engineering-and-technology-conference-feticon-2024-jun-2-6-2024.pdf
doi: arXiv:2412.20400
---

2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2 - 6, 2024, 
University of Ilorin, Nigeria 
1 
 
Design of an Improved Microstrip Antenna Operating at a Frequency Band of 28 GHz  
 
S. O. Zakariyya1*, V. O. Omole1, B. O. Sadiq2,3, R. A. Alao1 , J. A. Adesina4 , E. Obi5  
 
1Electrical and Electronics Engineering Department, University of Ilorin, Ilorin, Nigeria. 
2Electrical and Computer Engineering, Kampala International University, Uganda 
3Computer Engineering Department, Ahmadu Bello University, Zaria, Nigeria 
4Computer Engineering Department, University of Ilorin, Ilorin, Nigeria. 
5Electronics and Telecommunication Engineering Department, Ahmadu Bello University, Zaria, Nigeria 
*Email: zakariyya.os@unilorin.edu.ng 
 
 
ABSTRACT  
The design of an improved microstrip antenna operating in the 28 GHz frequency spectrum is the main goal of 
this work. The design used a Roger RT 5880 LZ substrate with a thickness and permittivity of 0.762mm and 
1.96, respectively. The antenna was simulated in CST Microwave Studio. As the antenna feed, a quarter-wave 
transformer was used to provide an impedance match of 50 ohms. To improve the antenna's performance, a U-
shaped element was added to the ground plane. The antenna resonated at 28 GHz frequency, according to 
simulation data, with a return loss of -21.4 dB, VSWR of 1.18, bandwidth of 2.026 GHz, and gain of 8.19 dB. 
The proposed antenna exhibits a performance improvement in terms of gain and bandwidth due to the addition 
of U-shaped element when benchmarked with existing designs in the literature work.  
 
KEYWORDS: 5G communication, Microstrip, Antenna, quarter-wave transformer, CST microwave studio 
1. 
INTRODUCTION  
The evolution of mobile and cellular networks has experienced remarkable progress over recent decades, 
evolving through various generations that each introduced enhanced features surpassing their predecessors. 
Demand for bandwidth and mobile broadband has surged exponentially in the last decade, resulting in a 
significant increase in data traffic that largely outpaced the capabilities of prior generations, most notably 4G. 
This burgeoning demand, particularly for data-intensive applications, necessitated a shift towards higher 
frequencies beyond the traditionally used sub-6 GHz range before the advent of 5G. These earlier frequencies, 
though sufficient for past needs, began to experience congestion issues and network capacity limitations, 
underscoring the imperative for higher bandwidth and data rates to support the emerging landscape of digital 
consumption and services (Zakariyya et al., 2019). 
5G technology has been designed to address these challenges by not only utilizing the existing sub-6 GHz 
frequency bands but also expanding into the millimeter-wave spectrum, which ranges from 24 GHz to 100 GHz. 
This shift to higher frequencies is a cornerstone of 5G's ability to provide higher data rates, reduced latency, and 
increased capacity and the ability to connect numerous devices simultaneously. The millimeter waves 
frequencies, despite their limited propagation range and higher susceptibility to both attenuation and 
environmental obstructions, unlocks the potential for significantly expanded bandwidth and capacity. Among 
the existing millimeter waves spectrum, 28-GHz is notably preferred for 5G applications due to its lower 
atmospheric absorptions and attenuations rates (Larsson et al, 2014; Hu et al, 2018). 
The design of antennas, especially Microstrip Patch Antennas (MPAs), is crucial in overcoming the limitations 
of the millimeter wave band and maximizing the use of this wider frequency range. MPAs offer significant 
advantages due to their compact size, design flexibility, and seamless integration with diverse devices and 
network setups (Zakariyya et al., 2015; Zakariyya et al., 2016; Salami et al., 2018). However, traditional patch 
antennas often suffer from low gain and limited bandwidth. To address these shortcomings, this study introduces 
an improved patch antenna tailored for 5G communication. 
Rahman et al. (2016) presented an antenna operating at 28 GHz with a bandwidth of 2.66 GHz. However, this 
design lacked compactness and had a low gain. Przesmycki et al. (2020) designed a rectangular patch antenna 
operating at 28 GHz, utilizing RT/duroid substrate. This antenna achieved notable metrics. However, the gain 
did not meet the requirements for 5G applications. Awan et al. (2021) discussed a microstrip antenna with a 
defective ground structure (DGS) at 28 GHz. While this design exhibited good bandwidth and return loss, its 
gain may still be insufficient to overcome the path and absorption losses in the millimeter-wave spectrum. 


---

2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2 - 6, 2024, 
University of Ilorin, Nigeria 
2 
 
Kamal et al. (2021) introduced a single-band hook-shaped antenna at 28 GHz. This antenna demonstrated a 
good return and wide bandwidth. However, its size was not compact, and its gain was relatively low. 
Additionally, Raheel et al. (2021) proposed a microstrip patch antenna operating at 28/38 GHz. This design 
achieved a gain of 7.1 dBi and an impedance bandwidth of 1 GHz (27.6 GHz - 28.6 GHz). Hussain et al. (2022) 
attempted a circular microstrip patch antenna with two rectangular slots, showcasing a good impedance 
bandwidth. However, this antenna was relatively large and had a modest gain. Furthermore, Farahat & Hussein 
(2022) introduced a patch antenna operating in the 28/38 GHz bands, achieving a gain of 6.6 dB and a 
bandwidth of 1.23 GHz in the 28 GHz range. Gaid et al, 2024 proposed a microstrip patch antenna operating at 
28/38 GHz. This design achieved a gain of 8.1 dB and an impedance bandwidth of 1.43 GHz.  
These discussed antennas exhibit various strengths and weaknesses, such as wide bandwidths, high gains, or 
compact sizes. However, their performance can be improved by adding a U shape element on the ground plane. 
Hence, this research aims to strike a balance between antenna size, impedance bandwidth, and gain by designing 
a small-size antenna with high gain, optimal impedance bandwidth, and coverage of the 28 GHz band. 
 
 
 
2. 
ANTENNA DESIGN 
The initial step in creating a patch antenna involves selecting the substrate, as its properties, like thickness and 
dielectric constant, significantly impact the antenna's characteristics. In this particular design, a Roger RT 
5880LZ substrate was chosen with a thickness of 0.762mm and a relative dielectric constant of 1.96. Copper 
was used for both the patch conductor and ground plane. These materials were chosen due to their high 
conductivity. The dimensions of the patch element are calculated using transmission line model accordingly 
(Zakariyya et al., 2016; Balanis, 2005): 
                      𝑤𝑝𝑐=
𝑣
2𝑓𝑟√
2
𝜀𝑟_𝑙+1 
 
       
 
 
 
(1) 
The patch width is 𝑤𝑝𝑐, 𝜀𝑟_𝑙 is the relative dielectric constant and 𝑓𝑟 represents the frequency at which the 
antenna resonates and 𝑣 is the speed of light. 
The effective dielectric constant is expressed as where ℎ_𝑠 is substrate height: 
        𝜀𝑟_𝑒𝑓𝑓=
𝜀𝑟_𝑙+1
2
+
𝜀𝑟_𝑙−1
2
(1 + 12ℎ_𝑠
𝑤𝑝𝑐)
−1
2 
       
 
 
 
(2) 
As a result of fringing, the length of the patch is extended by a distance equal to: 
       ∆𝐿_𝑝= 0.412ℎ_𝑠
(𝜀𝑟_𝑒𝑓𝑓+0.3)(𝑤𝑝𝑐
ℎ_𝑠
⁄
+0.264)
(𝜀𝑟_𝑒𝑓𝑓−0.258)(𝑤𝑝𝑐
ℎ_𝑠
⁄
+0.8) 
       
 
 
(3) 
The length is determined by:  
                𝐿_𝑝= 𝐿_𝑒𝑓𝑓-2∆𝐿_𝑝  
       
 
 
 
 
(4) 
                 𝐿_𝑒𝑓𝑓=
𝑣
2𝑓𝑟√𝜀𝑟_𝑒𝑓𝑓  
 
       
 
 
 
(5) 
The edge impedance  𝑍𝑖𝑛 = 90
𝜀𝑟_𝑙2
𝜀𝑟_𝑙−1 (
𝐿_𝑝
𝑤𝑝𝑐)
2
         
 
 
 
 
(6) 
 Where 𝐿_𝑝 is the patch length 
The line impedance of the quarter wave is given by: 
                𝑍𝑇= √𝑍0𝑍𝑖𝑛  
 
       
 
 
 
 
(7) 
 The length (𝐿_𝑝) and width (𝑤𝑝𝑐) of the radiating patch for the design was calculated to be 3.2 mm and 4.4 mm 
using the mathematical equations described in (1-4). The load impedance at the edge of the patch is calculated to 
be approximately 190.5 ohms using Eq. (6).  A simulation model for the single element antenna implemented in 


---

2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2 - 6, 2024, 
University of Ilorin, Nigeria 
3 
 
CST-MWS is shown in Figure 1. For enhancement of the antenna performance, a U shape element is created on 
the ground plane to serve as parasitic element.  
 
Figure 1: Front and back view of the designed antenna 
 
 
3. 
RESULTS AND DISCUSSION  
3.1. Return Loss 
Figure 2 shows the return loss of the proposed MPA. For mobile communication systems, a standard value of -
10 dB is acceptable as the baseline for good performance. The proposed MPA has a return loss of -21.4 dB, 
resonating at the desired resonant frequency of 28 GHz and covering a frequency band of 27.185 GHz – 29.211 
GHz with a bandwidth of 2.026 GHz.  
3.2. Voltage Standing Wave Ratio 
Figure 3 shows the Voltage Standing Wave Ratio (VSWR) of the proposed MPA design. For mobile 
communication systems, the value of VSWR should be small (not more than 2.5 and close to 1.0) in order to 
ensure proper impedance matching and little amount of reflected power. The proposed MPA design achieved a 
VSWR of 1.18 at a resonant frequency of 28 GHz which indicates good matching between the feeding line and 
the radiating patch element. 
3.3. Radiation Pattern 
Figure 4a and Figure 4b shows the 2D and 3D radiation pattern plot of the proposed MPA design. As observed 
from the 3D plot, the proposed patch antenna design has a gain of 8.19 dBi which is considered acceptable in 
this scenario of compact antenna design.  
 
Figure 2: Return loss plot   
 
   
Figure 3: voltage standing wave ratio 


---

2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2 - 6, 2024, 
University of Ilorin, Nigeria 
4 
 
 
 
 
 Figure 4a: 2D Radiation pattern plot  
 
Figure 4b: 3D Radiation pattern plot 
Table 1 is a summary of the comparison between the proposed design and other reported 5G antennas. From the 
table, the proposed 5G antenna antenna is found to perform better than the majority of the counterparts in terms 
of the bandwidth and gain. 
Table 1: Comparison between the Proposed Design and Other Reported Antennas 
Reference Antennas 
S11(dB) 
Bandwidth (GHz) 
Gain (dB)  
Proposed design 
-21.4 
2.02 
8.19 
Gaid et al., 2024 
-45 
1.43 
8.1 
Farahat & Hussein, 
2022 
-34.5 
1.23 
6.6 
Raheel et al., 2021 
-25 
1 
7.1 
 
 
 
4. 
CONCLUSION  
A microstrip patch antenna has been designed for 5G applications in mobile communication. The antenna was 
designed to resonate at 28 GHz. A U-shape structure was added to the ground plane with the aim of enhancing 
the antenna's performance. The proposed MPA simulation results show that the return loss, bandwidth, gain and 
VSWR are -21.4 dB, 2.02 GHz, 8.19 dB, and 1.18, respectively. The proposed antenna offers highly competitive 
performance when compared to other designs. The suggested structure is a good candidate for 28 GHz band 
applications due to its simplicity, good radiation properties, and compactness 
 
 
REFERENCES  
Awan, W. A., Naqvi, S. I., Hussain Naqvi, A., Abbas, S. M., Zaidi, A., and Hussain, N. (2021). Design and 
characterization of wideband printed antenna based on DGS for 28 GHz 5G applications. Journal of 
Electromagnetic Engineering and Science, 21(3), 177–183. https://doi.org/ 10.26866/jees.2021.3.r.24 
Farahat, A. E., and Hussein, K. F. A. (2022). Dual-Band (28/38 GHz) Wideband MIMO Antenna for 5G 
Mobile Applications. IEEE Access, 10, 32213–32223. https://doi. org/10.1109/ACCESS.2022.3160724 
Gaid, A. S. A., Ali, A. M., Saif A., and Mohammed, W. A. A. (2024). Design and analysis of a low profile, 
high gain rectangular microstrip patch antenna for 28 GHz applications, Cogent Engineering, 11:1, 2322827, 
DOI: 10.1080/23311916.2024.2322827 
Hu, S., Rusek, F., and Edfors, O. (2018). Beyond Massive MIMO: The Potential of Data Transmission With 
Large 
Intelligent 
Surfaces. 
IEEE 
Transactions 
on 
Signal 
Processing, 
66(10), 
2746–
2758. doi:10.1109/tsp.2018.2816577 


---

2nd Faculty of Engineering and Technology Conference (FETiCON 2024), Jun. 2 - 6, 2024, 
University of Ilorin, Nigeria 
5 
 
Hussain, M., Mousa Ali, E., Jarchavi, S. M. R., Zaidi, A., Najam, A. I., Alotaibi, A. A., Althobaiti, A., and 
Ghoneim, S. S. M. (2022). Design and characterization of compact broadband antenna and its MIMO 
configuration for 28 GHz 5G applications. Electronics, 11(4), 523. https:// doi.org/10.3390/electronics11040523 
Kamal, M. M., Yang, S., Kiani, S. H., Sehrai, D. A., Alibakhshikenari, M., Abdullah, M., Falcone, F., 
Limiti, E., and Munir, M. (2021). A novel hook-shaped antenna operating at 28 GHz for future 5G mmwave 
applications. Electronics, 10(6), 673. https://doi.org/10.3390/electronics10060673 
Larsson, E., Edfors, O., Tufvesson, F., and Marzetta, T. (2014). Massive MIMO for next generation wireless 
systems. IEEE Communications Magazine, 52(2), 186–195. doi:10.1109/mcom.2014.6736761  
Przesmycki, R., Bugaj, M., and Nowosielski, L. (2020). Broadband microstrip antenna for 5G wireless 
systems operating at 28 GHz. Electronics, 10(1), 1. https://doi.org/ 10.3390/electronics10010001  
Raheel, K., Altaf, A., Waheed, A., Kiani, S. H., Sehrai, D. A., TuBBal, F., and Raad, R. (2021). E-shaped 
H-slotted 
dual 
band 
mmWave 
antenna 
for 
5G 
technology. 
Electronics, 
10(9), 
1019. 
https://doi.org/10.3390/electronics10091019  
Rahman, A., Yi, N. M., Ahmed, A. U., Alam, T., Singh, M. J., and Islam, Moha. M. M. T. (2016). A 
compact 5G antenna printed on manganese zinc ferrite substrate material. IEICE Electronics Express, 13(11), 
20160377–20160377. https://doi.org/10.1587/elex.13.20160377 
Salami, A. F., Zakariyya, O. S., Sadiq B. O., and Abdulrahman, O. A. (2018). Evaluative Assessment of an 
X-band  Microstrip  Patch  Antenna  for  Wireless  Systems.  ABUAD Journal of  Engineering  Research  and 
Development   (AJERD),  1(2) , 264-272. 
 Zakariyya, S. O. (2015). Modeling of Miniaturized, Multiband and Ultra-Wideband Fractal antenna. M.Sc. 
Thesis, Institute of Graduate studies and research, Eastern Mediterranean University, Gazimagusa, North 
Cyprus. 
Zakariyya, O. S., Sadiq B. O., Abdulrahman, O. A., and Salami, A. F. (2016). Modified edge fed Sierpinski 
carpet miniaturized microstrip Patch antenna. Nigeria Journal of Technology, 35(3), 637-641.  
Zakariyya, O. S., Sadiq B. O., Olaniyan, A. A., and Salami, A. F. (2016). Dual Band Fractal Antenna Design 
for Wireless Application. Computer Engineering and Applications Journal, 5(3), 101-108. 
Zakariyya, S. O., Sadiq, B. O., Adebayo, M. A., Salami, A. F., Usman, A. M., and Afolayan, M. A. (2019). 
A High Gain Patch Antenna Array for 5G Communication. 2nd International Conference of the IEEE Nigeria 
Computer Chapter (NigeriaComputConf), pp. 1-6. 
 
 
