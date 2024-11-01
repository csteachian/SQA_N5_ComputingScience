# 309 Star Rating
# This program that will take in a star rating out of 5 for a film (the number should be a whole number)
# the program will keep asking for an input if the number is not between 0 and 5 (inclusive).
# The program will then display the number of stars the film got.

# Use the program code below to help you create a test table containing normal, extreme and exceptional test data.

output = ""
star_rating = int(input("Enter star rating (0-5): "))
while star_rating < 0 or star_rating > 5:
    print("Error. Invalid rating. Try again.")
    star_rating = int(input("Enter star rating (0-5): "))
for index in range(0,star_rating):
    output = output + "*"
print(output)