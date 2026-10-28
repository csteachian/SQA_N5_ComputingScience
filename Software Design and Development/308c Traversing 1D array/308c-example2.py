# 308c Traversing 1D Array - Example 2

total = 0
items = [4,9,6,13] # <-- array
for index in range(len(items)): # <-- fixed loop, len
    total = total + items[index] # <-- adds current item in array to total variable    

print(total)