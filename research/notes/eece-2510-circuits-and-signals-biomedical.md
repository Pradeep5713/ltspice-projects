---
title: 'EECE 2510 – Circuits and Signals: Biomedical'
id: eece-2510-circuits-and-signals-biomedical
tags:
- btech-ece-projects-259aee
- ltspice-tutorial
- ekg-biomedical
- active-filters
created: '2026-09-25T03:15:29.973857Z'
updated: '2026-09-25T03:16:26.764264Z'
source: https://ece.northeastern.edu/courses/eece2150/dimarzio/labs/Lab10_OpAmpFilterLTSpiceDesign-9-21.pdf
source_domain: ece.northeastern.edu
fetched_at: '2026-09-25T03:15:29.972961Z'
fetch_provider: builtin
status: draft
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Northeastern University EECE 2510 (Circuits and Signals: Biomedical Applications)
  Lab 10 handout: an LTspice-based active-filter design exercise built around an EKG
  signal chain. Students build a first-order active low-pass filter in LTspice using
  the LT1490 op-amp (Rf=100kOhm, Cf=10nF, Rs=20kOhm, +/-10V rails, RL=1kOhm), run
  an AC sweep (.ac dec 100 1 1000000) to find cutoff frequency and compare to the
  RC time constant prediction, then apply a 200Hz/0.5Vpp pulse source (transient analysis)
  to observe square-wave distortion and its frequency content via FFT. Repeats the
  exercise for a first-order active high-pass filter (Rs=100kOhm, Cs=10nF, Rf=200kOhm)
  to find in-band gain, fc, and explain roll-off at high frequency. Directly usable
  as a step-by-step LTspice tutorial/rubric for a B.Tech ECE biomedical (EKG amplifier/filter)
  project.'
raw_file: raw/eece-2510-circuits-and-signals-biomedical.pdf
---

EECE 2510 – Circuits and Signals: Biomedical
Applications
Lab 10, LTSpice Analysis of Active Filters
INTRODUCTION:
As discussed in class, Op-amps are useful building blocks in many sensing and 
measurement applications.  To measure the EKG signal, we will be using them to amplify
small signals, to reject common-mode signals, and to filter out unwanted low and high-
frequency noise and interference.
PART 1:  LTSPICE MODELING OF OP AMP CIRCUITS
Figure 1: First order active low pass filter for part 1
1.1
In LTSpice, use the LT1490 op-amp to build an active low pass filter shown in 
figure 1.  Use Rf=100kΩ ,Cf=10nF ,∧Rs=20kΩ.  Use +¿−10V DC power 
supplies for the op-amp and use an AC source to the input of the filter.  The load 
resistance RL=1k Ω
Some tips on starting/using PSpice:  
1. Run LTSpice 
2. New schematic
3. Save as, specify name and location – somewhere you have permission to write 
(desktop, for example).


---

4. OK
5. Special note:  m is 10
−3, M is also 10
−3, Meg is 10
6, meg is also 10
6 or 1e6 is 106.  
6. Add a standard voltage source, right click to edit, click advanced and enter the  
AC amplitude of the source. There is no need to change any other parameters.
1.2
Test the amplifier with an AC input with 0.1V amplitude and create a semilog 
plot of the response from 1 Hz to 1 MHz using the AC Sweep mode with a 
logarithmic frequency sweep. Set up the simulation as follows (using the 
simulate button and “edit simulation command” on Windows or by going to 
draft>spice directive on Mac). Set up the simulation for an ac analysis, by 
decade, 100 points/decade, from 1 Hz to 1,000,000Hz. The command shown on 
the schematic should be
             .ac dec 100 1 1000000
           (hint – use a voltage probe at the output of the op-amp to display the output 
voltage). You will need to right click on the left vertical axis to change to linear 
scale.  Right click on the right vertical axis to remove the phase plot. Note that 
this is the transfer function, H (ω), except that it is multiplied by 0.1 because the
input is 0.1V.  Q1: What is the cutoff frequency, f c, (the half power point, or 
where the voltage is 0.707 times the maximum output voltage)?  Is this what 
you expect, considering the value of the RC time constant? 
1.3
Q2: What happens if the amplitude of the input sinusoid is changed to 0.5V?
1.4
Time domain view of the filter response: Now a use a pulsed source to produce a
200 Hz square wave with 0.5V p-p and connect to the filter input.  Plot both the 
input and output voltages. Use transient analysis in this case, choose the interval
of the simulation to be about 10 cycles of the square waveform. A reasonable 
choice for the properties of the Pulse source is as follows
             PULSE(-.25 0.25 0 1u 1u 2.5ms 5ms 10)
