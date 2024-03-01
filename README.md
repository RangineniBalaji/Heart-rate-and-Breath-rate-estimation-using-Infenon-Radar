# Heart rate and Breath rate Estimation using radar data

## Introduction
This repository contains the implementation details and results of radar-based physiological monitoring for enhancing safety and health monitoring in autonomous vehicles. By leveraging radar data, this project aims to estimate heart rate and breath rate of passengers, contributing to safety enhancement and health monitoring within autonomous vehicle environments.

## Safety Enhancement
The ability to estimate heart rate and breath rate using radar data can significantly contribute to enhancing safety in autonomous vehicles. By continuously monitoring vital signs, the vehicle can detect signs of distress or health issues, enabling appropriate actions such as alerting the passenger or adjusting driving parameters.

## Health Monitoring
Integrating health monitoring capabilities into autonomous vehicles aligns with the broader trend of incorporating wellness and healthcare features into smart technologies. This enhances the passenger experience and opens up new avenues for partnerships with healthcare providers and insurers.

## Methodology
### Logarithmic Scaling
We applied logarithmic scaling to the radar data by taking the absolute values of the raw complex data and then applying the natural logarithm function. This process helped enhance the data's suitability for analysis.

### Frame Formation
The raw data, initially in complex form, was reshaped into 450 frames, each containing 16,384 data points. This framing facilitated further analysis and processing of the radar data.

### Breath Rate Estimation
To estimate breath rate, we combined every 5 frames using the mean operation. This aggregation method accounts for the relatively stable nature of breath rate, typically ranging from 12 to 30 breaths per minute.

### Heart Rate Estimation
For heart rate estimation, we utilized the entire set of 450 frames without combining. This decision was made considering the potential variability in heart rate, which can range up to 110 beats per minute, requiring a more granular analysis.

### Threshold Identification
- **Heart Rate Threshold**: Through manual analysis of plotted graphs sampled every 200 frames, we identified a clear threshold for heart rate estimation. The threshold for heart rate was determined to be above 600 beats per minute.
- **Breath Rate Threshold**: By visually inspecting the sampled graphs, we established a distinct threshold range for breath rate estimation, falling within the range of 200 to 300 breaths per minute.
  ![image](https://github.com/RangineniBalaji/Heart-rate-and-Breath-rate-estimation-using-Infenon-Radar/assets/83932925/011ca1da-6d06-412c-8268-c723c866b0ef)


### Threshold-based Filtering
Our algorithm identifies relevant physiological signals by counting data points that exceed or fall within established heart rate and breath rate thresholds.

### Threshold-based Peak Identification
We refine peak identification by computing the average value of data points within the identified threshold range, facilitating accurate detection of physiological peaks.

### Peak Detection
Based on chucking signals within each chunk, peaks are detected using the signal's mean value as a threshold.

### Calculating Time Differences
Time differences between consecutive peaks within each chunk are computed.

### Estimating Heart Rate and Breath Rate
Heart rate and breath rate are estimated from the mean time difference between peaks, converted to beats per minute.

## Results
### Heart Rates Array (60sec)
[80 84 84 80 86 93 89 70 85 80 80 83 91 88 105 90 105 88 95 92 93 105 82 104 120 88 95 75 105 90 89 85 70 82 80 70 100 92 108 96 83 101 113 87 95 90 91 90 90 90 90 90 84 96 90 93]

### Breath Rates Array (60sec)
[0, 0, 0, 0, 12, 12, 12, 15, 15, 15, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 17, 17, 17, 17, 17, 17, 19, 19, 20, 20, 20, 20, 20, 20, 19, 19, 19, 19, 19, 19, 19, 19, 19, 23, 23, 23, 23, 23, 24, 24, 24, 30, 30, 30, 0, 0, 0, 0, 0]

![image](https://github.com/RangineniBalaji/Heart-rate-and-Breath-rate-estimation-using-Infenon-Radar/assets/83932925/8a1b5d15-ca0d-4f9d-af40-970cd380b364)


## Conclusion
Radar-based physiological monitoring offers promising avenues for enhancing safety and health monitoring in autonomous vehicles. By accurately estimating heart rate and breath rate, potential health issues can be detected early, leading to improved passenger safety and well-being. Further refinement and validation of the proposed methodology are warranted to ensure its reliability and effectiveness in real-world applications.
