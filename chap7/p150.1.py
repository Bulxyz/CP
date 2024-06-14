import numpy as np

# Define the function f(m, t)
def f(m, t):
    return m - np.tanh(m / t)

# Bisection method
def bisection(f, t, a, b, tol=1e-6, max_iter=100):
    if f(a, t) * f(b, t) >= 0:
        raise ValueError("Bisection method requires a change of sign over the interval")
    for _ in range(max_iter):
        c = (a + b) / 2
        f_c = f(c, t)
        if np.abs(f_c) < tol or (b - a) / 2 < tol:
            return c
        if f(a, t) * f_c < 0:
            b = c
        else:
            a = c
    raise ValueError("Bisection method did not converge")

# Function to find a suitable interval where the function changes sign
def find_sign_change_interval(f, t, start, end, step=0.1):
    a = start
    b = a + step
    while b <= end:
        if f(a, t) * f(b, t) < 0:
            return a, b
        a = b
        b += step
    raise ValueError("No sign change found in the interval")

# Parameters
t = 0.5

# Finding a suitable interval [a, b] for the bisection method
start = 0
end = 2
a, b = find_sign_change_interval(f, t, start, end)

# Finding the root
root = bisection(f, t, a, b, tol=1e-6)

# Print the root with six significant figures
print(f"Root to six significant figures for t = {t}: {root:.6f}")
