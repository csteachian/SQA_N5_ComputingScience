# 309 - Example 2
# A program asks the user to enter a letter between A and D to select an answer to a multiple choice quiz.

answer = input("Enter your answer (A-D): ")
while answer < "A" or answer > "D":
    print("Error. Invalid answer. Try again.")
    answer = input("Enter your answer (A-D): ")
print("You answered ",answer)