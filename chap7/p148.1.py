import numpy as np

# Define the functions
def f_even(E_B):
    return np.sqrt(10 - E_B) * np.tan(np.sqrt(10 - E_B)) - np.sqrt(E_B)

def f_odd(E_B):
    return np.sqrt(10 - E_B) * 1/np.tan(np.sqrt(10 - E_B)) - np.sqrt(E_B)

# Define the derivatives for Newton-Raphson method
def df_even(E_B):
    sqrt_term = np.sqrt(10 - E_B)
    tan_term = np.tan(sqrt_term)
    return (-0.5 / sqrt_term) * tan_term + (sqrt_term / np.cos(sqrt_term)**2) + 0.5 / np.sqrt(E_B)

def df_odd(E_B):
    sqrt_term = np.sqrt(10 - E_B)
    cot_term = 1 / np.tan(sqrt_term)
    return (-0.5 / sqrt_term) * cot_term - (sqrt_term / np.sin(sqrt_term)**2) + 0.5 / np.sqrt(E_B)

# Newton-Raphson method
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Newton-Raphson did not converge")

# Bisection method
def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Bisection method requires a change of sign over the interval")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Bisection method did not converge")

# Helper function to find a valid interval for Bisection method
def find_sign_change_interval(f, start, end, step=0.1):
    a = start
    b = a + step
    while b <= end:
        if f(a) * f(b) < 0:
            return a, b
        a = b
        b = a + step
    raise ValueError("No sign change found in the interval")

# Finding solutions
# Initial guesses for Newton-Raphson method
initial_guesses_even = [0.5, 4, 7]
initial_guesses_odd = [2, 5, 8]

# Intervals for Bisection method
intervals_even = [find_sign_change_interval(f_even, 0, 10) for _ in initial_guesses_even]
intervals_odd = [find_sign_change_interval(f_odd, 0, 10) for _ in initial_guesses_odd]

# Solving with Newton-Raphson
solutions_newton_even = [newton_raphson(f_even, df_even, x0) for x0 in initial_guesses_even]
solutions_newton_odd = [newton_raphson(f_odd, df_odd, x0) for x0 in initial_guesses_odd]

# Solving with Bisection
solutions_bisect_even = [bisection(f_even, a, b) for a, b in intervals_even]
solutions_bisect_odd = [bisection(f_odd, a, b) for a, b in intervals_odd]

# Comparing the solutions
print("Solutions using Newton-Raphson (even):", solutions_newton_even)
print("Solutions using Newton-Raphson (odd):", solutions_newton_odd)
print("Solutions using Bisection (even):", solutions_bisect_even)
print("Solutions using Bisection (odd):", solutions_bisect_odd)
