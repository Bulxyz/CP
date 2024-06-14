import numpy as np
import matplotlib.pyplot as plt

def equation(EB):
    epsilon = 1e-7  # small constant to avoid division by zero
    return np.sqrt(EB) * np.cos(np.sqrt(10 - EB)) / (np.sin(np.sqrt(10 - EB)) + epsilon) - np.sqrt(10 - EB)

EB_values = np.linspace(0, 10, 1000)
f_values = equation(EB_values)

# Plot the first 20 results
plt.plot(EB_values[:20], f_values[:20])
plt.xlabel('EB')
plt.ylabel('f(EB)')
plt.title('Plot of f(EB) for the first 20 values')
plt.grid(True)
plt.show()
