# Multi-band AWGN Generator (GNU Radio Companion)

This project is a GNU Radio Companion (GRC) simulation that explores two distinct methodologies for generating Multi-band Additive White Gaussian Noise (AWGN). It benchmarks a traditional time-domain filtering approach against a direct frequency-domain spectral masking method using a custom Embedded Python Block.

---

## What Does This Project Do and Where Is It Used?

In real-world communication channels (like wireless links or fiber optic cables), signals never travel in a vacuum—they are constantly degraded by noise. To test the resilience, Bit Error Rate (BER), and Signal-to-Noise Ratio (SNR) of a receiver system in a controlled lab environment, we need a reliable way to generate synthetic noise.

This project serves as a practical stress-testing and simulation tool for several scenarios:
* **Channel Modeling:** Simulating noisy, multi-band interference environments to see how a communication system holds up.
* **SDR (Software Defined Radio) Benchmarking:** Testing how well physical or simulated receiver filters can isolate a signal when specific neighboring bands are flooded with noise.
* **Noise Cancellation and DSP Algorithms:** Providing a predictable baseline to validate algorithms designed to suppress or filter out targeted spectral noise.
* **Academic Evaluation:** Visually demonstrating the performance and spectral differences between time-domain (filter-based) and frequency-domain (mathematical mask-based) signal generation.

---

## Flowgraph Architecture

The GRC flowgraph runs two parallel processing paths synchronized into a single QT GUI Frequency Sink for real-time spectrum comparison:

### 1. Classic Filter-Based Path (Top - in0)
* **Dataflow:** Noise Source (Gaussian) -> Throttle -> Split into Low Pass Filter and Band Pass Filter -> Combined via Add -> in0.
* **Characteristics:** Mimics physical analog hardware circuitry. Due to the nature of time-domain filter taps, it exhibits realistic, sloped transition bands (smooth roll-offs).

### 2. Custom Python Block Path (Bottom - in1)
* **Dataflow:** Multi-band AWGN Gen (Embedded Python) -> Throttle (Complex Vector) -> Vector to Stream -> in1.
* **Characteristics:** Generates noise directly in the frequency domain by creating sharp mathematical masks at targeted bins before computing the IFFT. This yields near-ideal, perfectly sharp "brick-wall" spectral edges.

---

## Shared Variables and Parameters

The system is configured using the following exact parameters defined within the GRC flowgraph variables:

| Variable ID | Value | Description |
| :--- | :--- | :--- |
| samp_rate | 32000 | System sampling rate (32 kHz) |
| num_samples | 65536 | FFT Size / Vector length for processing |
| center_frequency | [5k, 10k, 15k] | Targeted center frequencies for custom noise |
| bandwidth | [3k, 1k, 3k] | Target bandwidths allocated for each custom band |

---

## Expected Output (Spectrum Analysis)

Upon executing the flowgraph, the QT GUI Frequency Sink plot highlights the architectural differences:
* **Blue Line (Data 0):** Features a central low-pass noise block and an asymmetrical band-pass peak around 7.5 kHz with standard filter sloped edges.
* **Red Line (Data 1):** Showcases three perfectly distinct, rectangular noise islands centered precisely at 5 kHz, 10 kHz, and 15 kHz with razor-sharp vertical transitions.

---

## Repository File Structure and Setup

### File Structure:
* multiband_awgn.grc (The GNU Radio Companion flowgraph file)
* awgn_band.py (The custom core Python function)
* README.md (This documentation file)

### How to Run:
1. Open GNU Radio Companion.
2. Load the `multiband_awgn.grc` file.
3. Ensure your custom script path inside the Embedded Python Block is correctly linked.
4. Press F6 or click Execute to see the live spectrum display.
