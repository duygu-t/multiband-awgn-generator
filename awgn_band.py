"""
Multi-band AWGN Generator
Optimized for readability and GRC integration by Duygu Tüzün
"""

import numpy as np

def generate_awgn(sample_rate, num_samples, center_freqs, bandwidths):
    # Step 1: Generate raw complex white Gaussian noise (I/Q)
    noise = (np.random.normal(0, 1, num_samples) + 1j * np.random.normal(0, 1, num_samples))

    # Step 2: Transform raw noise to frequency domain (FFT)
    noise_fft = np.fft.fft(noise)
    frequency_axis = np.fft.fftfreq(num_samples, 1.0 / sample_rate)

    # Step 3: Map passbands to the filter mask
    filter_mask = np.zeros(num_samples, dtype=bool)

    for center_freq, bandwidth in zip(center_freqs, bandwidths):
        f_min = center_freq - bandwidth / 2.0
        f_max = center_freq + bandwidth / 2.0

        # Positive and negative (mirror) frequency ranges
        filter_mask |= (frequency_axis >= f_min) & (frequency_axis <= f_max)
        filter_mask |= (frequency_axis >= -f_max) & (frequency_axis <= -f_min)

    # Zero-out unsought frequencies
    noise_fft[~filter_mask] = 0

    # Step 4: Transform back to the time domain using IFFT
    filtered_noise = np.fft.ifft(noise_fft)
    return tuple(filtered_noise)