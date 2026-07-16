# Multi-band AWGN Generator (GNU Radio Companion)

This repository contains a GNU Radio Companion mini-project that generates and compares multi-band Additive White Gaussian Noise (AWGN) using two completely distinct methodologies: traditional time-domain filtering and direct frequency-domain spectral masking via a custom Embedded Python Block.

## 📌 Project Overview
In Software Defined Radio (SDR) and digital signal processing systems, isolating specific frequency bands with noise or signals is a fundamental task. This project benchmarks:
1. **The Classic Approach:** Broad-spectrum white noise shaped by cascaded time-domain filters.
2. **The Modern Python Approach:** A single, custom Embedded Python Block that mathematically designs noise bands directly in the frequency domain before computing the IFFT.

---

## ⚙️ Flowgraph Architecture

The GNU Radio Companion (GRC) flowgraph runs two parallel processing paths synchronized into a single **QT GUI Frequency Sink** for clear, real-time spectrum comparison:

### 1. Classic Filter-Based Path (Top - `in0`)
* **Dataflow:** `Noise Source (Gaussian)` ➔ `Throttle` ➔ Split into `Low Pass Filter` & `Band Pass Filter` ➔ Combined via `Add` ➔ `in0`.
* **Characteristics:** Mimics physical hardware circuitry. Due to the nature of time-domain filter taps, it exhibits realistic, sloped transition bands (smooth roll-offs).

### 2. Custom Python Block Path (Bottom - `in1`)
* **Dataflow:** `Multi-band AWGN Gen (Embedded Python)` ➔ `Throttle (Complex Vector)` ➔ `Vector to Stream` ➔ `in1`.
* **Characteristics:** Generates noise directly in the frequency domain by creating sharp mathematical masks at targeted bins. This yields near-ideal, perfectly sharp **"brick-wall"** spectral edges.

---

## 📊 Shared Variables & Parameters

The system is configured using the following exact parameters defined within the GRC flowgraph variables:

| Variable ID | Value | Description |
| :--- | :--- | :--- |
| `samp_rate` | `32000` | System sampling rate (32 kHz) |
| `num_samples` | `65536` | FFT Size / Vector length for processing |
| `center_frequency` | `[5k, 10k, 15k]` | Targeted center frequencies for custom noise |
| `bandwidth` | `[3k, 1k, 3k]` | Target bandwidths allocated for each custom band |

---

## 📈 Expected Output (Spectrum Analysis)

Upon executing the flowgraph, the **QT GUI Frequency Sink** plot highlights the architectural differences:
* **Blue Line (`Data 0`):** Features a central low-pass noise block and an asymmetrical band-pass peak around $7.5 \text{ kHz}$ with standard filter sloped edges.
* **Red Line (`Data 1`):** Showcases three perfectly distinct, rectangular noise islands centered precisely at $5 \text{ kHz}$, $10 \text{ kHz}$, and $15 \text{ kHz}$ with razor-sharp vertical transitions.

---

## 🚀 Repository File Structure & Setup
Your local project directory contains:
* `multiband_awgn.grc` (The GNU Radio Companion flowgraph file)
* `awgn_band.py` (The custom core Python function)
* `README.md` (This documentation file)

### How to Run:
1. Open **GNU Radio Companion**.
2. Load the `multiband_awgn.grc` file.
3. Ensure your custom script path inside the Embedded Python Block is correctly linked.
4. Press **F6** or click **Execute** to see the live spectrum display.
