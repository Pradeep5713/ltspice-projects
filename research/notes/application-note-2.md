---
title: Application Note
id: application-note-2
tags:
- btech-ece-projects-259aee
- power-electronics
- buck-converter
- ti-application-note
created: '2026-09-25T03:19:59.097940Z'
updated: '2026-09-25T03:21:14.967122Z'
source: https://www.ti.com/lit/pdf/slva477
source_domain: www.ti.com
fetched_at: '2026-09-25T03:19:59.096683Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'TI application note SLVA477 giving the step-by-step formulas for calculating
  a buck converter power stage built around an integrated-switch IC in continuous
  conduction mode: maximum duty cycle D = VOUT/(VIN(max) x eta) with eta estimated
  at 90% worst case; inductor ripple current from VIN(max), VOUT, D, L, and switching
  frequency fS; max IC output current = ILIM(min) - deltaIL/2; inductor sizing via
  deltaIL = 20%-40% of IOUT(max); Schottky rectifier diode average current IF = IOUT(max)
  x (1-D) and diode power PD = IF x VF x D; feedback resistor divider sized so IR1/2
  >= 100 x IFB (<1% error); input/output ceramic capacitor guidance (X5R or better,
  low ESR) plus COUT(min) formulas for ripple (deltaIL/(8 x deltaVOUT x fS)) and for
  transient overshoot.'
raw_file: raw/application-note-2.pdf
---

Application Note
Basic Calculation of a Buck Converter's Power Stage
Brigitte Hauke
Low Power DC/DC Applications
Abstract
This application report gives the formulas to calculate the power stage of a buck converter built with an 
integrated circuit having a integrated switch and operating in continuous conduction mode. It is not intended to 
give details on the functionality of a buck converter or how to compensate a converter. For additional information, 
see the references at the end of this document.
Appendix A contains the formulas without description.
Table of Contents
1 Basic Configuration of a Buck Converter.............................................................................................................................2
1.1 Necessary Parameters of the Power Stage.......................................................................................................................2
2 Calculate the Maximum Switch Current............................................................................................................................... 2
3 Inductor Selection...................................................................................................................................................................3
4 Rectifier Diode Selection........................................................................................................................................................4
5 Output Voltage Setting........................................................................................................................................................... 4
6 Input Capacitor Selection.......................................................................................................................................................5
7 Output Capacitor Selection....................................................................................................................................................5
8 References.............................................................................................................................................................................. 6
9 Revision History......................................................................................................................................................................6
A Formulas to Calculate the Power State of a Buck Converter.............................................................................................7
List of Figures
Figure 1-1. Buck Converter Power Stage....................................................................................................................................2
Figure 5-1. Resistive Divider for Setting the Output Voltage....................................................................................................... 4
www.ti.com
Table of Contents
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Basic Calculation of a Buck Converter's Power Stage
1
Copyright © 2026 Texas Instruments Incorporated


---

1 Basic Configuration of a Buck Converter
Figure 1-1 shows the basic configuration of a buck converter where the switch is integrated in the selected 
integrated circuit ( IC). Some converters have the diode replaced by a second switch integrated into the 
converter (synchronous converters). If this is the case, all equations in this document apply besides the power 
dissipation equation of the diode.
VIN
VOUT
IIN
IOUT
CIN
COUT
L
D
SW
Figure 1-1. Buck Converter Power Stage
1.1 Necessary Parameters of the Power Stage
The following four parameters are needed to calculate the power stage:
1.
Input voltage range: VIN(min) and VIN(max)
2.
Nominal output voltage: VOUT
3.
Maximum output current: IOUT(max)
4.
Integrated circuit used to build the buck converter. This is necessary because some parameters for the 
calculations must be derived from the data sheet.
If these parameters are known, the power stage can be calculated.
2 Calculate the Maximum Switch Current
The first step to calculate the switch current is to determine the duty cycle, D, for the maximum input voltage. 
The maximum input voltage is used because this leads to the maximum switch current.
(max)
V
Maximum Duty Cycle: D =
V
η
´
OUT
IN
(1)
VIN(max) = maximum input voltage
VOUT = output voltage
η = efficiency of the converter, e.g., estimated 90%
The efficiency is added to the duty cycle calculation, because the converter also has to deliver the energy 
dissipated. This calculation gives a more realistic duty cycle than just the formula without the efficiency factor.
Use either an estimated factor, e.g., 90% (which is not unrealistic for a buck converter worst-case efficiency), or 
see the Typical Characteristics section of the data sheet of the selected converter.
The next step in calculating the maximum switch current is to determine the inductor ripple current. In the 
converter's data sheet; normally, a specific inductor or a range of inductors are named for use with the IC. 
So, use the recommended inductor value to calculate the ripple current, an inductor value in the middle of the 
recommended range, or if none is given in the data sheet, the one calculated in the Inductor Selection section of 
this application report.
(
)
IN(max)
OUT
L
S
V
V
D
Inductor Ripple Current: ΔI
=
L
-
´
´
f
(2)
VIN(max) = maximum input voltage
VOUT = desired output voltage
Basic Configuration of a Buck Converter
www.ti.com
2
Basic Calculation of a Buck Converter's Power Stage
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Copyright © 2026 Texas Instruments Incorporated


