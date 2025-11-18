# TASK 6
# ======
# Create a program which asks the user to enter the number of words in an essay (INTEGER)
# and the number of words they can type per minute (INTEGER). 
# Calculate how many minutes it will take them to type the essay.
# Display the number of minutes calculated on the screen.

noWords = int(input("Enter number of words in the essay:"))
wpm = int(input("Enter the number of words per minute you can type:"))
noMins = (noWords / wpm)
print("The essay will take you " + str(noMins) + " minutes")