import numpy as np
import matplotlib.pyplot as plt

# Extract the data from the table
r = np.array([0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, 0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2.0, 2.0, 2.0, 2.0])
v = np.array([170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090])

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(r, v, 'bo-')
plt.xlabel('Distance, r (Mpc)')
plt.ylabel('Radial Velocity, v (km/s)')
plt.title('Distance vs. Radial Velocity for 24 Extragalactic Nebulae')
plt.grid()
plt.show()
