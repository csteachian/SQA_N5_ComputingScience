marks = [45,23,55,86,2,87,33,0]

for index in range(len(marks)):
    if marks[index] > 70:
        print("A")
    elif marks[index] > 60:
        print("B")
    elif marks[index] > 50:
        print("C")
    elif marks[index] > 40:
        print("D")
    else:
        print("F")