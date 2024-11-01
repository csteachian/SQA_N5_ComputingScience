# 309 Example 1
# A program asks the user to enter their age as a whole number.

age = int(input("Enter your age: "))
while age < 0 or age >= 117:
    print("Error. Invalid age. Try again.")
    age = int(input("Enter your age: "))
print("Thank you. Your age has been recorded as",age)