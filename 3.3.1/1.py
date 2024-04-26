import math

def sin_approximation(x, num_terms):
    result = 0
    for n in range(num_terms):
        coefficient = (-1)**n
        term = x**(2*n + 1) / math.factorial(2*n + 1)
        result += coefficient * term
    return result

x = 1.2  # Input value for x
num_terms = 10  # Number of terms in the finite sum approximation

sin_x_approx = sin_approximation(x, num_terms)
sin_x_actual = math.sin(x)

print(f"Approximation of sin({x}) using {num_terms} terms: {sin_x_approx}")
print(f"Actual value of sin({x}): {sin_x_actual}")
