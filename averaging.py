import numpy as np
def find_average(signal):
    threshold = np.mean(signal)
    averaged = []

    for i in range(60):
        start_index = i * int(len(signal) / 60)  # Divide the total length by 60 for a 60-second interval
        end_index = start_index + int(len(signal) / 60)  # Divide the total length by 60 for a 60-second interval

        # Extract the subset of the signal within the window
        window_signal = signal[start_index:end_index]

        # Average the values within the window to get a single value
        averaged_value = np.mean(window_signal)

        # Append the averaged value to the breath rates array
        averaged.append(averaged_value)
    return averaged