import numpy as np
from gnuradio import gr
import sys

# GNU Radio'nun yolu bulması için masaüstü klasörünü ekliyoruz
sys.path.append(r"C:\Users\Duygu\Desktop\awgn_project")
import awgn_band 

class blk(gr.decim_block):
    def __init__(self, sample_rate=32000.0, num_samples=65536, center_freqs=[5000, 10000], bandwidths=[1000, 1000]):
        # GNU Radio 3.8+ ve sonraki modern sürümler için güvenli decimation bloğu başlatma yöntemi
        gr.decim_block.__init__(
            self,
            name='Multi-band AWGN Gen',
            in_sig=None,
            out_sig=[(np.complex64, num_samples)],
            decim=1 # Eksik olan ve hataya sebep olan parametre buydu!
        )
        self.sample_rate = sample_rate
        self.num_samples = num_samples
        self.center_freqs = center_freqs
        self.bandwidths = bandwidths

    def work(self, input_items, output_items):
        # Orijinal awgn_band.py dosyasındaki fonksiyonu çağırıyoruz
        filtered_noise = awgn_band.generate_awgn(self.sample_rate, self.num_samples, self.center_freqs, self.bandwidths)
        output_items[0][:] = filtered_noise
        return len(output_items[0])