import numpy as np
import matplotlib.pyplot as plt
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
sigma = np.sqrt(variance)

# Compute the chi-square
chi_square = np.sum(((T - T_fit) / sigma)**2)
dof = len(x) - 2  # Degrees of freedom
print(f"Chi-square: {chi_square:.2f}")
print(f"Degrees of freedom: {dof}")
print(f"Chi-square per degree of freedom: {chi_square / dof:.2f}")

# Interpret the chi-square value
if chi_square / dof < 1:
    print("The fit is good, as the chi-square per degree of freedom is less than 1.")
else:
    print("The fit is not as good, as the chi-square per degree of freedom is greater than 1.")
