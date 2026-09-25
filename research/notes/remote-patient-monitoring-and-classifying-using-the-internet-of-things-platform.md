---
title: Remote patient monitoring and classifying using the internet of things platform
  combined with cloud computing | Journal of Big Data | Springer Nature Link
id: remote-patient-monitoring-and-classifying-using-the-internet-of-things-platform
tags:
- btech-ece-projects-259aee
- iot-cloud-ml
- biomedical-electronics
- lstm
created: '2026-09-25T03:17:44.558187Z'
updated: '2026-09-25T03:18:10.148826Z'
source: https://doi.org/10.1186/s40537-021-00507-w
source_domain: link.springer.com
fetched_at: '2026-09-25T03:17:44.556544Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Open-access Journal of Big Data (Springer, 2021) paper proposing a remote
  patient-monitoring architecture combining IoT sensor data, 5G transport, and cloud
  computing, with an LSTM deep-neural-network classifier at the cloud core to prioritize
  sensitive information and remotely classify/monitor patient condition in both static
  (smart-home) and dynamic (mobile-health) scenarios, simulated in MATLAB. Reports
  the proposed LSTM-based method reaches 97.13% classification accuracy, a 10.41%
  average improvement over compared prior methods. Cited as reference [4] by the AD8232/ESP32
  IoT-ECG paper; provides the cloud-analytics/ML complement to that paper's sensor-hardware
  focus, useful for a B.Tech ECE project that wants to add cloud-based ML classification
  on top of a hardware ECG front end.
doi: 10.1186/s40537-021-00507-w
citation_count: 76
venue: Journal Of Big Data
is_retracted: false
---

*Suggested by [[iot-enabled-hemodynamic-surveillance-system-ad8232]] — cited primary source on IoT remote patient monitoring + cloud computing, ref [4]*

