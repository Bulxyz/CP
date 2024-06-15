import numpy as np
from scipy import stats

# Extract the data from Table 7.3
r = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, 0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2.0, 2.0, 2.0, 2.0])
v = np.array([170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090])

# Perform the linear regression with the two-sided alternative
slope, intercept, r_value, p_value, std_err = stats.linregress(r, v, alternative='two-sided')

print(f"Slope (H): {slope:.2f}")
print(f"Intercept (a): {intercept:.2f}")
print(f"R-squared: {r_value**2:.2f}")
print(f"Standard error: {std_err:.2f}")

# Calculate the variance of the data
v_mean = np.mean(v)
variance = np.sum((v - v_mean)**2) / (len(v) - 1)
print(f"Variance of the data: {variance:.2f}")

# Calculate the deviation of the fit from the data
v_fit = intercept + slope * r
deviation = np.sum(((v - v_fit) / np.sqrt(variance))**2) / (len(v) - 2)
print(f"Deviation of the fit from the data: {deviation:.2f}")

# Calculate the variances and standard errors of the slope and intercept
r_mean = np.mean(r)
sigma_a_sq = deviation * np.sum(r**2) / (len(r) * np.sum((r - r_mean)**2))
sigma_b_sq = deviation / np.sum((r - r_mean)**2)

sigma_a = np.sqrt(sigma_a_sq)
sigma_b = np.sqrt(sigma_b_sq)

print(f"Variance of the slope (σ_a^2): {sigma_a_sq:.2f}")
print(f"Variance of the intercept (σ_b^2): {sigma_b_sq:.2f}")
print(f"Standard error of the slope (σ_a): {sigma_a:.2f}")
print(f"Standard error of the intercept (σ_b): {sigma_b:.2f}")

# Interpret the results
if sigma_a < abs(slope) and sigma_b < abs(intercept):
    print("The standard errors of the slope and intercept are reasonably small compared to their values, so it makes sense to use them as the errors in the deduced values.")
else:
    print("The standard errors of the slope and intercept are large compared to their values, which may indicate that the model does not fit the data well or that the uncertainties in the data are underestimated.")