---

D = duty cycle calculated in Equation 1
fS = minimum switching frequency of the converter
L = selected inductor value
It now has to be determined if the selected IC can deliver the maximum output current.
L
MAXOUT
LIM(min)
ΔI
Maximum output current of the selected IC: I
= I
2
-
(3)
ILIM(min) = minimum value of the current limit of the integrated switch (given in the data sheet)
ΔIL = inductor ripple current calculated in Equation 2
If the calculated value for the maximum output current of the selected IC, IMAXOUT, is below the system's required 
maximum output current, the switching frequency has to be increased to reduce the ripple current or another IC 
with a higher switch current limit has to be used.
Only if the calculated value for IMAXOUT is just a little smaller than the needed one, it is possible to use the 
selected IC with an inductor with higher inductance if it is still in the recommended range. A higher inductance 
reduces the ripple current and therefore increases the maximum output current with the selected IC.
If the calculated value is above the maximum output current of the application, the maximum switch current in 
the system is calculated:
L
SW(max)
OUT(max)
ΔI
Application specific maximum switch current: I
=
+ I
2
(4)
ΔIL = inductor ripple current calculated in Equation 2
IOUT(max) = maximum output current necessary in the application
This is the peak current, the inductor, the integrated switch(es), and the external diode have to withstand.
3 Inductor Selection
Data sheets often give a range of recommended inductor values. If this is the case, choose an inductor from this 
range. The higher the inductor value, the higher is the maximum output current because of the reduced ripple 
current.
In general, the lower the inductor value, the smaller is the solution size. Note that the inductor must always have 
a higher current rating than the maximum current given in Equation 4; this is because the current increases with 
decreasing inductance.
For parts where no inductor range is given, the following equation is a good estimation for the right inductor:
(
)
OUT
IN
OUT
L
S
IN
V
×
V
V
L =
ΔI
V
-
´
´
f
(5)
VIN = typical input voltage
VOUT = desired output voltage
fS = minimum switching frequency of the converter
ΔIL = estimated inductor ripple current, see the following:
The inductor ripple current cannot be calculated with Equation 1 because the inductor is not known. A good 
estimation for the inductor ripple current is 20% to 40% of the output current.
L
OUT(max)
ΔI
= (0.2 to 0.4)
I
´
(6)
ΔIL = estimated inductor ripple current
IOUT(max) = maximum output current necessary in the application
www.ti.com
Inductor Selection
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Basic Calculation of a Buck Converter's Power Stage
3
Copyright © 2026 Texas Instruments Incorporated


---

4 Rectifier Diode Selection
To reduce losses, use Schottky diodes. The forward current rating needed is equal to the maximum output 
current:
(1
)
F
OUT(max)
I
= I
´
- D
(7)
IF = average forward current of the rectifier diode
IOUT(max) = maximum output current necessary in the application
Schottky diodes have a much higher peak current rating than average rating. Therefore the higher peak current 
in the system is not a problem.
The other parameter that has to be checked is the power dissipation of the diode. It has to handle:
D
F
F
P
= I
V
´
(8)
IF = average forward current of the receiver diode
VF = forward voltage of the rectified diode
D = duty cycle calculated in Equation 1
5 Output Voltage Setting
Almost all converters set the output voltage with a resistive divider network (which is integrated if they are fixed 
output voltage converters).
With the given feedback voltage, VFB, and feedback bias current, IFB, the voltage divider can be calculated.
R1
R2
IR1/2
IFB
VOUT
VFB
Figure 5-1. Resistive Divider for Setting the Output Voltage
The current through the resistive divider needs to be at least 100 times as big as the feedback bias current:
R1/2
FB
I
100
I
³
´
(9)
IR1/2 = current through the resistive divider to GND
IFB = feedback bias current from data sheet
This adds less than 1% inaccuracy to the voltage measurement and for the calculation of the feedback divider, 
the current into the feedback pin can be neglected. The current also can be a lot higher. The only disadvantage 
of smaller resistor values is a higher power loss in the resistive divider, but the accuracy is increased a little.
With the preceding assumption, the resistors are calculated as follows:
FB
2
R1/2
V
R
= I
(10)
Rectifier Diode Selection
www.ti.com
4
Basic Calculation of a Buck Converter's Power Stage
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Copyright © 2026 Texas Instruments Incorporated


