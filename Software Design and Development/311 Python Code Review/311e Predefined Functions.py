# 311e Predefined Functions

# predefined functions (with parameters): random; round; length
print()
# random numbers
import random
lotteryBall = random.randint(1,59) # 1 is min, 59 is max
print(lotteryBall) # will show number between 1 and 59

# round
fp = random.random() * 100
print(fp)
newFP = round(fp,2)
print(newFP)

# length

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