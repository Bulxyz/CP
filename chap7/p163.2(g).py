import numpy as np
from scipy import stats

# Extract the data from Table 7.2
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
T = np.array([14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9])

# Perform the linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, T)

# Compute the variance
T_fit = intercept + slope * x
residuals = T - T_fit
variance = np.sum(residuals**2) / (len(x) - 2)

# Compute the variances of the slope and intercept
mean_x = np.mean(x)
sum_sq_x = np.sum((x - mean_x)**2)
sigma_a_sq = variance * (1/len(x) + mean_x**2 / sum_sq_x)
sigma_b_sq = variance / sum_sq_x

print(f"Variance of the intercept (σa^2): {sigma_a_sq:.2f}")
print(f"Variance of the slope (σb^2): {sigma_b_sq:.2f}")
print(f"Standard error of the intercept (σa): {np.sqrt(sigma_a_sq):.2f}")
print(f"Standard error of the slope (σb): {np.sqrt(sigma_b_sq):.2f}")