Figure 2, periodic pulse wave form in LTSpice
V 1 (Vinitial)the voltage level at the start of the pulse
V 2 (Von) 
the voltage level at the peak of the 
pulse
Tdelay the time delay before the start of the pulse
Trise
          the pulse rise time
h
l
f ll i


---

V1 and V2 should be   −0.25V and +0.25 or 0V and 0.5V for a 0.5V p-p square wave. 
Tdelaycan be set to zero.  Trise and Tfall should be significantly smaller than the period,
perhaps 1-10 microseconds. If they are too small, LTSpice could take a long time to 
simulate, or it might not find a solution.  Tperiod is the total period of the pulse which 
should be double the value of Ton for a square wave that has equal times spent in the 
high and low voltage states. As before, use the simulation command on Windows or the 
spice directive on Mac to set up the simulation to transient analysis.
Q3: Use probes to plot both the input and the output voltages. Examine the output 
signal, save/print the output or sketch it in your lab-book and try to explain why the 
output wave looks as it does, rather than just being a square wave.  Try thinking in 
both the time and frequency domains when coming up with your answer. It may be 
helpful to use the FFT function to display the frequency components for both the 
input and output waves (you may have to do this in two windows). Change both the 
vertical and horizontal axis to linear scale and limit the horizontal axis if you like – 
displaying the FFT up to 5 kHz is about right.
Hint – it may help you see what is happening if you try using square waves with higher
and lower frequencies to see what the filter does (10x to 100x higher or lower, 
maybe).
1.5      Now, change your circuit so that it is an active high pass filter shown in Figure 3 
with RS=100kΩ ,CS = 10nF ,Rf=200kΩ and plot the filter response to an AC 
input from 1 Hz to 1 MHz. Q4: What are the in-band gain and f c of the circuit? 
Q5: Why does the output roll off at high frequencies, if this is a high-pass 
filter??
1.6
If you have time: Now use a pulsed source to produce a 200 Hz square wave 
with 0.5V amplitude and connect this to the filter input.  Plot both the input and
output voltages.  Q6: Examine the output signal, save the output plot or sketch 
it in your lab-book and try to explain why the output wave looks as it does, 
again thinking in both the time and frequency domains.


---

Hint – again it may help you see what is happening if you try inputting square 
waves with higher and lower frequencies (10x to 100x higher or lower, maybe).
Figure 3: First order active high pass filter for part 1
INSTRUCTIONS FOR THE WRITE-UP…
Please follow instructions for writing lab reports available on Canvas
IMPORTANT: BEFORE YOU LEAVE THE LAB:
a.
Place all of the components that your removed from the red tool box back in 
that box and return it to the cabinet that houses them
b. Collect all used components and wires from your bench and place them in 
your group’s reusable plastic container. If you are not going to use these 
components or wires again please discard them in the trash bin.
c.
Turn off all of the equipment you have used on your workbench.
d. Make sure you return your protoboard, the equipment wires and your 
reusable container to the front window.
e. Make sure to have your notebook signed by an instructor before you leave 
the lab.
Department of Electrical Engineering, Northeastern University.
Last updated: 8/23/2021/ I. Salama;2/28/16, N. McGruer; 
