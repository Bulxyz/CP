import numpy as np
import matplotlib.pyplot as plt

def m(t):
    return 1 - np.tanh(1/t)

# Create a range of temperatures
t = np.linspace(0.1, 2, 100)

# Calculate the corresponding magnetization
m_values = m(t)

# Create a plot
plt.figure(figsize=(8, 6))
plt.plot(t, m_values)
plt.xlabel("Reduced Temperature (t)")
plt.ylabel("Reduced Magnetization (m(t))")
plt.title("Reduced Magnetization vs. Reduced Temperature")
plt.grid()
plt.show()
