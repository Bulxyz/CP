import numpy as np
from scipy.optimize import fsolve

V0 = 10

def equation_even(EB):
    return np.sqrt(10 - EB) * np.tan(np.sqrt(10 - EB)) - np.sqrt(EB)

# Solve for bound-state energies
energies = fsolve(equation_even, np.linspace(0, V0, 100))

print("Bound-state energies for even wave functions:")
print(energies)
