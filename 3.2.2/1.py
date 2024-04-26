import numpy as np

def bessel_downward_recursion(L, x_values):
    j = np.zeros((len(x_values), L+1))

    # Initial values for j_0(x) and j_1(x)
    j[:, 0] = np.sin(x_values) / x_values
    j[:, 1] = np.sin(x_values) / x_values**2 - np.cos(x_values) / x_values

    for l in range(1, L):
        j[:, l+1] = ((2*l + 1) / x_values)* j[:, l] - j[:, l-1]

    return j

L_values = 25
x_values = [0.1, 1, 10]

for x in x_values:
    bessel_values = bessel_downward_recursion(L_values, np.array([x]))

    print(f"Bessel Function values for x = {x}:")
    for l in range(L_values + 1):
        print(f"j_{l}({x}) = {bessel_values[0][l]}")

#####################################################
import numpy as np

def bessel_upward_recursion(L, x_values):
    j = np.zeros((len(x_values), L+1))

    # Initialize the starting values for j_0(x) and j_1(x)
    j[:, 0] = np.sin(x_values) / x_values
    j[:, 1] = np.sin(x_values) / x_values**2

    for l in range(1, L):
        j[:, l+1] = ((2*l + 1) / x_values)* j[:, l] - j[:, l-1]

    return j

L_values = 25
x_values = [0.1, 1, 10]

for x in x_values:
    bessel_values = bessel_upward_recursion(L_values, np.array([x]))

    print(f"Bessel Function values for x = {x}:")
    for l in range(L_values + 1):
        print(f"j_{l}({x}) = {bessel_values[0][l]}")
