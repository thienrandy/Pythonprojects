"""
Write a Python program to
compute and print the volume of a 3D pyramid.
Use this formula. Display the answer rounded
up to 2 decimal places.
Formula: V = l * w * h / 3
"""

#Step 1 - Ask user for inputs (INPUTS)
length_of_pyramid = float(input("Enter length of pyramid: "))
width_of_pyramid = float(input("Enter width of pyramid: "))
height_of_pyramid = float(input("Enter height of pyramid: "))

#Step 2 - Perform the calculations (processing)
volume_of_pyramid = ( length_of_pyramid * width_of_pyramid * height_of_pyramid / 3)

#Step 3 - Print the answer (outputs)
print("The volume of the Pyramid is {:.2f}".format(volume_of_pyramid))
