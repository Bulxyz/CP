# Area.py

import math

PI = 3.14159

def volume_of_sphere(radius):
  return (4/3) * PI * radius ** 3

radius = float(input("Enter the radius of the sphere: "))
volume = volume_of_sphere(radius)
print("The volume of the sphere is:", volume)
