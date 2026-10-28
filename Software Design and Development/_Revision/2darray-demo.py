columns = [0 for x in range(9)]
rows = [columns for x in range(9)]

# display board
for r in range(9):
    output = ""
    for c in range(9):
        output = output + "," + str(rows[r][c])
    print(output)

# get row and column
row = int(input("Enter row:"))
while row < 1 or row > 9:
    row = int(input("Error. Enter row:"))
col = int(input("Enter col:"))
while col < 1 or col > 9:
    col = int(input("Error. Enter col:"))
num = int(input("Enter num:"))
while num < 1 or num > 9:
    num = int(input("Error. Enter num:"))

rows[row][col] = num

# display board
for r in range(9):
    output = ""
    for c in range(9):
        output = output + "," + str(rows[r][c])
    print(output)
