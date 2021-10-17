print("      BATTLESHIP")
print("     0  1  2  3  4  5  6  7  8  9")

hit = [21]
place = 0
for x in range(10):
    row = ""
    for y in range(10):
        ch = " _ "
        if place == 21:
            ch =" x "
        row = row + ch
        place = place + 1
    print(x, " ", row)
 