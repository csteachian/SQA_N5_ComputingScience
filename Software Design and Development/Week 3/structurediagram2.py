# Structure Diagram Example 2

# assumptions
num_charging_stations = 3
startMiles = 0

for index in range(num_charging_stations):
    currentMiles = int(input("Enter current mileage: "))
    kwRating = int(input("Enter valid kw rating: "))
    if kwRating == 7:
        pricePerMile = 0
    else:
        if kwRating == 22:
            pricePerMile = 0.005
        else:
            pricePerMile = 0.01
    milesTravelled = (currentMiles - startMiles)
    startMiles = currentMiles
    costOfJourneyStage = pricePerMile * milesTravelled

    