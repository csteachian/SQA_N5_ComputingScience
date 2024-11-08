# 311a Variables.py

# Describe, exemplify, and implement the appropriate constructs
# in a high-level (textual) language:
# - expressions to assign values

character = 'A' # character data type
name = 'Genevieve' # string
votes = 266 # integer
price = 19.99 # float
hasWon = True # boolean
items = [] # empty 1D array
items = ['Banana','Honey','Porridge','Milk'] # 1D array of string
items.append('Apple')

# - expressions to return values using arithmetic operations (addition, subtraction, multiplication, division, and exponentiation)

stockLevel = 16
chocBarPrice = 1.15
totalCost = 0
print(stockLevel, chocBarPrice, totalCost)
totalCost = stockLevel * chocBarPrice # multiplying stockLevel by chocBarPrice
print(stockLevel, chocBarPrice, totalCost)
print("This is not a variable",stockLevel)

# shopping list
items = []
for index in range(5):
    items.append(input("Enter item for shopping list: "))

print(items)