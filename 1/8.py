# Area.py

import math

PI = 3.14159

def calculate_volume(radius):
  return (4/3) * PI * radius ** 3

def main():

  # Open input file
  input_file = open('input.txt', 'r')

  # Read radius from file  
  radius = float(input_file.read())

  # Close input file
  input_file.close()

  # Calculate volume  
  volume = calculate_volume(radius)

  # Open output file
  output_file = open('output.txt', 'w')

  # Write output to file
  output_file.write(f'The volume of the sphere with radius {radius} is: {volume}')

  # Close output file
  output_file.close()

  # Open output file and print
  output_file = open('output.txt', 'r')
  print(output_file.read())

if __name__ == '__main__':
  main()
