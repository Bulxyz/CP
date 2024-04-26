import numpy as np

def bessel_upward_recursion(L, x_values, tolerance=1e-10):
    j = np.zeros((len(x_values), L+1))

    # Initialize the starting values for j_0(x) and j_1(x)
    j[:, 0] = np.sin(x_values) / x_values
    j[:, 1] = np.sin(x_values) / x_values**2

    for l in range(1, L):
        j[:, l+1] = ((2*l + 1) / x_values)* j[:, l] - j[:, l-1]

        # Check for convergence and break if relative error is below tolerance
        if np.allclose(j[:, l+1], j[:, l], atol=tolerance):
            break

    return j

L_values = 25
x_values = [0.1, 1, 10]
tolerance = 1e-10

for x in x_values:
    bessel_values = bessel_upward_recursion(L_values, np.array([x]), tolerance)

    print(f"Bessel Function values for x = {x}:")
    for l in range(L_values + 1):
        print(f"j_{l}({x}) = {bessel_values[0][l]}")
