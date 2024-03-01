import numpy as np

def impute_values(rate_array, threshold):
    rate_array = np.array(rate_array)

    for i in range(len(rate_array)):
        if rate_array[i] < threshold:
            left_indices = np.where(rate_array[:i] > threshold)[0][-2:]
            right_indices = np.where(rate_array[i+1:] > threshold)[0][:2] + i + 1
            indices = np.concatenate((left_indices, right_indices))
            replacement_value = np.mean(rate_array[indices])
            rate_array[i] = replacement_value

    return rate_array
