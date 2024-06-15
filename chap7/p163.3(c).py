import numpy as np
from scipy import stats

# Extract the data from Table 7.3
r = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, 0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2.0, 2.0, 2.0, 2.0])
v = np.array([170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090])

# Perform the linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(r, v)

print(f"Slope (H): {slope:.2f}")
print(f"Intercept (a): {intercept:.2f}")
print(f"R-squared: {r_value**2:.2f}")
print(f"Standard error: {std_err:.2f}")
