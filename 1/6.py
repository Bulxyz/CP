# Area.py

import math

PI = 3.14159

def volume_of_sphere(radius):
  return (4/3) * PI * radius ** 3

# Open input file for reading 
input_file = open('input.txt', 'r') 

# Read radius from input file
radius = float(input_file.read())

# Calculate volume
volume = volume_of_sphere(radius)

# Open output file for writing  
output_file = open('output.txt', 'w')

# Write volume to output file in a specific format
output_file.write(f'The volume of the sphere with radius {radius} is: {volume}')

# Close files
input_file.close()
output_file.close()

# Open output file and read contents
output_file = open('output.txt', 'r')
print(output_file.read())

