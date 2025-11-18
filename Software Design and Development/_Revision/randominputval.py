bookrating = int(input("Enter your book rating"))
while bookrating < 1 or bookrating > 5:
    print("Invalid rating. Should be 1-5")
    bookrating = int(input("Enter your book rating"))
print("You entered",str(bookrating),"as your rating.")