---
title: Deploying Real-Time Speech Recognition on ESP32 Using TinyML and Edge Impulse
  | Springer Nature Link
id: deploying-real-time-speech-recognition-on-esp32-using-tinyml-and-edge-impulse-sp
tags:
- btech-ece-projects-259aee
created: '2026-09-25T03:15:38.314841Z'
source: https://link.springer.com/chapter/10.1007/978-3-031-97907-1_17
source_domain: link.springer.com
fetched_at: '2026-09-25T03:15:38.313893Z'
fetch_provider: builtin
status: draft
type: note
tier: unknown
content_type: unknown
deprecated: false
doi: 10.1007/978-3-031-97907-1_17
---

Deploying Real-Time Speech Recognition on ESP32 Using TinyML and Edge Impulse | Springer Nature Link
Skip to main content
Deploying Real-Time Speech Recognition on ESP32 Using TinyML and Edge Impulse
Conference paper
First Online:
01 October 2025
pp 211–230
Cite this conference paper
Save conference paper
View saved research
Artificial Intelligence – COMIA 2025
(COMIA 2025)
Abstract
The emergence of Tiny Machine Learning (TinyML) has enabled real-time on-device inference on ultra-low-power microcontrollers, eliminating reliance on cloud computing while significantly reducing latency, power consumption, and bandwidth requirements. This study explores the deployment of a TinyML-based speech recognition system on an ESP32 microcontroller, leveraging Edge Impulse for model development, Mel-Frequency Cepstral Coefficients (MFCCs) for feature extraction, and TensorFlow Lite for Microcontrollers (TFLM) for efficient inference.
The model was trained on a curated subset of the Google Speech Commands Dataset, incorporating background noise augmentation to enhance robustness in real-world environments. Using Edge Impulse’s EON Compiler, the model was fully quantized and optimized, achieving a 37% reduction in RAM usage and 27% in ROM. The final model attained 87.14% accuracy on testing data and 97.1% average classification confidence during real-time inference, with excellent noise rejection (99.6%) and latency of 266 ms.
Compared to state-of-the-art systems deployed on more powerful platforms, the proposed approach achieves competitive accuracy while maintaining real-time inference and minimal resource consumption on ultra-low-power hardware. This makes it particularly suitable for battery-powered IoT, robotics, and embedded automation applications where connectivity and energy efficiency are critical.
By balancing performance and efficiency, this research highlights the viability of deploying speech recognition systems on constrained microcontrollers. Future work will explore advanced architectures and enhanced feature extraction strategies to further improve recognition accuracy, especially for short or phonetically similar commands.
This is a preview of subscription content,
log in via an institution
to check access.
Access this chapter
Log in via an institution
Subscribe and save
Springer+
from $39.99 /Month
Starting from 10 chapters or articles per month
Access and download chapters and articles from more than 300k books and 2,500 journals
Cancel anytime
View plans
Buy Now
Chapter
USD 29.95
Price excludes VAT (USA)
Available as PDF
Read on any device
Instant download
Own it forever
Buy Chapter
eBook
USD 79.99
Price excludes VAT (USA)
Available as EPUB and PDF
Read on any device
Instant download
Own it forever
Buy eBook
Softcover Book
USD 99.99
Price excludes VAT (USA)
Compact, lightweight edition
Free shipping worldwide -
view details
Buy Softcover Book
Tax calculation will be finalised at checkout
Purchases are for personal use only
Institutional subscriptions
Similar content being viewed by others
TinyML Platforms Benchmarking
Chapter
© 2022
Modern C++ in Resource-Constrained Edge Systems: An ESP32 Evaluation Bridging Efficiency and Practical AI Applications
Chapter
© 2026
Portable Real-Time Sign Language Mediator with Embedded Machine Learning
Chapter
© 2026
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Personal Computing
Register-Transfer-Level Implementation
Speech and Audio Signal Processing
Control Structures and Microprogramming
Embedded Systems
Speech and Audio Processing
Tiny Machine Learning in Edge Computing Systems
References
Banbury, Colby, et al. MicroNets: Neural Network Architectures for Deploying TinyML Applications on Commodity Microcontrollers.
arXiv:2010.11267
(2021).
https://doi.org/10.48550/arXiv.2010.11267
David, Robert, et al.: TensorFlow lite micro: embedded machine learning on TinyML systems.
arXiv:2010.08678
(2021).
https://doi.org/10.08678/arXiv.2010.08678
Shi, W., Cao, J., Zhang, Q., Li, Y., L. Xu,: Edge computing: vision and challenges. IEEE Internet Things J.
3
(5) (2016).
https://doi.org/10.1109/JIOT.2016.2579198
Warden, P.: Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition,
arXiv:1804.03209
(2018).
https://doi.org/10.48550/arXiv.1804.03209
Kadir, A. D. I. A., Al-Haiqi, A., Din, N. M.: A Dataset and TinyML model for coarse age classification based on voice commands. In 15th IEEE Malaysia International Conference on Communications: Emerging Technologies in IoT and 5G, MICC 2021 - Proceedings, (2021).
https://doi.org/10.1109/MICC53484.2021.9642091
Njor, E., Madsen, J., Fafoutis, X.: A Primer for TinyML predictive maintenance: input and model optimisation. In: IFIP Advances in Information and Communication Technology (2022).
https://doi.org/10.1007/978-3-031-08337-2_6
Tsoukas, V., Boumpa, E., Giannakas, G., Kakarountas, A.: A review of machine learning and TinyML in healthcare. In: ACM International Conference Proceeding Series (2021).
https://doi.org/10.1145/3503823.3503836
Diab, M.S., Rodriguez-Villegas, E.: Embedded machine learning using microcontrollers in wearable and ambulatory systems for health and care applications: a review. IEEE Access
10
(2022).
https://doi.org/10.1109/ACCESS.2022.3206782
Abadade, Y., et al.: A comprehensive survey on TinyML. IEEE Access
11
(2023).
https://doi.org/10.1109/ACCESS.2023.3294111
Ray, P.P.: A review on TinyML: state-of-the-art and prospects. J. King Saud Univ. Comput. Inf. Sci.
34
(4) (2022).
https://doi.org/10.1016/j.jksuci.2021.11.019
Pačnik, G., Benkič, K., Brečko, B.: Voice operated intelligent wheelchair - VOIC. In: IEEE International Symposium on Industrial Electronics (2005).
https://doi.org/10.1109/ISIE.2005.1529099
Sharifuddin, M.S.I., Nordin, S., Ali, A.M.: Voice control intelligent wheelchair movement using CNNs. In: Proceedings - 2019 1st International Conference on Artificial Intelligence and Data Sciences, AiDAS 2019, (2019).
https://doi.org/10.1109/AiDAS47888.2019.8970865
Sharifuddin, M.S.I., Nordin, S. Ali, A.M.: Comparison of CNNs and SVM for voice control wheelchair. IAES Int. J. Artif. Intell.
9
(3) (2020).
https://doi.org/10.11591/ijai.v9.i3.pp387-393
Sutikno, S., Anam, K., Sujanarko, B.: Design of electrical wheelchair navigation for disabled patient using convolutional neural networks on Raspberry Pi 3. In: AIP Conference Proceedings, (2020).
https://doi.org/10.1063/5.0014513
Jabardi, M.H.: Voice controlled smart electric-powered wheelchair based on artificial neural network. Int. J. Adv. Res. Comput. Sci.
8
(5) (2017).
https://doi.org/10.26483/ijarcs.v8i5.3650
Al-Rousan, M. Assaleh, K.: A wavelet- and neural network-based voice system for a smart wheelchair control. J. Franklin Inst.
348
(1) 2011.
https://doi.org/10.1016/j.jfranklin.2009.02.005
Sutikno, Anam, K., Saleh, A.: Voice controlled wheelchair for disabled patients based on CNN and LSTM. In: ICICoS 2020 - Proceeding: 4th International Conference on Informatics and Computational Sciences, (2020).
https://doi.org/10.1109/ICICoS51170.2020.9299007
Edge Impulse - The Leading Edge AI Platform (2025).
https://edgeimpulse.com/
Hymel, Shawn, et al.: Edge Impulse: An MLOps Platform for Tiny Machine Learning.
arXiv:2212.03332
, arXiv, el 28 de abril de (2023)
EON Compiler | Edge Impulse Documentation. (2024).
https://docs.edgeimpulse.com/docs/edge-impulse-studio/deployment/eon-compiler
Elhanashi, Abdussalam, et al.: Advancements in TinyML: applications, limitations, and impact on IoT devices. Electronics
13
(17), 3562 DOI.org (Crossref) (2024).
https://doi.org/10.3390/electronics13173562
Espressif Systems (2025).
https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf
INMP441 Datasheet (2025).
https://invensense.tdk.com/wp-content/uploads/2015/02/INMP441.pdf
Warden, P., Situnayake, D.: TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers. 1st Edn. O’Reilly (2020)
Google Scholar
Google Speech Commands Benchmark (Keyword Spotting).
https://paperswithcode.com/sota/keyword-spotting-on-google-speech-commands
Papers with Code - Learning Efficient Representations for Keyword Spotting with Triplet Loss (2025).
https://paperswithcode.com/paper/learning-efficient-representations-for-3
Shawn Hymel (2013).
https://shawnhymel.com/
B. Jacob et al.: Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference (2017).
https://doi.org/10.48550/arXiv.1712.05877
Download references
Author information
Authors and Affiliations
Facultad de Ingeniería, Universidad Panamericana, Augusto Rodin 498, 03920, Ciudad de México, Mexico
Manuel González & Hiram Ponce
Department of Mechanical Engineering, Tecnun, University of Navarra, 20018, San Sebastián, Spain
Sebastián Gutiérrez
Facultad de Ingeniería, Universidad Panamericana, Josemaría Escrivá de Balaguer 101, 20290, Aguascalientes, Mexico
Ricardo Espinosa
Authors
Manuel González
View author publications
Search author on:
PubMed
Google Scholar
Sebastián Gutiérrez
View author publications
Search author on:
PubMed
Google Scholar
Ricardo Espinosa
View author publications
Search author on:
PubMed
Google Scholar
Hiram Ponce
View author publications
Search author on:
PubMed
Google Scholar
Corresponding author
Correspondence to
Manuel González
.
Editor information
Editors and Affiliations
Universidad Panamericana, Mexico City, Distrito Federal, Mexico
Lourdes Martínez-Villaseñor
Instituto Politécnico Nacional, Mexico City, Mexico
Bella Martínez-Seis
Instituto Politécnico Nacional, Mexico City, Mexico
Obdulia Pichardo
Rights and permissions
Reprints and permissions
Copyright information
© 2025 The Author(s), under exclusive license to Springer Nature Switzerland AG
About this paper
Cite this paper
González, M., Gutiérrez, S., Espinosa, R., Ponce, H. (2025).  Deploying Real-Time Speech Recognition on ESP32 Using TinyML and Edge Impulse.

                     In: Martínez-Villaseñor, L., Martínez-Seis, B., Pichardo, O. (eds) Artificial Intelligence – COMIA 2025. COMIA 2025. Communications in Computer and Information Science, vol 2552. Springer, Cham. https://doi.org/10.1007/978-3-031-97907-1_17
Download citation
.RIS
.ENW
.BIB
DOI
:
https://doi.org/10.1007/978-3-031-97907-1_17
Published
:
01 October 2025
Publisher Name
:
Springer, Cham
Print ISBN
:
978-3-031-97906-4
Online ISBN
:
978-3-031-97907-1
eBook Packages
:
Artificial Intelligence (R0)
Springer Nature Proceedings excluding Computer Science
Share this paper
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
TinyML
Speech Recognition
Edge Impulse
TensorFlow Lite
ESP32
MFCC
Neural Networks
IoT
Energy-Efficient AI
Publish with us
Policies and ethics
Profiles
Manuel González
View author profile
Sebastián Gutiérrez
View author profile