---

OUT
1
2
FB
V
R = R
1
V
æ
ö
´
-
ç
÷
è
ø
(11)
R1,R2 = resistive divider, see Figure 5-1.
VFB = feedback voltage from the data sheet
IR1/2 = current through the resistive divider to GND, calculated in Equation 9
VOUT = desired output voltage
6 Input Capacitor Selection
The minimum value for the input capacitor is normally given in the data sheet. This minimum value is necessary 
to stabilize the input voltage due to the peak current requirement of a switching power supply. The best practice 
is to use low-equivalent series resistance (ESR) ceramic capacitors. The dielectric material must be X5R or 
better. Otherwise, the capacitor loses much of its capacitance due to dc bias or temperature.
The value can be increased if the input voltage is noisy.
7 Output Capacitor Selection
The best practice is to use low-ESR capacitors to minimize the ripple on the output voltage. Ceramic capacitors 
are a good choice if the dielectric material is X5R or better.
If the converter has external compensation, any capacitor value above the recommended minimum in the data 
sheet can be used, but the compensation has to be adjusted for the used output capacitance.
With internally compensated converters, the recommended inductor and capacitor values must be used, or the 
recommendations in the data sheet for adjusting the output capacitors to the application in the data sheet must 
be followed for the ratio of L × C.
With external compensation, the following equations can be used to adjust the output capacitor values for a 
desired output voltage ripple:
L
OUT(min)
S
OUT
ΔI
C
=
8
× ΔV
´ f
(12)
COUT(min) = minimum output capacitance
ΔIL = estimated inductor ripple current
fS = minimum switching frequency of the converter
ΔVOUT = desired output voltage ripple
The ESR of the output capacitor adds some more ripple, given with the equation:
OUT(ESR)
L
ΔV
= ESR
ΔI
´
(13)
ΔVOUT(ESR) = additional output voltage ripple due to capacitors ESR
ESR = equivalent series resistance of the used output capacitor
ΔIL = inductor ripple current from Equation 2 or Equation 6
Often the selection of the output capacitor is not driven by the steady-state ripple, but by the output transient 
response. The output voltage deviation is caused by the time it takes the inductor to catch up with the increased 
or reduced output current needs.
The following formula can be used to calculate the necessary output capacitance for a desired maximum 
overshoot:
2
OUT
OUT(min),OS
OUT
OS
ΔI
L
C
= 2
V
V
´
´
´
(14)
COUT(min),OS = minimum output capacitance for a desired overshoot
www.ti.com
Input Capacitor Selection
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Basic Calculation of a Buck Converter's Power Stage
5
Copyright © 2026 Texas Instruments Incorporated


---

ΔIOUT = maximum output current change in the application
VOUT = desired output voltage
VOS = desired output voltage change due to the overshoot
8 References
1.
Understanding Buck Power Stages in Switchmode Power Supplies (SLVA057)
2.
Examples of Applications with the Pulse Width Modulator TL5001 (SLVAE05)
3.
Understanding Output Voltage Limitations of DC/DC Buck Converters (SLYT293)
4.
Designing Ultrafast Loop Response With Type-III Compensation for Current Mode Step-Down Converters 
(SLVA352)
5.
Robert W. Erickson: Fundamentals of Power Electronics, Kluwer Academic Publishers, 1997
6.
Mohan/Underland/Robbins: Power Electronics, John Wiley & Sons Inc., Second Edition, 1995
7.
George M. Harayda, Akira Omi, and Axel Yamamoto: Improve Your Designs with Large Capacitance Value 
Multi-Layer Ceramic Chip ( MLCC ) Capacitors, Panasonic
8.
Jeffrey Cain, Ph.D.: Comparison of Multilayer Ceramic and Tantalum Capacitors, AVX Corporation
9 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision B (August, 2015) to Revision C (October, 2026)
Page
•
Updated the numbering format for tables, figures, and cross-references throughout the document ................ 1
Changes from Revision A (August 2012) to Revision B (August 2015)
Page
•
Changed equation 1 and supporting text in Calculate the Maximum Switch Current section............................ 2
References
www.ti.com
6
Basic Calculation of a Buck Converter's Power Stage
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Copyright © 2026 Texas Instruments Incorporated


