import math

# Function to calculate the quadratic solutions
def quadratic_solutions(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        x3 = (-2*c) / (b + math.sqrt(discriminant))
        x4 = (-2*c) / (b - math.sqrt(discriminant))
        return x1, x2, x3, x4
    else:
        return None

# Input values for a, b, and c
a = 1
b = 5
c = 6

# Calculate the solutions
solutions = quadratic_solutions(a, b, c)

# Display the solutions
if solutions:
    x1, x2, x3, x4 = solutions
    print("Quadratic Solutions:")
    print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
else:
    print("No real solutions exist for the given coefficients.")
