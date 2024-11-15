# # # Variables & Operations

# # name = "Mr Simpson"

# # variableName = "value"

# # cost = 19.995

# # numberOfItems = 9 # integer

# # print("there are",numberOfItems,"items in your basket.")
# # print("there are"+str(numberOfItems)+"items in your basket.")

# # totalCost = numberOfItems * cost
# # print("Total Cost is",totalCost) # pre-defined function

# # ----------------------------
myArray = ['A','B','D','D','C','A']
answers = ['B','B','D','A','D','B']
questionNo = [1,2,3,4,5,6]

for pos in range(6):
    if questionNo[pos] == 1:
        if (myArray[pos] == answers[pos]):    
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Not the important question.")

#-----
# stickerText = "Beep for Scotland"
# for index in range(10): # fixed loop
#     print(stickerText)
#     print()

# stickerText = "Beep for Scotland"
# keepGoing = "Y"
# while keepGoing == "Y":
#     print(stickerText)
#     keepGoing = input("Keep going? (Y/N): ")