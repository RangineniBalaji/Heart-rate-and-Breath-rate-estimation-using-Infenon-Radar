import numpy as np
from scipy.signal import find_peaks

def estimate_rate(signal, threshold, frame_rate):
    rate_list = []

    for i in range(len(signal)):
        start_index = i * 1  
        end_index = start_index + 25

        window_signal = signal[start_index:end_index]
        peaks, _ = find_peaks(window_signal, height=threshold)

        time_diffs = np.diff(peaks) / frame_rate

        rate = 60 / np.mean(time_diffs) if len(time_diffs) > 0 else 0
        rate_list.append(int(np.ceil(rate)))
    return rate_list
