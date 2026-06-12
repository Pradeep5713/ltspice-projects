# RC Low-Pass Filter

## Circuit

| Component | Value |
|-----------|-------|
| R1 | 1 kΩ |
| C1 | 159 nF |
| V1 | AC 1 V |

## Calculated vs Simulated

| Parameter | Calculated | Simulated | Error |
|-----------|-----------|-----------|-------|
| Cutoff frequency (f_c) | 1001.0 Hz | 1000.0 Hz | 0.10% |
| Magnitude at f_c | −3.0 dB | -3.01 dB | — |

## Verification

**Result: PASS** — simulated cutoff is within 10% of theoretical value.

## Bode Plot

![Bode Magnitude](results/bode.png)

## Theory

$$f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi \times 1\,\text{k}\Omega \times 159\,\text{nF}} \approx 1001\,\text{Hz}$$
