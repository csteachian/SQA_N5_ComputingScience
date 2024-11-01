# Validating a price [Python]
# 308a Input Validation

#Get user input
price= int(input("Enter price"))

#Validate greater than 0
while price <= 0:
    print("Error, price must be greater than 0")
    price = int(input("Please enter a valid price"))