# Francisco Sanchez
# 11/08/23

import math

# Define a function to calculate the area of a circle with radius 'r'.
def areaOfCircle(r):
    # Check if the radius is negative.
    if r < 0:
        return "Radius cannot be negative" # Return an error message if the radius is negative.
    else:
        return math.pi * (r ** 2)

# Here is the radius used
radius = 5.0
area = areaOfCircle(radius)
print(f"The area of circle with radius {radius} is {area:.2f}")
