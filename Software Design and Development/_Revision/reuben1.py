# SQA 2025 Q9b
purpose = input("Enter the purpose of the animation: ")
if purpose == "education":
    discount = 20
elif purpose == "charity":
    discount = 30
else:
    discount = 0
finalCost = basicCost - discount
print(finalCost)