# Talent Show
# By I Simpson
# 25/06/2024

# RECEIVE name FROM KEYBOARD
name = input("What is your name? ")
# GET age FROM KEYBOARD
age = int(input("Enter your age: "))
# WHILE (age < 11) OR (age> 18)
while age < 11 or age > 18:
# SEND “Invalid age” TO DISPLAY
    print("Invalid age")
# GET age FROM KEYBOARD
    age = int(input("Enter your age: "))
# END WHILE

# SEND “Welcome to the talent show” & name TO DISPLAY
print("Welcome to the Talent Show", name)