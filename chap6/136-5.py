import numpy as np

# Define the size of the system
N = 100

# Define the coefficient matrix a
a = np.fromfunction(lambda i, j: 1 / (i + j + 1), (N, N))

# Define the right-hand side vector b
b = np.array([1 / (i + 1) for i in range(N)])

# Solve the system of linear equations
y = np.linalg.solve(a, b)

# Compare the numerical solution with the analytic solution
analytic_solution = np.zeros(N)
analytic_solution[0] = 1

# Print the comparison
print("Numerical Solution:")
print(y)
print()
print("Analytic Solution:")
print(analytic_solution)
