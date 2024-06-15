import numpy as np
import matplotlib.pyplot as plt
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

# Calculate the variance of the data
v_mean = np.mean(v)
variance = np.sum((v - v_mean)**2) / (len(v) - 1)
print(f"Variance of the data: {variance:.2f}")

# Calculate the deviation of the fit from the data
v_fit = intercept + slope * r
deviation = np.sum((v - v_fit)**2) / (len(v) - 2)
print(f"Deviation of the fit from the data: {deviation:.2f}")

# Count the number of points outside the σ error band
num_outside = np.sum(np.abs(v - v_fit) > std_err)
print(f"Number of points outside the σ error band: {num_outside}")
print(f"Fraction of points outside the σ error band: {num_outside / len(v):.2f}")

# Plot the data and the linear fit
plt.figure(figsize=(8, 6))
plt.plot(r, v, 'bo', label='Data')
plt.plot(r, intercept + slope*r, 'r--', label='Linear Fit: v(r) = {:.2f} + {:.2f}r'.format(intercept, slope))
plt.xlabel('Distance, r (Mpc)')
plt.ylabel('Radial Velocity, v (km/s)')
plt.title('Distance vs. Radial Velocity for 24 Extragalactic Nebulae')
plt.legend()
plt.grid()
plt.show()
