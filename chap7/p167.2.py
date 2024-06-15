import numpy as np
from scipy.optimize import curve_fit

# Data points
x = np.array([0, 1, 2, 3])
y = np.array([1, 3, 7, 15])

# Transform the data
x_squared = x**2
y_log = np.log(y)

# Perform linear regression
a, b = np.polyfit(x_squared, y_log, 1)

# Recover the original parameters
A = np.exp(a)
b = b

print(f"A = {A:.2f}")
print(f"b = {b:.2f}")

# Calculate the fitted values
y_fit = A * np.exp(-b * x**2)

# Calculate the chi-square value
residuals = y - y_fit
chi_square = np.sum((residuals / y)**2)
print(f"Chi-square value: {chi_square:.2f}")
