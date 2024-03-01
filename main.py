import numpy as np
import matplotlib.pyplot as plt
from data_processing import load_data, scale_data, reshape_data
from analysis import count_points_above_threshold, calculate_mean_values, count_values_within_threshold
from rate_estimation import estimate_rate
from imputation import impute_values
from averaging import find_average

# Load and preprocess data
data = load_data("data1.raw.bin")
scaled_data = scale_data(data)
reshaped_data = reshape_data(scaled_data)

# Breath Rate
BR_threshold = 600
count_array = count_points_above_threshold(reshaped_data, BR_threshold)
mean_values = calculate_mean_values(count_array, 5)
averaged = find_average(mean_values)
breath_rate_list = estimate_rate(averaged, np.mean(averaged), 1)

# Heart Rate
HR_threshold_lower = 200
HR_threshold_upper = 300
count_array = count_values_within_threshold(reshaped_data, HR_threshold_lower, HR_threshold_upper)
mean_values = calculate_mean_values(count_array, 2)
heart_rate_list = estimate_rate(np.ceil(mean_values), np.mean(mean_values), 4)
heart_rate_list = find_average(heart_rate_list)
heart_rate_list = impute_values(heart_rate_list, 60)

# Plotting
plt.plot(heart_rate_list, label="Heart Rate")
plt.plot(breath_rate_list, label="Breath Rate")
plt.title("Heart Rate and Breath Rate Estimation Over Time")
plt.xlabel("Time")
plt.ylabel("Rate")
plt.legend()
plt.show()

