from scipy.optimize import fsolve
import numpy as np

# Given variables
W1 = 10
W2 = 20
L1 = 3
L2 = 4
L3 = 4
L = 8

# Define the system of equations
def equations(variables):
    theta1, theta2, theta3 = variables
    T1 = W1 / np.sin(theta1)
    T2 = W2 / np.sin(theta2)
    return [
        L1 * np.cos(theta1) + L2 * np.cos(theta2) + L3 * np.cos(theta3) - L,
        L1 * np.sin(theta1) + L2 * np.sin(theta2) - L3 * np.sin(theta3),
        T1 * np.cos(theta1) - T2 * np.cos(theta2) - L3,
    ]

# Solve the system of equations
initial_guess = [np.pi/4, np.pi/4, np.pi/4]
solutions = fsolve(equations, initial_guess)

# Extract the solutions
theta1, theta2, theta3 = solutions
T1 = W1 / np.sin(theta1)
T2 = W2 / np.sin(theta2)
T3 = np.sqrt(T1**2 + T2**2 - 2 * T1 * T2 * np.cos(theta3))

# Print the results
print("Angles (in radians):")
print("theta1 =", theta1)
print("theta2 =", theta2)
print("theta3 =", theta3)
print("\nTensions:")
print("T1 =", T1)
print("T2 =", T2)
print("T3 =", T3)
