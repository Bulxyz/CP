import numpy as np
from scipy.optimize import fsolve

def equation_even(EB, V0):
    return np.sqrt(V0 - EB) * np.tan(np.sqrt(V0 - EB)) - np.sqrt(EB)

def find_bound_states(V0):
    energies = fsolve(equation_even, np.linspace(0, V0, 100), args=(V0,))
    return len(energies), energies

# Change the potential depth
potential_depths = [20, 30]

for V0 in potential_depths:
    num_states, states = find_bound_states(V0)
    print(f"For potential depth V0 = {V0}:")
    print(f"Number of bound states: {num_states}")
    print("Energies of bound states:")
    print(states)
    print()
