# Heart Rate and Breath Rate Estimation using Infineon Radar

This project aims to estimate heart rate and breath rate using data from an Infineon radar. It consists of several Python files, each serving a specific purpose in the data processing, analysis, and rate estimation pipeline.

## Files Overview
1. **main.py**: This is the main script that orchestrates the entire process. It loads data from the radar, preprocesses it, calculates breath rate and heart rate, and visualizes the results.
2. **data_processing.py**: This module contains functions for loading, scaling, and reshaping radar data. It prepares the raw data for further analysis.
3. **rate_estimation.py**: Here, the heart rate and breath rate are estimated using signal processing techniques. The main function `estimate_rate()` calculates the rates based on peak detection in the signal.
4. **averaging.py**: This module implements averaging techniques to smoothen the rate estimates. The `find_average()` function computes the average rate over fixed time intervals.
5. **imputation.py**: In this file, missing or unreliable rate values are imputed using neighboring values. The `impute_values()` function replaces low-confidence values with the average of adjacent reliable values.
6. **analysis.py**: This module provides functions for analyzing radar data. Functions like `count_points_above_threshold()` and `calculate_mean_values()` are used for preprocessing and data analysis.

## Usage
To run the project:
1. Ensure you have Python installed.
2. Install the required dependencies.
3. Place your radar data file (`data1.raw.bin`) in the project directory.
4. Execute `main.py` to process the data and visualize the estimated heart rate and breath rate.

## Dependencies
- NumPy
- Matplotlib
- SciPy

## Identifying Thresholds
To identify thresholds for heart rate and breath rate estimation, visual analysis was performed on the radar data. This process was documented in the `main_vital_sign.ipynb` Jupyter Notebook, which contains both the code and visualizations of the identified thresholds.

### Steps:
1. **Loading Data**: The raw radar data (`data1.raw.bin`) was loaded into the notebook.
2. **Data Preprocessing**: The data was scaled and reshaped to prepare it for analysis.
3. **Threshold Identification**: Visualizations of the radar data were created to identify appropriate thresholds for heart rate and breath rate estimation.
4. **Breath Rate Threshold**: A threshold of 600 was chosen for breath rate estimation based on the visual analysis.
5. **Heart Rate Threshold**: The heart rate threshold was determined by analyzing the mean values of counts within a specific range of values in the radar data.

For detailed steps and visualizations, refer to the [main_vital_sign.ipynb](main_vital_sign.ipynb) notebook.

