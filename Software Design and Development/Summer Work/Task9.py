# Task 9
# ======
# Create a program which asks the user to enter a number between 25 and 75 inclusive (INTEGER).
# Display an error message if the number is outside of the valid range.
# Use iteration in your program solution.

thisNumber = int(input("Enter a number:"))
while thisNumber < 25 or thisNumber > 75:
    print("Error! Enter a number between 25 and 75.")
    thisNumber = int(input("Enter a number:"))
