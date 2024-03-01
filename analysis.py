import numpy as np

def count_points_above_threshold(data, threshold):
    count_greater_than_threshold = np.sum(data > threshold, axis=1)
    return count_greater_than_threshold

def calculate_mean_values(count_array, window_size):
    mean_values = np.mean(count_array.reshape(-1, window_size), axis=1)
    return mean_values

def count_values_within_threshold(data, threshold_lower, threshold_upper):
    count_within_threshold = np.sum((data > threshold_lower) & (data < threshold_upper), axis=1)
    return count_within_threshold
