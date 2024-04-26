import numpy as np

def bessel_upward_recursion(L, x_values, tolerance=1e-10):
    j_up = np.zeros((len(x_values), L+1))
    relative_errors = []

    # Initialize the starting values for j_0(x) and j_1(x) for upward recursion
    j_up[:, 0] = np.sin(x_values) / x_values
    j_up[:, 1] = np.sin(x_values) / x_values**2

    for l in range(1, L):
        j_up[:, l+1] = ((2*l + 1) / x_values)* j_up[:, l] - j_up[:, l-1]

        # Calculate relative error
        error = np.abs(j_up[:, l+1] - j_up[:, l]) / np.maximum(np.abs(j_up[:, l+1]), np.abs(j_up[:, l]))
        relative_errors.append(error)

        # Check for convergence and break if relative error is below tolerance
        if np.all(error < tolerance):
            break

    return j_up

def bessel_downward_recursion(L, x_values):
    j_down = np.zeros((len(x_values), L+1))

    # Initialize the starting values for j_L(x) and j_{L+1}(x) for downward recursion
    j_down[:, L] = np.cos(x_values)
    j_down[:, L-1] = np.sin(x_values)

    for l in range(L-2, -1, -1):
        j_down[:, l] = ((2*l + 1) / x_values)* j_down[:, l+1] - j_down[:, l+2]

    return j_down

L_values = 25
x_values = [0.1, 1, 10]
tolerance = 1e-10

for x in x_values:
    j_up = bessel_upward_recursion(L_values, np.array([x]), tolerance)
    j_down = bessel_downward_recursion(L_values, np.array([x]))

    print(f"Bessel Function values for x = {x}:")
    for l in range(L_values + 1):
        relative_diff = np.abs(j_up[0][l] - j_down[0][l]) / (np.abs(j_up[0][l]) + np.abs(j_down[0][l]))
        print(f"l = {l}, j_up_{l} = {j_up[0][l]}, j_down_{l} = {j_down[0][l]}, Relative Difference = {relative_diff}")
