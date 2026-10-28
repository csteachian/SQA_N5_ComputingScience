# 308c Traversing 1D Array - Example 3

target = 9
position = -1
items = [4,9,6,13] # <-- array
for index in range(len(items)): # <-- fixed loop, len
    if target == items[index]: # <-- selection statement
        print("FOUND IT!")
        position = index

if position < 0:
    print("NOT FOUND IT!")