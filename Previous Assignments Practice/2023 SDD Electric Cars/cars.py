# Electric Cars
# Ian Simpson

# Main steps - Calculate vehicle charging costs
milesTravelled = [] # I realised milesTravelled needs to be an array
journeyStage = []

# 1. Get journey details
# 1.1. Get mileage at the start of the journey (startMiles)
startMiles = int(input("Enter start mileage: "))
# 1.2. Get number of charging stations
noChargingStations = int(input("Enter number of charging stations: "))

# 2. Calculate and store the cost of each stage of the journey
for index in range(noChargingStations): # 2.1
    print("Current charging station = ",index) # 2.1.1
    currentMiles = int(input("Enter mileage at charging station"))

    kwRating = int(input("Enter kw rating: ")) # 2.1.2
    while kwRating != 7 and kwRating != 22 and kwRating != 50:
        print("Error. Only enter 7, 22 or 50.")
        kwRating = int(input("Enter kw rating: "))

    if kwRating == 7: # 2.1.3
        pricePerMile = 0
    elif kwRating == 22:
        pricePerMile = 0.005
    else:
        pricePerMile = 0.01
    
    thisMilesTravelled = (currentMiles - startMiles) # 2.1.4
    milesTravelled.append(thisMilesTravelled) # adapted for 1D array
    startMiles = currentMiles # 2.1.5
    journeyStage.append(pricePerMile * thisMilesTravelled) # 2.1.6 adapted for 1D array

# 3. Display total miles, journey stage costs and total cost
totalJourneyCost = 0
totalMiles = 0
for index in range(noChargingStations): # 3.1
    print("Journey stage",index," = ",journeyStage[index]) # 3.1.1
    totalJourneyCost = totalJourneyCost + journeyStage[index] # 3.1.2
    totalMiles = totalMiles + milesTravelled[index] # 3.1.3
print(round(totalJourneyCost,2)) # 3.2
print(totalMiles,"with message") # 3.3