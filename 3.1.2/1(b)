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

# Test case with a = 1, b = 1, and c = 10^(-n)
a = 1
b = 1

for n in range(1, 11):  # Testing for n = 1 to 10
    c = 10**(-n)
    solutions = quadratic_solutions(a, b, c)
    
    if solutions:
        x1, x2, x3, x4 = solutions
        error_x1 = abs(x1 - x3)  # Calculate error between x1 and x3
        error_x2 = abs(x2 - x4)  # Calculate error between x2 and x4
        
        print(f"For n = {n}:")
        print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}")
        print(f"Error between x1 and x3: {error_x1}")
        print(f"Error between x2 and x4: {error_x2}")
        print()
    else:
        print(f"For n = {n}: No real solutions exist for the given coefficients.")
