import random

arraything = [1,6,42,99,128,666]
# Program 4 - Investigate and modify
rightnumber = random.choice(arraything)
guess = 1
number = int(input("Guess a number: "))
while (guess < 5) and (number != rightnumber):
  print("Not right. Try again.")
  print("The random number was:",rightnumber)
  number = int(input("Guess a number: "))
  rightnumber = random.choice(arraything)
  guess = guess + 1
  
if guess < 5:
   print("Well done!")
print("The random number was:",rightnumber)