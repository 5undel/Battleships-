def show_board(hit,miss,comp):
    print("      BATTLESHIP")
    print("     0  1  2  3  4  5  6  7  8  9")


    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in hit:
                ch ="💥 "
            elif place in miss:
                ch =" x "
            elif place in comp:
                ch ="💀 "
            row = row + ch
            place = place + 1
        print(x, " ", row)
    

hit = [21,22,]
miss = [20,24,12,13]
comp = [23]

show_board(hit,miss,comp)