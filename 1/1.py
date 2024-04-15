# Area.py

import math

PI = 3.14159

def area_of_circle(radius):
  return PI * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("The area of the circle is:", area)