Remote patient monitoring and classifying using the internet of things platform combined with cloud computing | Journal of Big Data | Springer Nature Link
Skip to main content
SpringerOpen journals have moved to Springer Nature Link.
Learn more about website changes.
Remote patient monitoring and classifying using the internet of things platform combined with cloud computing
Research
Open access
Published:
08 September 2021
Volume 8
, article number
120
(
2021
)
Cite this article
You have full access to this
open access
article
Download PDF
Save article
View saved research
Journal of Big Data
Aims and scope
Submit manuscript
Remote patient monitoring and classifying using the internet of things platform combined with cloud computing
Download PDF
Abstract
Many researchers have recently considered patients’ health and provided an optimal and appropriate solution. With the advent of technologies such as cloud computing, Internet of Things and 5G, information can be exchanged faster and more securely. The Internet of things (IoT) offers many opportunities in the field of e-health. This technology can improve health services and lead to various innovations in this regard. Using cloud computing and IoT in this process can significantly improve the monitoring of patients. Therefore, it is important to provide a useful method in the medical industry and computer science to monitor the status of patients using connected sensors. Thus, due to its optimal efficiency, speed, and accuracy of data processing and classification, the use of cloud computing to process the data collected from remote patient sensors and IoT platform has been suggested. In this paper, a prioritization system is used to prioritize sensitive information in IoT, and in cloud computing, LSTM deep neural network is applied to classify and monitor patients’ condition  remotely, which can be considered as an important innovative aspect of this paper. Sensor data in the IoT platform is sent to the cloud with the help of the 5th generation Internet. The core of cloud computing uses the LSTM (long short-term memory) deep neural network algorithm. By simulating the proposed method and comparing the obtained results with other methods, it is observed that the accuracy of the proposed method is 97.13%, which has been improved by 10.41% in average over the other methods.
Similar content being viewed by others
IoT-enabled healthcare transformation leveraging deep learning for advanced patient monitoring and diagnosis
Article
Open access
30 July 2024
Remote Patient Monitoring Using IoT, Cloud Computing and AI
Chapter
© 2021
An Overview of Cloud Computing and the Internet of Things (IoT) in Health Care
Chapter
© 2025
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Health Informatics
Machine Learning
Big Data
e-Health
Internet of Things
Cloud Computing
Multicriteria Decision-Making in Healthcare Systems and Applications
Introduction
Cloud computing is one of the most valuable and promising research paths [
1
]. This computing method provides infrastructure and software services for users as well as the services requested by users through the Internet. Considering the notable growth of cloud computing, the number of clients and requests is increasing rapidly. Therefore, increasing the speed and accuracy of cloud computing is very important [
2
]. Using cloud computing can significantly improve the monitoring of patients. The cloud provides a powerful platform for performing hard and major computing activities that consists of several information processing operations from storing and processing to database and device services. The requirement to archive, analyze, and interpret high volumes of datasets has encouraged numerous companies and persons to support cloud computing [
3
].
In recent years, the healthcare service sector has become one of the main targets of the academic community and the financial market. This sector has attracted a lot of funds, mostly because of its research potential. The healthcare sector faces many problems, including insufficient resources, high cost of healthcare, and inefficient management of hospital resources. There are also a number of logistics challenges, such as the amount of medical care that patients need, the limited number of beds and equipment, as well as the small number of healthcare specialists. Patient monitoring is usually performed passively, meaning that medical teams control medication in response to changes in patient's health status [
4
].
The response time is very important, as in critical cases the patient's condition may be worsen. IoT offers many opportunities in the field of e-health. This technology can improve health services and lead to various innovations in this regard [
5
]. IoT acts as a catalyst for healthcare and plays a key role in healthcare services [
6
]. Body sensor network (BSN) detects abnormal and unforeseen conditions by evaluating the physiological parameters and symptoms and sending vital signs for medical evaluation. Therefore, the temporary medications can be prescribed immediately to prevent critical conditions. With the help of IoT, medical care processes are facilitated and the health services are also improved by using smart systems [
7
]. IoT provides a platform for achieving goals such as improving the quality of human life in terms of health and facilitating the daily lives of people with disabilities and chronic diseases. It has made life easier, especially for those who cannot be physically present to care for the patients [
8
].
E-health [
9
] is a field of research that has many benefits for society if it is properly employed. Some of the services that can be provided by IoT in the healthcare field include:
A.
Automatic collection of data related to the patient’s vital signs through a network of sensors connected to the medical equipment and patient’s body (software agents constantly monitor the collected data to identify any abnormalities in the health status of patients and inform healthcare specialists).
B.
Sending the collected data to the cloud platform of the medical center to be stored and processed.
C.
Comprehensive analysis of mobile health plans and sharing medical data.
Furthermore, it allows remote storage of data on cloud-based platforms and enables the cooperation of any authorized person, including external specialists and the internal team [
5
]. It is also an appropriate platform for health applications based on mobile/tablet/PDA devices. The use of smartphones provides numerous opportunities to create effective healthcare services and solutions. This research presents the simulation of a remote patient monitoring system based on IoT and cloud computing in two static (smart homes) and dynamic (mobile health) environments to increase the effectiveness of health services (in any place and any time) and improve the healthcare system using MATLAB simulator.
Therefore, the LSTM deep neural network is used in this paper to remotely classify and monitor the condition of patients. Data and information about the patients’ condition are provided via sensors in the IoT and 5th generation Internet to cloud computing and as an input to the LSTM deep neural network. The LSTM Deep Neural Network is based on trained input data and produces a model based on hidden layers and neural structure. Then it receives information about patients 'status for classification and evaluation and uses the generated model to classify and monitor patients’ health status remotely. In Sect.
2
, the related works are reviewed. Section
3
presents the proposed method. Finally, in Sects.
4
and
5
, the obtained results are given, followed by the conclusion and suggestions for future works.
Related work
In this section, the researches performed in the field of monitoring patients’ health status is reviewed, and then, the papers published in recent years are compared in Table
1
. This table provides the advantages and disadvantages of each method.
Table 1 Comparing the advantages and disadvantages of previous methods
Full size table
In [
4
], an enhanced optimized Genetic algorithm approach is proposed to obtain the high dimensionality in the gene expression data where SVM kernel classification methods are used to evaluate the discrete genetic structures with classifications that might be recommended as useful techniques in the prediction and finding new genes for malaria infection.
In [
5
], a Remote Patient Monitoring System (RPMS) aims to effectively manage the hospital resources through patient monitoring at home. RPMS is an IoT-based solution for patient monitoring that supports the automatic collection and transmission of patient data to remote databases. A web system provides access to this data through a user-friendly interface.
In [
10
], an innovative IoT-based system is developed for medication identification and prescription monitoring which is called Pharmaceutical intelligent information system (PIIS). This system can be used for examining medications to identify dangerous side effects, renal absorption reactions, side effects during pregnancy or lactation, and certain diseases such as tuberculosis.
In [
11
], a home monitoring and decision support system is provided to assist physicians in diagnosis, remote monitoring, treatment, prescription, rehabilitation, and progression of patients with Parkinson’s disease. This system is an expert system that collects tremor data and helps physicians diagnose and treat it.
In [
12
], an IoT-based health monitoring system is presented to investigate the role of smart data in the smart home based on remote health monitoring. Remote health monitoring is a technology that makes it possible to monitor the patients outside of clinical settings (usually at home), which can increase access to care and reduce the cost of providing healthcare.
In [
13
], an IoT-based mobile gateway (e.g. mobile/tablet/PDA, etc.) is developed for mobile health scenarios. The gateway automatically collects information such as location, heartbeat rate, and possible diagnosis, and promptly sends it to the caregivers.
In [
14
], an IoT-based health monitoring system is provided for children with autism. Health information for autistic patients is collected using a wearable sensor that is put on the head. Then the information read from the brains of these patients is continuously sent to the monitoring server. With any discrepancies in the information read, an alert is generated and an email is sent to the caregiver. In case of any emergency, alerts are also sent to the physician. Patient personal details can also be stored in a cloud environment for scalability and effective security.
In [
15
], an IoT-based framework for healthcare (Health IoT) is provided in which ECGs and other healthcare data are collected by mobile devices and sensors and securely sent to the cloud so that the specialists have access to them. Signal enhancement techniques, encryption, and other related analyses are used to prevent identity theft or clinical error.
In [
16
], a system called Smart Architecture for In-Home Healthcare (SAHHC) is proposed, which is a healthcare solution using the image and facial expressions used to monitor patients and the elderly who have special needs.
In [
17
], an IoT-based monitoring framework in the Intensive Care Unit (ICU) is proposed to improve the delivery of medical services. The framework presented in this paper focuses on the efficient monitoring of various events (and anomalies) with temporary dependencies, followed by time-sensitive alerts. The results show that IoT-equipped ICUs are much more efficient in monitoring sensitive events than manual and conventional Tele-ICU monitoring. In addition, the method to generate alerts provides more information and increases the advantages of the system.
In [
18
], a system for reminding and monitoring medication use is proposed which works with the help of IoT. This paper focuses on the medication and its use schedule which is useful for improving the efficiency of the prescribed medication and reducing the economic factor. They observed some monitoring technologies that build the in-home monitoring system. The monitoring system can be implemented with sensor components and a wireless module that should be secured so that the message containing the health information is not distorted. IoT plays a vital role in the communication between the two devices, the use of standard messages, and communication protocol so that we can securely communicate important health-related messages. The IoT open source cloud is efficient for storing sensor data. The advantage of digital storage is that it is easy to recover and performs faster in case of an emergency.
[
19
] Examines the IoT-based patient monitoring system. An IoT-based patient monitoring system is an alternative used to help patients with chronic diseases. The goal of this method is to improve the quality of life of patients-not only are they monitored, but they also gain the ability to improve their eating habits and exercise routine. The results of this study show that the developed model for the system at the time of making inferences and achieving results is as effective as orders to obtain measurements through sensors, as well as recommendations and exercise tips in improving patients' eating habits.
In [
20
] a patient monitoring system using IoT is proposed. The patient monitoring system is associated with a single concept called IoT. IoT is more than a connection between objects that have embedded technology with Internet infrastructure. Through using a wireless sensor network, smart monitoring and reliable connection between things can be achieved. Collecting data and information is a major challenge in wireless networking (sensors). The purpose of this method is to obtain efficient data from sources (patients) to the destination (physicians) by collecting data and disseminating information. The goal of data collection is to increase energy efficiency and disseminate information for data routing in the sensor network to reduce delays in data transmission from source to destination.
In [
21
] an intelligent patient monitoring system is proposed to monitor patients' health. Several sensors are used to collect a patient's biological behavior. Significant biological information is then transferred to the IoT cloud. The proposed system allows physicians and nurses to monitor patients in the Intensive Care Unit in real-time, which improves the efficiency and quality of services. There is a great opportunity to change this system as a wearable device that allows us to monitor the elderly or children from a remote distance.
In [
22
] new generation technology and IoT are used to manage and analyze a large amount of data. The main focus of this research is on patients' e-health and the IoT platform. By simulating their proposed method, they succeeded in achieving a significant improvement in patient health monitoring and analysis.
In [
23
] the health care monitoring system and IoT-based analysis is presented. In this research, an innovative IoT-based framework for health applications is successfully developed. The system can accurately measure three vital signs, including body temperature, heart rate, and blood pressure. Data is available for physicians to observe and monitor in real-time, even if patients take tests out of the clinical environment.
In [
24
] approach is proposed a long-term and short-term memory network and extends it to two mechanisms (i.e., time and attention-based) to conduct multi-label classification based on patients’ clinical visit records. The former mechanism is used to handle the temporal irregularity across clinical visits whereas the latter mechanism assists in determining the importance of each visit for the prediction task. Using a large clinical record data set collected from a hospital in Southeast China, the propose approach outperforms a variety of traditional and deep learning methods in predicting future disease diagnoses.
In [
25
] aims to provide a comprehensive analysis of DL models based on long-term memory (LSTM) with several performance measures on the MIT-BIH arrhythmia dataset for the heartbeat classification. The different variants of the LSTM DL model are offered for classification purposes. The results clearly show that the LSTM DL models are suitable for classifying heart beats.
In [
26
], a hybrid dimensionality reduction model is proposed for classifying the malaria vector data. Here, an optimized genetic algorithm (GA-O) is applied to extract subset relevant genes. The PCA and ICA are used on the subset data to extract latent components in the data. The combination of GA-O with PCA and GA-O with ICA are classified through KNN on a Mosquito Anopheles gambiae dataset.
In [
27
] the researcher is able to provide a method for analyzing the customer portfolio using clustering techniques, deep neural network, and online hybrid similarity criteria. However, each of the proposed methods has challenges such as inaccuracy and high error of recommendations.
According to the literature and the researches performed in the field of remote monitoring of patients' condition, it is observed that despite the different advantages of each proposed method, they have not yet been able to meet challenges like insufficient accuracy and high classification error. Here, the LSTM deep neural network is used to remotely classify and monitor the health status of patients. Data information is provided as an input to the deep neural network. Deep neural network is trained based on input data and produces a model based on hidden layers and neural structure. Then, it receives information about the patients' condition and uses the generated model to remotely classify and monitor patients' health status.
Methodology
In this section, the architecture of the proposed model is described. The following figure shows the architecture of the proposed method. As shown in Fig.
1
, patients are hospitalized at home or in the hospital wearing wrist sensors. These sensors collect the necessary information and send them to cloud computing servers. Sensors used in the proposed architecture include heart rate sensor, body temperature sensor, blood pressure sensor, blood sugar sensor, stress sensor, consciousness sensor, pulse counter, and accelerometer. These sensors are connected to the microcontroller using wires. The communication between the sensors and the microcontroller can also be wireless and via Wi-Fi. The number of sensors is not limited and can be increased.
Fig. 1
Full size image
The architecture of the proposed model
This paper considers a system called “prioritization system” as an IoT-based interface which detects more sensitive information and transmits it to the next level (cloud computing). The priority is allocated to the data as a label and used in the next steps. Therefore, the information is sent to the IoT-based priority system and the priority system forms a queue based on the priority of sensitive and non-sensitive information and sends the queue to the microcontroller at specific time intervals. The microcontroller is used to monitor the parameters of the sensors and as an interface to send the information from the patient to the mobile gateway (e.g. mobile/tablet/PDA, etc.). The microcontroller then encrypts the information with AES and sends it to the mobile gateway via Bluetooth or Wi-Fi. The mobile gateway, which is equipped with two SIM cards, sends it to cloud computing through 5G.
The LSTM deep neural network system is embedded at the core of cloud computing to remotely classify and monitor patients’ health status. The main task of the LSTM deep neural network algorithm is to determine the normal and acute conditions of patients. If the patient is in a severe condition based on the received information, the patient's deep neural network LSTM is detected and the relevant alarms are immediately sent to the patient, physician, nurse, and patient's family. Priority is given to the patients with an acute condition.
Description of the proposed method
The most important components of the proposed method are presented in the following sections.
Sensors
In [
6
], 3 sensors are used to monitor patients' health status. Unlike [
6
] which uses only 3 sensors, we use 8 sensors for patients. These sensors are as follows:
Heart rate sensor.
Body temperature sensor.
Blood pressure sensor.
Blood sugar level sensor.
Stress level sensor.
Consciousness level sensor.
Pulse counter.
Accelerometer.
In the method presented in [
6
], only pulse counter, accelerometer, and temperature sensor are used, which cannot report the different states of the patient and this may lead to disorders in the treatment process. Therefore, in this paper, we use more sensors to have an accurate analysis. The significant improvement that we achieve in the new architecture is that, first, we use more sensors and then, we apply a priority system.
Sensors that are installed in different parts of the body to maintain patients’ health are of great importance; and based on the current condition of the person, the priority of that sensor should be defined for the priority system. For example, body temperature, stress level, and blood pressure of a person with breast cancer are prioritized over other signs. This is also very important for other patients, especially patients with rare diseases. Therefore, the priority system makes it possible that the sensors send the information to the mobile gateway (e.g. mobile/tablet/PDA, etc.) based on the degree of sensitivity. For example, the pulse counter and heart rate sensor report pulse count information to the microcontroller every minute. The body temperature sensor also provides information about the patient's body temperature every 30 s. Other sensors also provide specific behavior as needed.
In the next step, the information is sent to the mobile gateway via Bluetooth and Wi-Fi. By installing this feature, we can take steps in energy consumption and reliability of sending information, as well as preventing data loss. In the following, this issue is discussed in detail.
Microcontroller interface (single node)
The microcontroller is used to monitor the parameters of the sensors and as an interface to send the information from the patient to the mobile gateway (e.g. mobile/tablet/PDA, etc.). The following section examines the process of encrypting and decrypting information using the AES algorithm.
Mobile gateway
In the next step, the encrypted information is sent from the microcontroller to the mobile gateway via Wi-Fi or Bluetooth. One of the features we have provided for the microcontroller is that sending data is possible both via Bluetooth and Wi-Fi. In some cases, the mobile phone is located near the patient, and information is sent via Bluetooth to the mobile gateway. In cases where the mobile phone is located at a far distance, the information is sent via Wi-Fi.
Reducing mobile energy consumption
So far, we have discussed how to connect a microcontroller to a mobile gateway. Considering that reducing energy consumption is one of the most important given criteria, we improve the operation of sending information via mobile. The strategy we have considered in the mobile interface or gateway to improve power consumption is that the mobile device/tablet/PDA is not constantly connected to the microcontroller. Based on the time schedules, we turn on Wi-Fi when necessary. Also, we do not perform the process of encryption on the mobile device or tablet, etc. As fully described in the previous section, this process is performed by the microcontroller to reduce energy consumption as much as possible. On the other hand, calculations and predictions are made by the mobile device and cloud computing data centers. Therefore, the amount of energy consumption is reduced.
Also, since the mobile device is connected to the Internet and energy consumption is very high when the Internet is turned on, with the interface provided in the mobile device, the Internet is turned off and the microcontroller is connected via Bluetooth when there is no need to send information to cloud computing, except when Bluetooth has a limited range, communication is taken place via Wi-Fi, in which case the mobile phone Internet is turned off before sending information. Also, one of the other given criteria is to design an architecture to produce a new and developed infrastructure by which we can provide a new model in the medical industry through IoT.
Providing two SIM cards for mobile
One of the most important features that [
8
] does not consider is that the mobile device does not have two SIM cards. Having only one SIM card in critical situations can result in major damage or death. If we use only one SIM card and it faces problems in data connection, receiving information will be aborted. So, here we use two SIM cards. Iranian telecommunications companies that offer SIM cards include MTN Iran cell, IR-MCI, and RighTel. Therefore, in critical situations, if the transmission of information faces problems, or one of the SIM cards does not work properly, the other SIM card starts working and the process of sending information continues. In such a situation, the reliability of the proposed model is approved.
5th generation mobile network or 5G
In this paper, we will apply the infrastructure for using the 5th generation mobile network so that the device which is equipped with this facility can use it. Moreover, we have used 3rd, 4th, and lower generations so that devices with lower capabilities can send messages. Therefore, in the proposed model, mobile gateways send their information to the cloud through the Internet and 5G by default. Cloud computing stores information and sends an alarm to the patient's family. Finally, the patient's family or the center takes necessary measures and guides the patient in critical situations.
Classification of patients using LSTM deep neural network
In this section, LSTM deep neural network algorithm is introduced for classification and monitoring of patients’ health status. After applying patient’s status data to the proposed system, the two important phases of the proposed method are as follows: the first part of the samples is used to train algorithm patterns in the deep learning system and the second part is used as test samples to test the proposed method in order to classify and monitor the condition of patients.
Separating data and training samples
One of the important phases that must be considered in the training of the LSTM deep neural network algorithm is the separation of the samples into two main parts. Data sampling is one of the stages of data mining that is considered in the proposed approach. There are different sampling methods, three of the most important are:
Random sampling.
Classified sampling.
Balanced sampling.
Random sampling is one of the simplest sampling methods. It acts randomly and separates samples from the original data to the desired extent. One of the disadvantages of this method is that it may not accurately reflect the whole dataset, and ultimately reduce the accuracy of data classification and validation of the proposed method. Stratified sampling method is also one of the improved methods of random sampling method. This method does the sampling process based on probability and also selects the samples as a percentage. However, it has its problems, too. For example, it may not select probability-based samples. In balanced sampling, one selects the required samples in a balanced way from the existing categories. This method does not have the problems of the previous methods and selects balanced samples or data from the available samples. The sampling method used in this paper is the balanced method to separate training data and test data. Therefore, 70% of the samples are training samples and 30% are test samples.
Applying LSTM deep neural network algorithm
Deep learning neural network is one of the important classes in the field of classification and monitoring of patients' condition. The structure of this classification is presented in the following. Four types of layers are used in the neural network part of the proposed method, and we will discuss them later.
Input layer
The parameters semantically examined in the previous section are applied in a normalized way as the input of the deep neural network. The nerves of this layer represent the input data vector resulting from the feature extraction step.
Hidden layers
Generally, neural network training and the initial weights enter the network, respectively in a supervised learning manner and Gaussian distribution (or normal distribution). By implementing backpropagation method, these weights are updated and reused in the network. This type of training is very slow and finding the local minimum instead of the general minimum has always been one of the challenges of this method. Hinton showed that we can solve this problem by using each layer pre-training employing Unsupervised Learning. Therefore, in this paper, deep neural network architecture is applied using the method proposed by Hilton [
28
]. The deep neural network architecture as well as the related explanations used in this paper is shown in Fig.
2
.
Fig. 2
Full size image
The basic architecture of deep neural network
Output layer
In this section, two types of output layers are used. An output layer called output layer 1 is used in order to rebuild the network. This layer is made of input and is used only to train the neural network. This layer obtains its input information from the last layer of the hidden layers and performs backpropagation. Another output layer that is used in this method is the soft max layer, called output layer 2. This layer is embedded in order to use regression. This method of data regression is a generalized logic regression.
This method is used when dealing with multiple data classes. The output of this method determines the probability of belonging to each class of data.
Software regression function
In logistic regression, the regression function has a nonlinear relationship with the linear combination of descriptive variables. This relationship is modeled with the Pro bit function. In definitions associated with classification, a binary variable is achieved [
28
]:
$${y}_{i}\in \left\{-1 . +1\right\}.$$
(1)
This is to regulate a Bernoulli Y random variable with (η) probability of success. Success probability depends on a predictor, η = η (x). If the predictor regulating a random variable is considered X, then η (x) is a conditional expectation of Y. In such a case we have (
2
):
$$E\left\{Y|X\right\}=\eta \left(x\right).$$
(2)
In classification, however, a link function to the relation form (
4
) transfers the expectation to the linear composition of the predictors. Such models are called generalized linear models. In the logistic regression, the link function is selected logarithmically according to (
3
).
$$g\left(a\right)=ln\frac{a}{1-a}.$$
(3)
The inverse of a logarithmic function is a logistic function that is selected as (
4
):
$${h}_{\theta }\left(x\right)=\frac{1}{1+\mathrm{exp}(-{\theta }^{T}.x)}.$$
(4)
In this method, the model parameters (θ), are optimized by the loss function as (
5
).
$$\left(\theta \right)=-\left[\sum_{i=1}^{m}\left\{\begin{array}{c}{y}^{\left(i\right)}.\mathrm{ln}\left({h}_{\theta }\left({x}^{\left(i\right)}\right)\right)+\\ \left(1-{y}^{\left(i\right)}\right).\mathrm{ln}\left(1-{h}_{\theta }\left({x}^{\left(i\right)}\right)\right)\end{array}\right\}\right].$$
(5)
Software regression is the generalized type of logistic regression and is used when there is more than one data class. According to the explanations given in this section, the neural network architecture used in this study can be shown as Fig.
3
. In this figure, the number of nerves in the input layer is assumed 4, which might be different based on the characteristics obtained in the feature extraction stage. Each hidden layer includes 3 layers with 3 nerves, which may change during the execution phase depending on the response, accuracy, and speed of the network.
Fig. 3
Full size image
The structure of LSTM used in the proposed model [
30
]
The performance of the proposed algorithm is based on deep learning. In this way, the training data set is entered into the core of the LSTM deep neural network algorithm and the model is generated. Test data is then entered into the model of the algorithm and makes a response for each test sample. Each response indicates whether the patient is in an acute condition or not. The response is either yes or no. The internal core of this algorithm is presented in the following format. The LSTM is a family of inductive algorithms for computer-based mathematical modeling of multi-parameter datasets that have fully automated structural and parametric optimization. LSTM can be used in areas such as data mining, knowledge discovery, making predictions, complex systems modeling, optimization, and pattern recognition. The results of Men et al. showed that the LSTM neural network performs better than classical prediction algorithms such as Single Exponential Smooth, Double Exponential Smooth, and Reproducible Neural Network [
24
].
LSTM algorithms are performed by an inductive method which sorts complex polynomial models and selects the best solution using the so-called external criterion [
30
]. In Fig.
2
, the LSTM network structure used in the proposed model is provided.
As shown in Fig.
3
,
\(X=\left({x}_{1}.{x}_{2}.\dots .{x}_{n}\right)\)
is entered into the artificial neural network as an input vector. Based on the X inputs, a set of nerves is formed in hidden layers and produces a neural network model. The artificial neural network includes an input vector, several hidden layers, and an output vector [
31
].
A set of neurons can represent the common LSTM algorithm. They have different pairs of nerve cells in each layer and join them using quadratic polynomials. The result of this connection is new neurons in the next layer. This method is defined to find a f defined function so that it can approach the actual output y for an input vector with data
\(X=\left({x}_{1}.{x}_{2}.{x}_{3}.\dots .{x}_{n}\right)\)
instead of the function f to predict output y. Therefore, according to M samples from single-output multiple-input data pairs, the following relationships are defined:
$${y}_{i}=f\left({x}_{i1}.{x}_{i2}.{x}_{i3}. \dots . . {x}_{in}\right). i=1.2.\dots .M.$$
(6)
An LSTM neural network might now be trained to predict output values.
$$X=\left({x}_{i1}.{x}_{i2}.{x}_{i3}.\dots .{x}_{in}\right).$$
(7)
Namely:
$${\widehat{y}}_{i}=\widehat{f}\left({x}_{i1}.{x}_{i2}.{x}_{i3}. \dots . . {x}_{in}\right). i=1.2.\dots .M.$$
(8)
Now in order to minimize the square of the difference between the predicted and the actual output, we face problem in determining a neural network of the deep neural network type:
$$\sum_{k=1}^{M}\left[(\widehat{f}\left({x}_{i1}.{x}_{i2}.{x}_{i3}.\dots .{x}_{in}\right)-{y}_{i}{)}^{2}\right]\to Min.$$
(9)
The complex form polynomial in the core of the deep neural network can be used to represent the general relationship between input and output variables. The complex polynomial is represented in (
10
):
$$\widehat{y}={a}_{0}+\sum_{i=1}^{m}{a}_{i}{x}_{i}+\sum_{i=1}^{m}\sum_{j=1}^{m}{a}_{ij}{x}_{i}{x}_{j}+\sum_{i=1}^{m}\sum_{j=1}^{m}\sum_{k=1}^{m}{a}_{ijk}{x}_{i}{x}_{j}{x}_{k}+\dots $$
(10)
This is known as Ivakhnenko polynomial [
31
]. However, most programs use the two-variable form to predict the output y:
$$\widehat{y}=G\left({x}_{i}.{x}_{j}\right)={a}_{0}+{a}_{1}{x}_{i}+{a}_{3}{x}_{i}^{2}+{a}_{4}{x}_{j}^{2}+{a}_{5}{x}_{i}{x}_{j}.$$
(11)
Using regression techniques, the coefficients a
i
in (
11
) are calculated in order to measure the difference between the actual returns
\(\widehat{y}\)
.
\(\widehat{y}\)
is minimized for each pair (
x
i
,x
j
) as an input. The variables actually show that a polynomial tree is constructed using the quadratic form in (14), whose coefficients are obtained in the least squares. Therefore, the coefficients of each quadratic function Gi are obtained to optimize the total input–output pair of the set:
$${r}^{2}=\frac{\sum_{i=1}^{M}({y}_{i}-{G}_{i})}{\sum_{i=1}^{M}{y}_{i}^{2}}\to M in.$$
(12)
\(({y}_{i}.i=1.2.\dots .M)\)
. The polynomial structure of regression in (
12
) can include the dependent samples
\(p.q\epsilon \left\{1.2.\dots .M\right\}\)
for the difference
\(\left(\begin{array}{c}n\\ 2\end{array}\right)=n(n-1)/2\)
as the least squares
\(\left\{\left({y}_{i}.{x}_{ip}.{x}_{iq}\right).\left(i=1.2.\dots .M\right)\right\}\)
(This means that it is possible to construct a triple M data)
p
،
q
’ 1،2 uses such examples.
$$\left[\begin{array}{cc}{x}_{1p}& {x}_{1q}\\ {x}_{2p}& {x}_{2q}\\ \begin{array}{c}\cdots \\ {x}_{Mp}\end{array}& \begin{array}{c}\cdots \\ {x}_{Mq}\end{array}\end{array} \begin{array}{cc}\vdots & {y}_{1}\\ \vdots & {y}_{2}\\ \begin{array}{c}\cdots \\ \vdots \end{array}& \begin{array}{c}\cdots \\ {y}_{M}\end{array}\end{array}\right].$$
If a quadratic subunit is used in (
13
), for each row of M data, the following matrix equation is obtained:
$$\mathrm{Aa}\hspace{0.17em}=\hspace{0.17em}\mathrm{Y}, $$
(13)
where a vector of unknown quadratic polynomial coefficients is in (
11
):
$$a=\left\{{a}_{0}.{a}_{1}.{a}_{2}.{a}_{3}.{a}_{4}.{a}_{5}\right\}.$$
(14)
$$Y=\{{y}_{1}.{y}_{2}.{y}_{3}.\dots .{y}_{M}{\}}^{T}.$$
The vector is the output values of the samples:
$$A=\left[\begin{array}{ccc}\begin{array}{c}1\\ \begin{array}{c}1\\ \vdots \\ 1\end{array}\end{array}& \begin{array}{c}{x}_{1p}\\ \begin{array}{c}{x}_{2p}\\ \vdots \\ {x}_{Mp}\end{array}\end{array}& \begin{array}{ccc}\begin{array}{c}{x}_{1q}\\ \begin{array}{c}{x}_{2q}\\ \vdots \\ {x}_{Mp}\end{array}\end{array}& \begin{array}{c}{x}_{1p}{x}_{1q}\\ \begin{array}{c}{x}_{2p}{x}_{2q}\\ \vdots \\ {x}_{Mp}{x}_{Mq}\end{array}\end{array}& \begin{array}{cc}\begin{array}{c}{x}_{1p}^{2}\\ \begin{array}{c}{x}_{2p}^{2}\\ \vdots \\ {x}_{Mp}^{2}\end{array}\end{array}& \begin{array}{c}{x}_{1q}^{2}\\ \begin{array}{c}{x}_{2q}^{2}\\ \vdots \\ {x}_{Mq}^{2}\end{array}\end{array}\end{array}\end{array}\end{array}\right].$$
The least squares method of multiple regression analysis leads to the solving normal equations as follows:
$$a=({A}^{T}A{)}^{-1}{A}^{T}Y.$$
(15)
That the vector determines the best coefficients of the quadratic equation according to Eq. (
11
) for the whole triple M data set. However, this solution, which is derived directly from normal equations, is almost capable of bypassing errors. Therefore, with this core, the process of model development, classifying, and monitoring of patients is performed.
Simulation results of the proposed method
In this section, we first describe the system features for implementing the proposed method and then compare the results of the proposed method with those of other methods.
System specifications for simulation
The proposed method in this research has been implemented using MATLAB. Table
2
also shows the features of the system in which the proposed method is implemented and the results are evaluated.
Table 2 System specifications for simulating and evaluating the results
Full size table
As can be seen in Table
2
, the operating system used in this study is Windows 7 with a 32-bit operating system. The RAM used is 4–3.06 GB usable, the Intel processor—the number of cores is 7 (Core ™) i7 CPU)—Q 720 @ 1.60 GHz is 1.60 GHz.
Dataset
This study uses datasets associated with IoT devices that are connected to patients in the form of wrist sensors. Data received from IoT devices is distributed on an hourly basis. Therefore, about 10,000 data are received per hour and samples are more than 1 terabyte. IoT servers connected to patients store data received from IoT devices in 24 h. Table
3
shows an example of the dataset suggested in the proposed method.
Table 3 An example of the dataset suggested in the proposed method
Full size table
As can be seen in Table
3
, 10 individuals are examined and their health status is assessed considering different conditions in different times of the day. We can observe that tachycardia is not a significant criterion to determine critical condition during heavy activities or sports.
Assessment criteria
The following equations measure accuracy, precision and recall [
27
,
29
].
$${Accuracy}_{j}= \frac{{\sum }_{i=1}^{n}TP(i)+ {\sum }_{i=1}^{n}TN(i)}{{\sum }_{i=1}^{n}TP\left(i\right)+FN(i)+FP\left(i\right)+TN(i)}.$$
(16)
$${\mathrm{Sensitivity}}_{j}= \frac{{\sum }_{i=1}^{n}TP(i)}{{\sum }_{i=1}^{n}TP\left(i\right)+FN(i)}.$$
(17)
$${\mathrm{Specificity}}_{j}=\frac{{\sum }_{i=1}^{n}TN(i)}{{\sum }_{i=1}^{n}FP\left(i\right)+TN(i)}.$$
(18)
TP (True Positive) indicates patients who are in a normal health condition and identified as normal by the proposed method. TN (True Negative) indicates patients who are in a normal health condition but identified as critical by the proposed method. FP (False Positive) indicated patients who are in critical health condition and identified as normal by the proposed method. Finally, FN (False Negative) indicates patients who are in a critical health condition and identified as critical by the proposed method. n indicates the number of samples and i is between 1 and n [
27
].
Comparing the results
In this section, the results obtained from the simulation carried out in accordance with the proposed model are discussed. In this paper, the obtained results are compared with the findings of [
13
]. In this section, the accuracy of the proposed algorithm in different states of the patient’s body is discussed. We consider this criterion in our simulation and compare the obtained results with the results of this article. The following figure shows the final accuracy of the proposed model where the number of sensors is 8 and each sensor sends 100 events per unit of time to the microcontroller.
As seen in Fig.
4
, the vertical axis indicates the degree of accuracy of patients' health control and the horizontal axis shows the percentage of response to events sent to the hospital center by sensors. The proposed model has 100% accuracy to respond and send information in 95% of different cases. While other methods with fewer sensors, such as 2, 3, and 4 sensors, have an accuracy of 90% to 10%. One of the most important reasons for the high accuracy of the proposed method for sending and receiving information from sensors to the hospital center or to cloud computing is the use of the IoT technology and 5G platform. Also, the use of dual SIM mobile phones, wireless and wired communication channels has led to such accuracy. The following figure shows the test results of using 20 sensors compared to other methods.
Fig. 4
Full size image
Comparison of patient health control accuracy of the proposed method using 8 sensors with that of other methods
As it can be seen in Fig.
5
, the accuracy of sending and receiving data from sensors to the hospital center is 100% in 95% of cases and there is no challenges or problems regarding the data.
Fig. 5
Full size image
Results of the accuracy of sending and receiving data from sensors to the hospital in the proposed method using 20 sensors with that of other methods
Finally, we reduced the number of sensors on the patient's body so that we could measure the accuracy of diagnosing the patient’s conditions. The following figure shows the accuracy level of diagnosing the condition of patients in the proposed method.
As we can see in Fig.
6
, the accuracy of the proposed method in diagnosing patient’s condition in critical conditions is 100% and 87% in 70% and 30% of cases, respectively. However, it can be concluded that the number of patient sensors should be increased as much as possible to increase the accuracy of diagnosis and control of the patients’ condition.
Fig. 6
Full size image
The accuracy of classifying patients’ health status in the proposed model
Finally, we compare the final findings of this article with the results of the base article. The following figure shows the comparison of the accuracy of the proposed method with that of the reference [
13
].
As shown in Fig.
7
, the accuracy of the proposed method with 8 sensors is equal to 97.13% and the accuracy of the method proposed in [
13
] is equal to 89%. With these interpretations, the improvement rate of classification accuracy and diagnosis of patients in the proposed method compared to [
13
] is about 10.41%. In Table
4
shows the comparison of the results of the proposed method with other methods used in [
13
] in terms of accuracy, precision, and recall.
Fig. 7
Full size image
Comparison of classification accuracy and diagnosis accuracy of the proposed model with those of [
13
]
As seen in Table
4
, the accuracy level of the proposed model in identifying patients with critical health status is 97.13%. The proposed method compared to SVM, decision tree, KNN and Naïve Bayes methods is 21.87% and the improvement rate of the proposed method compared to the method suggested in [
13
] is 10.41%. The accuracy of identifying patients with critical health status in the proposed method is 98.44%. The proposed method is 39.64% compared to the SVM, Decision Tree, KNN, and Naïve Bayes methods and the improvement rate of the proposed method compared to the method suggested in [
13
] is 31.44%. The recall of identifying patients with critical health status in the proposed method is 98.21%. The proposed method is 14.96% compared to SVM, decision tree, KNN, and Naïve Bayes methods and the improvement rate of the proposed method compared to the method in [
13
] is 9.21%.
Table 4 The comparison of the proposed method based on LTSM deep neural network with that of [
13
] in terms of accuracy, precision, and recall
Full size table
Conclusion and future works
Patients who suffer from underlying and chronic diseases need special care which can be provided by a nurse, physician, hospital, and family. Home caregiving costs a lot and patients cannot stay in the hospital for a long time. In context-based systems, it is important to study sensitive tasks as well as present a framework that can provide the process of analyzing, and implementing new methods in the medical industry. Therefore, in this paper, a combination of cloud computing systems and IoT is used. At the core of IoT, the prioritization framework is used to prioritize sensitive requests, and in cloud computing, the LSTM deep neural network algorithm is used to remotely classify and monitor patients. By simulating and evaluating the results of the proposed method using MATLAB software, it is observed that the accuracy, precision, and recall of the proposed method compared to those of other methods have been significantly improved.
To further develop this study and to improve the results of the proposed method, the use of semantic methods and optimization techniques such as Krill Herd Optimization algorithm, compact cat swarm optimization algorithm, or Harris hawk’s optimization can be used in order to select the optimal features. Also, using reinforcement and collective learning systems instead of LSTM deep neural network algorithm can improve the results of this paper.
Availability of data and materials
The datasets generated and/or analysed during the current study are not publicly available due [REASON WHY DATA ARE NOT PUBLIC] but are available from the corresponding author on reasonable request.
References
Nan, Guofang et al. Distributed resource allocation in cloud-based wireless multimedia social networks. IEEE Netw. 28.4 (2014):74–80.‏2
Yu R, Zhang Y, Gjessing S, Xia W, Yang K. Toward cloud based vehicular networks with efficient resource management. IEEE Netw Mag. 2013;27(5):48–55.
Article
Google Scholar
Abiodun MK, Awotunde JB, Ogundokun RO, Misra S, Adeniyi EA, Arowolo MO, Jaglan V. Cloud and big data: a mutual benefit for organization development. J Phys Conf Ser. 2021;1767(1):012020 (
IOP Publishing
).
Article
Google Scholar
Adebiyi MO, Arowolo MO, Olugbara O. A genetic algorithm for prediction of RNA-seq malaria vector gene expression data classification using SVM kernels. Bull Elect Eng Informat. 2021;10(2):1071–9.
Article
Google Scholar
Suryandari Y. Survei IoT healthcare device. J Sistem Cerdas. 2020;3:153–64.
Article
Google Scholar
Mutlag A, et al. Enabling technologies for fog computing in healthcare IoT systems. Fut Generat Comput Syst. 2019;90:62–78.
Article
Google Scholar
Chrystinne OF, Carlos de JPL. An internet of things application with an accessible interface for remote monitoring patients. Springer International Publishing Switzerland; 2015.
Geetha G, Mohana Prasad K. Survey on real-time diabetic patient’s monitoring using internet of things. In: Artificial intelligence techniques for advanced computing applications. Springer, Singapore 259–270.‏9.
Qureshi KN, Din S, Jeon G, Piccialli F. An accurate and dynamic predictive model for a smart M-Health system using machine learning. Inform Sci. 2020;538:486–502.
Article
MathSciNet
Google Scholar
Jara AJ, Zamora MA, Skarmeta AF. Drug identification and interaction checker based on IoT to minimize adverse drug reactions and improve drug compliance. Pers Ubiquit Comput. 2014;18(1):5–17.
Article
Google Scholar
Chiuchisan, I. U. L. I. A. N. A., O. A. N. A. Geman. An approach of a decision support and home monitoring system for patients with neurological disorders using internet of things concepts. WSEAS Trans Syst. 13.1 (2014): 460–469.‏
Puustjärvi J, Puustjärvi L. The role of smart data in smart home: health monitoring case. Proc Comput Sci. 2015;69:143–51.
Article
Google Scholar
Santos J, et al. An IoT-based mobile gateway for intelligent personal assistants on mobile health environments. J Netw Comput Appl. 2016;71:194–204.
Article
Google Scholar
, Sundhara Kumar KB, Krishna B. IoT based health monitoring system for autistic patients. In: Proceedings of the 3rd International Symposium on Big Data and Cloud Computing Challenges (ISBCC-16’). Springer, Cham, 2016.‏
Shamim Hossain M, Ghulam M. Cloud-assisted industrial internet of things (iiot)-enabled framework for health monitoring. Comput Netw. 2016;101:192–202.
Article
Google Scholar
Mano LY, et al. Exploiting IoT technologies for enhancing Health Smart Homes through patient identification and emotion recognition. Comput Commun. 2016;89:178–90.
Article
Google Scholar
Bhatia M, Sood SK. Temporal informative analysis in smart-ICU monitoring: M-HealthCare perspective. J Med Syst. 2016;40(8):1–15.
Article
Google Scholar
Zanjal SV, Talmale GR. Medicine reminder and monitoring system for secure health using IOT. Proc Comput Sci. 2016;78:471–6.
Article
Google Scholar
Gupta S, Lipika G, Abhay KA. A novel framework of health monitoring systems. In: International Journal of Big Data and Analytics in Healthcare (IJBDAH) 2021;6.1:1–14.‏
Shaikh S et al. Patient monitoring system using iot. In: 2017 International Conference on Big Data, IoT and Data Science (BID). IEEE, 2017.‏
Uddin MS, Jannat BA, Suraiya B. Real time patient monitoring system based on Internet of Things. In: 2017 4th International Conference on Advances in Electrical Engineering (ICAEE). IEEE, 2017.‏
Dey N, Ashour AS, Bhatt C. Internet of things driven connected healthcare. In: Internet of things and big data technologies for next generation healthcare. Springer, Cham, 2017. pp 3–12.‏
Tan ET, Abdul HZ. Health care monitoring system and analytics based on internet of things framework. IETE J Res. 2019;65.5:653–60.
Article
Google Scholar
Rahmani AM, et al. Exploiting smart e-Health gateways at the edge of healthcare Internet-of-Things: a fog computing approach. Fut Generat Comput Syst. 2018;78:641–58.
Article
Google Scholar
Hiriyannaiah S, Siddesh GM, Kiran MHM, Srinivasa KG. A comparative study and analysis of LSTM deep neural networks for heartbeats classification. Heal Technol. 2021;11(3):663–71.
Article
Google Scholar
Arowolo MO, Adebiyi MO, Adebiyi AA, Olugbara O. Optimized hybrid investigative based dimensionality reduction methods for malaria vector using KNN classifier. J Big Data. 2021;8(1):1–14.
Article
Google Scholar
Vahidi Farashah M, Etebarian A, Azmi R, et al. An analytics model for TelecoVAS customers’ basket clustering using ensemble learning approach. J Big Data. 2021;8:36.
Article
Google Scholar
Hinton GE, Salakhutdinov RR. Reducing the dimensionality of data with neural networks. Science. 2006;313(5786):504–7.
Article
MathSciNet
Google Scholar
Vahidi Farashah M, Etebarian A, Azmi R, et al. A hybrid recommender system based-on link prediction for movie baskets analysis. J Big Data. 2021;8:32.
Article
Google Scholar
Farlow SJ. Self-organizing methods in modeling: GMDH type algorithms. CRC Press; 2020.
Xiao FF, et al. Artificial neural networks forecasting of PM2. 5 pollution using air mass trajectory based geographic model and wavelet transformation. Atmos Environ. 2015;107:118–28.
Article
Google Scholar
Download references
Acknowledgements
Not applicable.
Funding
Not applicable.
Author information
Authors and Affiliations
Department of Computer Engineering, Sabzevar Branch, Islamic Azad University, Sabzevar, Iran
Somayeh Iranpak
Department of Computer Engineering, Faculty of Engineering, University of Guilan, Rasht, Iran
Asadollah Shahbahrami
Department of Computer Engineering, Mashhad Branch, Islamic Azad University, Mashhad, Iran
Hassan Shakeri
Authors
Somayeh Iranpak
View author publications
Search author on:
PubMed
Google Scholar
Asadollah Shahbahrami
View author publications
Search author on:
PubMed
Google Scholar
Hassan Shakeri
View author publications
Search author on:
PubMed
Google Scholar
Contributions
All authors contributed to developing the ideas, and writing and reviewing this manuscript. All authors read and approved the final manuscript.
Corresponding author
Correspondence to
Asadollah Shahbahrami
.
Ethics declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing interests
The authors declare that they have no competing interests.
Additional information
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Rights and permissions
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by/4.0/
.
Reprints and permissions
About this article
Cite this article
Iranpak, S., Shahbahrami, A. & Shakeri, H. Remote patient monitoring and classifying using the internet of things platform combined with cloud computing.
J Big Data
8
, 120 (2021). https://doi.org/10.1186/s40537-021-00507-w
Download citation
Received
:
15 April 2021
Accepted
:
20 August 2021
Published
:
08 September 2021
Version of record
:
08 September 2021
DOI
:
https://doi.org/10.1186/s40537-021-00507-w
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
Internet of things (IoT)
Cloud computing
Remote patient monitoring
Patient data analysis
Profiles
Asadollah Shahbahrami
View author profile