---

A Formulas to Calculate the Power State of a Buck Converter
(max)
OUT
IN
V
η
Maximum Duty Cycle: D =
V
´
(15)
VIN(max) = maximum input voltage
VOUT = output voltage
η = efficiency of the converter, e.g., estimated 85%
(
)
IN(max)
OUT
L
S
V
V
D
Inductor Ripple Current: ΔI
=
L
-
´
´
f
(16)
VIN(max) = maximum input voltage
VOUT = desired output voltage
D = duty cycle calculated in Equation 15
fS = minimum switching frequency of the converter
L = selected inductor value
L
MAXOUT
LIM(min)
ΔI
Maximum output current of the selected IC: I
= I
2
-
(17)
ILIM(min) = minimum value of the current limit of the integrated switch (given in the data sheet)
ΔIL = inductor ripple current calculated in Equation 16
L
SW(max)
OUT(max)
ΔI
Application specific maximum switch current: I
=
+ I
2
(18)
ΔIL = inductor ripple current calculated in Equation 16
IOUT(max) = maximum output current necessary in the application
OUT
IN
OUT
L
S
IN
V
(V
V
)
Inductor Calculation: L=
(if no value is recommended in the data sheet)
ΔI
V
´
-
´
´
f
(19)
VIN = typical input voltage
VOUT = desired output voltage
fS = minimum switching frequency of the converter
ΔIL= estimated inductor ripple current, see next paragraph
L
OUT(max)
Inductor Ripple Current Estimation: ΔI =(0.2 to 0.4)
I
´
(20)
ΔIL = estimated inductor ripple current
IOUT(max) = maximum output current necessary in the application
(1
)
F
OUT(max)
Average Forward Current of Rectifier Diode: I
= I
´
- D
(21)
IOUT(max) = maximum output current necessary in the application
D = duty cycle calculated in Equation 1
D
F
F
Power Dissipation in Rectifier Diode: P
= I
V
´
(22)
IF = average forward current of the rectifier diode
VF = forward voltage of the rectifier diode
www.ti.com
Formulas to Calculate the Power State of a Buck Converter
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Basic Calculation of a Buck Converter's Power Stage
7
Copyright © 2026 Texas Instruments Incorporated


---

D = duty cycle calculated in Equation 1
R1/2
FB
Current through Resistive Divider Network for Output Voltage Setting: I
100
I
³
´
(23)
IFB = feedback bias current from data sheet
FB
2
R1/2
V
Value of Resistor Between FB Pin and GND: R
= I
(24)
OUT
OUT
1
2
FB
V
Value of Resistor Between FB Pin and V
: R = R
1
V
æ
ö
´
-
ç
÷
è
ø
(25)
VFB = feedback voltage from the data sheet
IR1/2 = current through the resistive divider to GND, calculated in Equation 23
VOUT = desired output voltage
L
OUT(min)
S
OUT
ΔI
Minimum Output Capacitance, if not given in Data Sheet: C
= 8
× ΔV
´ f
(26)
ΔIL = estimated inductor ripple current
fS = minimum switching frequency of the converter
ΔVOUT = desired output voltage ripple
OUT(ESR)
L
Additional Output Voltage Ripple due to ESR: ΔV
= ESR
ΔI
´
(27)
ESR = equivalent series resistance of the used output capacitor
IOUT(max) = maximum output current of the application
ΔIL = inductor ripple current from Equation 16 or Equation 20
2
OUT
OUT(min),OS
OUT
OS
ΔI
L
Output Voltage Overshoot due to Load Transient: C
= 2 × V
V
´
´
(28)
ΔIOUT = maximum output current change in the application
Vout = desired output voltage
VOS = desired output voltage change due to the overshoot
Formulas to Calculate the Power State of a Buck Converter
www.ti.com
8
Basic Calculation of a Buck Converter's Power Stage
SLVA477C – DECEMBER 2011 – REVISED SEPTEMBER 2026
Submit Document Feedback
Copyright © 2026 Texas Instruments Incorporated


---

IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE 
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” 
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY 
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD 
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate 
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable 
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an 
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license 
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully 
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TI’s products are provided subject to TI’s Terms of Sale, TI’s General Quality Guidelines, or other applicable terms available either on 
ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable 
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products 
are standard, catalog, general purpose devices.
TI objects to and rejects any additional or different terms you may propose.
IMPORTANT NOTICE
Copyright © 2026, Texas Instruments Incorporated
Last updated 10/2025
