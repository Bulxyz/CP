import numpy as np
import matplotlib.pyplot as plt

def equation(EB):
    return np.sqrt(EB) * (1 / np.tan(np.sqrt(10 - EB))) - np.sqrt(10 - EB)

# Plot the equation
EB_values = np.linspace(0.1, 9.9, 100)  # Avoiding EB = 0 and EB = 10 to prevent division by zero
f_values = equation(EB_values)

plt.plot(EB_values, f_values)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('EB')
plt.ylabel('f(EB)')
plt.title('Plot of sqrt(E) * cot(sqrt(10 - E)) - sqrt(10 - E) = 0')
plt.grid(True)
plt.show()
