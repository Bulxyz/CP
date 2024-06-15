import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def equation_even(EB):
    return np.sqrt(10 - EB) * np.tan(np.sqrt(10 - EB)) - np.sqrt(EB)

# Plot the function
EB_values = np.linspace(0, 10, 100)
f_values = equation_even(EB_values)

plt.plot(EB_values, f_values)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('EB')
plt.ylabel('f(EB)')
plt.title('Plot of f(EB) = sqrt(10 - EB) * tan(sqrt(10 - EB)) - sqrt(EB)')
plt.grid(True)
plt.show()

# Find approximate values for the zeros
zeros = fsolve(equation_even, [1, 3, 5, 7])
print("Approximate values for the zeros of f(EB):")
print(zeros)
