# Calculating rainfall over a week [Python]
# 308b Running Total

# Set total to 0
total = 0
# Loop 7 times
for index in range(7):
    # Get today's rainfall from user
    rainfallToday = float(input("Enter rainfall today (mm): "))
    # Add rainfallToday to total
    total = total + rainfallToday

# Display total rounded to 2 decimal places
print(round(total,2))