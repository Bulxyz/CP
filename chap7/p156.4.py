import numpy as np
import matplotlib.pyplot as plt

# Extract the data from the figure
t = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
N = np.array([36, 26, 19, 15, 10, 9, 7, 6, 4, 3, 3, 2, 1])

# Calculate the natural logarithm of the number of decays
ln_N = np.log(N)

# Perform linear regression
A = np.vstack([t, np.ones(len(t))]).T
m, b = np.linalg.lstsq(A, ln_N, rcond=None)[0]

# Calculate the lifetime τ
tau = -1 / m

print(f"Calculated lifetime τ: {tau:.2f} ns")
print(f"Tabulated lifetime of the pion: 26 ns")

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, N, 'bo-', label='Data')
plt.plot(t, np.exp(b) * np.exp(m * t), 'r--', label='Fit')
plt.xlabel('t [ns]')
plt.ylabel('N(t)')
plt.title('Exponential Decay of π Meson')
plt.legend()
plt.grid()
plt.show()
