import numpy as np

def equation_even(EB):
    return np.sqrt(10 - EB) * np.tan(np.sqrt(10 - EB)) - np.sqrt(EB)

def equation_odd(EB):
    return np.sqrt(10 - EB) / np.tan(np.sqrt(10 - EB)) - np.sqrt(EB)

def bisection_method(equation, a, b, tolerance, max_iterations):
    if equation(a) * equation(b) >= 0:
        print("The bisection method cannot guarantee convergence.")
        return None

    iteration = 1
    while iteration <= max_iterations:
        c = (a + b) / 2
        if equation(c) == 0 or (b - a) / 2 < tolerance:
            return c
        
        if equation(a) * equation(c) < 0:
            b = c
        else:
            a = c
        
        iteration += 1

    print("The bisection method did not converge within the specified number of iterations.")
    return None

# Find solutions for even wave functions
a = 0
b = 10
tolerance = 1e-6
max_iterations = 100

solution_even = bisection_method(equation_even, a, b, tolerance, max_iterations)
if solution_even is not None:
    print("Solution for even wave function:")
    print(solution_even)
else:
    print("No solution found for even wave function.")

# Find solutions for odd wave functions
a = 0
b = 10

solution_odd = bisection_method(equation_odd, a, b, tolerance, max_iterations)
if solution_odd is not None:
    print("Solution for odd wave function:")
    print(solution_odd)
else:
    print("No solution found for odd wave function.")
