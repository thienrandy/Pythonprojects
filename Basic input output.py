"""
Write some code that will ask the user for their first name, last name,
myNova id, gpa, and number of semesters completed. See below for
example, but values that are different from what is shown below. Use
appropriate variable names and data types based on data samples (str, int,
float). Print values with some messaging as shown below.\
"""
print("Northern Virginia Community College login")

first_name= input("Enter your first name:")
last_name=input("Enter your last name:")
myNova= int(input("Enter your Nova ID:"))
gpa= float(input("Enter your GPA:"))
semesters_completed= int(input("Enter number of semesters completed:"))


print("Welcome to Nova:",first_name, last_name)
print("Your myNova ID is:" , myNova)
print("Congrats on your GPA of:", gpa)
print("I see you have completed:" ,semesters_completed, "semesters so far")