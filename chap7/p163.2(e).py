import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Extract the data from Table 7.2
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
T = np.array([14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9])

# Perform the linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, T)

print(f"Slope (b): {slope:.2f}")
print(f"Intercept (a): {intercept:.2f}")
print(f"R-squared: {r_value**2:.2f}")
print(f"Standard error: {std_err:.2f}")

# Compute the variance
T_fit = intercept + slope * x
residuals = T - T_fit
variance = np.sum(residuals**2) / (len(x) - 2)
print(f"Variance: {variance:.2f}")

# Compute the deviation of the fit from the data
dev_from_fit = np.abs(T - T_fit)
print(f"Deviation from fit: {dev_from_fit}")

# Verify that about one-third of the points miss the σ error band
num_outside_sigma = np.sum(dev_from_fit > std_err)
print(f"Number of points outside the σ error band: {num_outside_sigma} out of {len(x)}")
print(f"Percentage of points outside the σ error band: {num_outside_sigma / len(x) * 100:.2f}%")
