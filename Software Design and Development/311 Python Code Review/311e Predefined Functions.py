# 311e Predefined Functions

# predefined functions (with parameters): random; round; length
print()
# random numbers
import random
for index in range(0,6):
    lotteryBall = random.randint(1,59)
    print(lotteryBall)

# round
cost = float(input("Please enter the cost of the item in £ and p: "))
noPounds = round(cost)
print("You will need £"+str(noPounds))
print("And you will get "+str(noPounds-cost)+"p change")


# round
fp = random.random() * 100
print(fp)
newFP = round(fp,2)
print(newFP)

# length

# password validator
password = input("Please enter your password: ")
while len(password) < 8:
    print("Your password must be 8 characters or more.")
    password = input("Please enter your password: ")
print("Password accepted.")

# This example counts the number of letters in the word variable

word = "Flibberwockelbumperdoodlecronkflizzlewhap"
noLetters = len(word) # counts each character in the word
print(word,"has",noLetters,"letters.")

# This example counts the number of items in the array

items = ['Banana','Apple','Crab','Dog Food','Egg']
noItems = len(items) # counts the number of items in the array
print(items,"has",noItems,"items in the array.")

# This example sums the number of letters in each item of the list

items = ['Banana','Apple','Crab','Dog Food','Egg']
noItems = len(items) # counts the number of items in the array
total = 0
for index in range(noItems):
    total = total + len(items[index]) # count the number of letters in each item
print(items,"has",noItems,"items and in total",total,"letters.")