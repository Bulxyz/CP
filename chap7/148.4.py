import numpy as np

# Define the functions with variable potential V
def f_even(E_B, V):
    if E_B >= V or E_B < 0:
        return np.nan
    return np.sqrt(V - E_B) * np.tan(np.sqrt(V - E_B)) - np.sqrt(E_B)

def f_odd(E_B, V):
    if E_B >= V or E_B < 0:
        return np.nan
    return np.sqrt(V - E_B) * 1/np.tan(np.sqrt(V - E_B)) - np.sqrt(E_B)

# Define the derivatives for Newton-Raphson method
def df_even(E_B, V):
    if E_B >= V or E_B < 0:
        return np.nan
    sqrt_term = np.sqrt(V - E_B)
    tan_term = np.tan(sqrt_term)
    return (-0.5 / sqrt_term) * tan_term + (sqrt_term / np.cos(sqrt_term)**2) + 0.5 / np.sqrt(E_B)

def df_odd(E_B, V):
    if E_B >= V or E_B < 0:
        return np.nan
    sqrt_term = np.sqrt(V - E_B)
    cot_term = 1 / np.tan(sqrt_term)
    return (-0.5 / sqrt_term) * cot_term - (sqrt_term / np.sin(sqrt_term)**2) + 0.5 / np.sqrt(E_B)

# Newton-Raphson method with backtracking
def newton_raphson_backtracking(f, df, x0, V, tol=1e-6, max_iter=100, backtrack_factor=0.5, max_backtracks=10):
    for _ in range(max_iter):
        f_x0 = f(x0, V)
        df_x0 = df(x0, V)
        if np.isnan(f_x0) or np.isnan(df_x0):
            raise ValueError(f"Newton-Raphson failed due to invalid function or derivative value at x0 = {x0}")

        x1 = x0 - f_x0 / df_x0

        # Backtracking
        backtracks = 0
        while np.isnan(f(x1, V)) or np.abs(f(x1, V)) > np.abs(f_x0):
            x1 = x0 - backtrack_factor * (f_x0 / df_x0)
            backtrack_factor *= 0.5
            backtracks += 1
            if backtracks > max_backtracks:
                raise ValueError("Newton-Raphson with backtracking did not converge")

        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Newton-Raphson with backtracking did not converge")

# Bisection method
def bisection(f, a, b, V, tol=1e-6, max_iter=100):
    if f(a, V) * f(b, V) >= 0:
        raise ValueError("Bisection method requires a change of sign over the interval")
    for _ in range(max_iter):
        c = (a + b) / 2
        f_c = f(c, V)
        if np.isnan(f_c):
            raise ValueError(f"Bisection failed due to invalid function value at c = {c}")
        if abs(f_c) < tol or (b - a) / 2 < tol:
            return c
        if f_c * f(a, V) < 0:
            b = c
        else:
            a = c
    raise ValueError("Bisection method did not converge")

# Helper function to find a valid interval for Bisection method
def find_sign_change_interval(f, start, end, V, step=0.1):
    a = start
    b = a + step
    while b <= end:
        if f(a, V) * f(b, V) < 0:
            return a, b
        a = b
        b = a + step
    raise ValueError("No sign change found in the interval")

# Function to find solutions for a given potential V
def find_solutions(V):
    # Initial guesses for Newton-Raphson method
    initial_guesses_even = [0.5, 4, 7]
    initial_guesses_odd = [2, 5, 8]

    # Intervals for Bisection method
    intervals_even = [find_sign_change_interval(f_even, 0, V, V) for _ in initial_guesses_even]
    intervals_odd = [find_sign_change_interval(f_odd, 0, V, V) for _ in initial_guesses_odd]

    # Solving with Newton-Raphson with backtracking
    solutions_newton_even = []
    for x0 in initial_guesses_even:
        try:
            solution = newton_raphson_backtracking(f_even, df_even, x0, V)
            solutions_newton_even.append(solution)
        except ValueError as e:
            solutions_newton_even.append(str(e))

    solutions_newton_odd = []
    for x0 in initial_guesses_odd:
        try:
            solution = newton_raphson_backtracking(f_odd, df_odd, x0, V)
            solutions_newton_odd.append(solution)
        except ValueError as e:
            solutions_newton_odd.append(str(e))

    # Solving with Bisection
    solutions_bisect_even = []
    for a, b in intervals_even:
        try:
            solution = bisection(f_even, a, b, V)
            solutions_bisect_even.append(solution)
        except ValueError as e:
            solutions_bisect_even.append(str(e))

    solutions_bisect_odd = []
    for a, b in intervals_odd:
        try:
            solution = bisection(f_odd, a, b, V)
            solutions_bisect_odd.append(solution)
        except ValueError as e:
            solutions_bisect_odd.append(str(e))

    # Evaluate precision
    precisions_newton_even = [f_even(sol, V) if isinstance(sol, (int, float)) else sol for sol in solutions_newton_even]
    precisions_newton_odd = [f_odd(sol, V) if isinstance(sol, (int, float)) else sol for sol in solutions_newton_odd]
    precisions_bisect_even = [f_even(sol, V) if isinstance(sol, (int, float)) else sol for sol in solutions_bisect_even]
    precisions_bisect_odd = [f_odd(sol, V) if isinstance(sol, (int, float)) else sol for sol in solutions_bisect_odd]

    # Comparing the solutions
    print(f"Solutions for V = {V}")
    print("Solutions using Newton-Raphson with backtracking (even):", solutions_newton_even)
    print("Precision of Newton-Raphson (even):", precisions_newton_even)
    print("Solutions using Newton-Raphson with backtracking (odd):", solutions_newton_odd)
    print("Precision of Newton-Raphson (odd):", precisions_newton_odd)
    print("Solutions using Bisection (even):", solutions_bisect_even)
    print("Precision of Bisection (even):", precisions_bisect_even)
    print("Solutions using Bisection (odd):", solutions_bisect_odd)
    print("Precision of Bisection (odd):", precisions_bisect_odd)
    print()

# Testing for different potential values
for V in [10, 20, 30]:
    find_solutions(V)
