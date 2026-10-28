heightOfChair = int(input("Enter the height of one chair: "))
heightOfTower = int(input("Enter the height of the stacked pair tower: "))
noChairLegs = ((heightOfTower / heightOfChair) * 2) * 4
print("The total number of chair legs in the tower is: "+str(noChairLegs))