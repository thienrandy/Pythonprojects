"""
Write a
Python program to
compute and print the
surface area of a 3D
cylinder. Use this
formula.
A = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
"""
# Step 1:  Input the radius and height from the user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
import math

# Print the value of pi
print (math.pi)

# step 2: Calculate the surface area
surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height

# Step 3: Print the surface area
print("The surface area of a cylinder is {:.2f}".format(surface_area))
