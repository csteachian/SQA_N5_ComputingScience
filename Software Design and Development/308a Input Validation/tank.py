# Tank has been hit by rocket
# Tank driving in a pond, almost fully submerged
# Rocket was going really fast
# Mayowa was riding the rocket

# rocketSpeed
rocketSpeed = int(input("Enter the speed of the rocket: "))
while rocketSpeed < 100 or rocketSpeed > 500: # metres/sec
    print("NO! It's not going to work!")
    rocketSpeed = int(input("Enter the speed of the rocket: "))
# it's valid
print("IT'S FINE. FINE. HONEST.")

# depthOfTank
# rocketRider
# tankDamage