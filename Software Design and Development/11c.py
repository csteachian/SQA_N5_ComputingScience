# input
no_badges = int(input("Enter number of badges: "))
day = input("Enter day of the week MO/TU/WE/TH/FR/SA/SU: ")
price = 0.25

# process
if (no_badges > 150) and (day == "SU"):
    discount = 0.1
    price = 0.2
elif (no_badges > 150):
    discount = 0.1
else:
    discount = 0

total_price = (no_badges * price) * (1 - discount)

# output
print(total_price)