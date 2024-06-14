import math

def f(m, t):
    return m - math.tanh(m / t)

def f_prime(m, t):
    return 1 - (1 - math.tanh(m / t)**2) / t

def newton_raphson(initial_guess, t, tol=1e-6, max_iterations=100):
    m = initial_guess
    for i in range(max_iterations):
        f_value = f(m, t)
        if abs(f_value) < tol:
            return m
        f_prime_value = f_prime(m, t)
        m = m - f_value / f_prime_value
    print("Newton-Raphson method failed to converge.")
    return None

# Find the root
t = 0.5
initial_guess = 0.4
root = newton_raphson(initial_guess, t)

if root is not None:
    print(f"The root is: {root:.6f}")
