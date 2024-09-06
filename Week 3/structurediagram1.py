# Structure Diagram Example 1

child_buffet = 2.00
response = input("Do you want cake? (yes/no): ")
if response == "yes":
    cake = 15.00
else:
    cake = 0.0
num_adults = int(input("Enter number of adults: "))
num_children = int(input("Enter number of children: "))
diet = []
for index in range(num_children):
    message = "Enter dietary requirements for child",index,": "
    requirements = input(message)
    diet.append(requirements)
if (num_adults + num_children) > 20:
    venue = 0.0
else:
    venue = 50.0
    
cost = (child_buffet * num_children) + cake + venue