# Task 10
# =======
# Create a program which asks for and stores each test score (INTEGER) in a class of 20 students.
# The program should only accept test scores between 0 and 100 inclusive.
# Display an error message if the number is outside of the valid range.
# When a valid score is entered, add this to a 1-D array called “testScores”.
# Display the contents of the 1-D array at the end of the program.
# Use iteration in your program solution.

testScores = []

for index in range(20):
    thisTestScore = int(input("Enter a test score:"))
    while thisTestScore < 0 or thisTestScore > 100:
        print("Error! Enter a number between 0 and 100.")
        thisTestScore = int(input("Enter a test score:"))
    testScores.append(thisTestScore)

for index in range(20):
    print(testScores[index])