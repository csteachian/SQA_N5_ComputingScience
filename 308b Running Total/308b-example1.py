# Running total of items in a 1D array [Python]
# 308b Running Total

# Set up items array + total variable
items = [4,9,6,13]
total = 0
# Loop 4 times
for index in range(4):
    # Add current item in items array to total
    total = total + items[index]

# Display total
print(total)