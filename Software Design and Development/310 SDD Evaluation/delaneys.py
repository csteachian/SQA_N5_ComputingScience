# 310 SDD Evaluation


# Intialising Variables 

songCounter = 0 
duration_of_training = 0 
duration_of_next_song = [0,0,0,0,0,0,0,0]
total = 0 
import random 

# Getting a valid training duration 

duration_of_training = int(input("How long is the training session going to be "))
while duration_of_training < 10 or duration_of_training > 30:
    print("ERROR, please enter a number between 10 and 30 ")
    duration_of_training = int(input("How long is the training session going to be "))

# Converting the training session time to seconds

duration_of_training = duration_of_training  * 60 

# Calculate total duration of songs

songCounter = 0 
while total < duration_of_training:
    duration_of_next_song[songCounter] = int(input("Enter the duration of the song in seconds "))
    total = total + duration_of_next_song[songCounter]
    if total >= duration_of_training:
        print("You have entered enough songs ")
    songCounter = songCounter + 1

# Displaying the training session summary 

counter = 1
print("You have played",songCounter,"number of songs")
foamMachine = random.randrange(1, songCounter)
for x in range(0, songCounter):
    print(counter,":", duration_of_next_song[x] )
    if foamMachine == counter:
        print("Start foam machine")
    counter = counter + 1 

print("The total length of the training session was ", total,)
