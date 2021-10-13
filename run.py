class Battleship(object):

    def __init__(self)

# Game board layout
def render(board_width, board_height, shots):
    header = "+" + "-" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "x"
            else:
                ch = " "
            row.append(ch)
        print("| " + "0".join(row) + " |")    

    print(header)
    
if __name__ == "__main__":
    shots = []

    while True:
        inp = input("Take your shot?\n")
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(8, 8, shots)