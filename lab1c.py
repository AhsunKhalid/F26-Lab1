
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: SEPTEMBER 16 2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
import math
# Create a variable called 'radius' and take its value form user.
radius=input("Enter Radius:")
# Convert the variable to integer using int()
radius=int(radius)
# use the contant pi form math module and compute the area of the circle using the variable 'radius'
area=math.pi*radius**2
print(f"Area of the Circle is {area}")