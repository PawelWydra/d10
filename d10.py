height = int(input("enter candy cane height"))

for row in range(height):
    for col in range(6):
        if (col == 5 and row != 0) or (row == 0) and (0 < col < 5):
            print("x", end="")
        elif col == 0 and row != 0 and row < (height / 2):
            print("x", end="")
        else:
            print(end=" ")
    print()
