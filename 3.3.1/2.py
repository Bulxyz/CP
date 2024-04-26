import math

def sin_series(x, tolerance=1e-7):
    n = 1
    term = x
    result = term
    while abs(term) >= abs(result * tolerance):
        n += 1
        term = (-1)**(n-1) *x**(2*n-1) / math.factorial(2*n-1)
        result += term
    return result, n

x = 1  # Value of x (x ≤ 1)
approximation, N = sin_series(x)
sin_x_actual = math.sin(x)

print(f"Approximation of sin({x}): {approximation} (using N = {N} terms)")
print(f"Actual value of sin({x}): {sin_x_actual}")
