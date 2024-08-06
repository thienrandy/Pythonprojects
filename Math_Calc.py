"""
user -> numbers -> Python app (Calc) -> output answer area of 2D trapezoid
Formula A= a+b / 2 * h
"""
len_of_top = float(input("Enter length of the top: "))
len_of_bottom = float(input("Enter length of the bottom: "))
height = float(input("Enter the height: "))

#Step 2 - Perform the calculations (processing)
area_of_trapezoid = ((len_of_top + len_of_bottom) / 2) * height

#Step 3 - Print the answer (outputs)
print("The area of the trapezoid is {:.2f}".format(area_of_trapezoid))



