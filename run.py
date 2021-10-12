
def render(board_width, board_height, shots):
    print("+" + " _ " * board_width + "+")

    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots:
                ch = "x"
            else:
                ch = " "
            row.append(ch)
        print("| " + " " + " " + " " + " " + " " + " " + " " + " ".join(row) + " |")
    

    print("+" + " _ " * board_width + "+")


if __name__ == "__main__":
    render(8, 8, [(3,1), (4,3), (3,5)])

    inp = input("Wher do you want to shoot?\n")
    xstr, ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)