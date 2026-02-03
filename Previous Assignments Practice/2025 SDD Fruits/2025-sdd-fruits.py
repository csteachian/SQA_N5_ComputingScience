import random

# 1. initialise variables
counter = 0
decision = "yes"
# 2. initialise a data structure and store the mystery fruits
mysteryFruit = ["apple" "banana" "blueberry" "kiwi" "mango" "orange" "peach" "pineapple" "raspberry" "strawberry"]
# 3. initialise a data structure to store the user's fruit selections
userFruits = []

# 4. WHILE decision = yes AND counter < 6
while decision == "yes" and counter <6:
    # 5. get and store valid fruit selection (input validation)
    userInput = input("please enter the fruit name: ")
    while len(userInput) <4:
        print("incorect fruit name length")
        userInput = input("please enter the fruit name: ")
    # 6. add 1 to counter
    counter = counter +1
    # 7. get and store decision regarding entering another fruit
    decision = input("do you wnat to enter another fruit: ")

# END WHILE
# 8. generate a random number between 0 and 9
number = random.randit(0,9) # if you are using random, remember to "import random"

# 9. display "The fruits you entered were."
print("the fruits you entered were.")
# 10. display all users entered fruit names (loop not essential here as not explicitly asked)
for index in range(counter):
    print(userFruits[index])

# 11. display "The mystery fruit is."
# 12. display the randomly selected mystery fruit
print("the mystery fruit is ", mysteryFruit[number])

# 13. add 1 to counter
counter = counter + 1

# 14. if counter < 3 THEN
if counter <3:
    # 15. display milkshake message
    print("milkshake")
# 16. else if counter = 3 or 4
elif counter ==3 or counter == 4:
    # 17. display smoothie message
    print("smoothie")
# 18. else display fruit juice message
else:
    print("fruit juice")