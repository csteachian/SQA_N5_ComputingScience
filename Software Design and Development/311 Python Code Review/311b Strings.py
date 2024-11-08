# 311b Strings

# Expressions to concatenate strings

example1 = "Hello"
example2 = "World"
fullMessage = example1 + example2 # concatenates example1 and example2 together
print(fullMessage)

# Expressions to extract substrings

firstName = 'Genevieve'
initial = firstName[0:1]
lastLetter = firstName[8:9] # gets last letter of firstName
lastLetter = firstName[-1:] # gets last letter of firstName (same as prev)
firstThree = firstName[:3] # gets first three letters of firstName
print(initial, lastLetter, firstThree)

# username generator
firstName = input("Enter firstname: ")
surname = input("Enter surname: ")
yearOfBirth = int(input("Enter year of birth: "))
username = firstName[0:1]+surname[-3:]+str(yearOfBirth)[2:]
print(username)