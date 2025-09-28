# Task 8
# ======
# Create a program which asks for the first name of each student (STRING) in a group of 10.
# Add each name to a 1-D array called “names”.
# Display the contents of the 1-D array at the end of the program.
# Use iteration in your program solution.

names = []

for index in range(10):
    student = input("Enter the first name of student:")
    names.append(student)

for index in range(10):
    print(names[index])