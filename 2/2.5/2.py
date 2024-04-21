import math

# Function to calculate the sum using the "bad way" method with explicit factorials
def bad_way_sum(x, eps=1e-8):
    term = x
    sum_val = x
    n = 2  # Start n from 2 to avoid division by zero
    while abs(term / sum_val) > eps:
        term = -term *x* x / ((2 *n + 1)* (2 * n - 2))  # Calculate the next term in the series with explicit factorials
        sum_val += term  # Add the term to the sum
        n += 1  # Increment the iteration count
    return sum_val, n  # Return the sum value and the final n value

# Define x values for computation
x_values = [0.1, 0.01, 0.001, 0.0001]

# Print table headings
print("x\timax\tsum\t|sum - sin(x)|/sin(x)")

# Calculate and print results for each x value
for x in x_values:
    sin_x = math.sin(x)
    sum_bad, n = bad_way_sum(x)  # Retrieve the sum value and the final n value
    relative_error = abs(sum_bad - sin_x) / sin_x
    print(f"{x}\t{n}\t{sum_bad}\t{relative_error}")
