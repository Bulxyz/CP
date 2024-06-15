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

# Plot the data and the linear fit
plt.figure(figsize=(8, 6))
plt.plot(x, T, 'bo-', label='Data')
plt.plot(x, intercept + slope*x, 'r--', label='Linear Fit: T(x) = {:.2f} + {:.2f}x'.format(intercept, slope))
plt.xlabel('Distance, x (cm)')
plt.ylabel('Temperature, T (°C)')
plt.title('Temperature vs. Distance along a Metal Rod')
plt.legend()
plt.grid()
plt.show()
