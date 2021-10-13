class Battleship(object):

    @staticmethod
    def build(head, length, direction):
        body = []
        for i in range(length):
            if direction == "N":
                el =(head[0], head[1] - i)
            elif direction == "S":
                el =(head[0], head[1] + i)
            elif direction == "E":
                el =(head[0] - i, head[1])
            elif direction == "W":
                el =(head[0] + i, head[1])

            body.append(el)

        return Battleship(body)

    def __init__(self, body):
        self.body = body


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
    Battleship = [
        Battleship.build((1,1), 2, "N" ),
        Battleship.build((3,5), 3, "S" ),
        Battleship.build((7,2), 4, "E" )
    ]

    for b in Battleship:
        print(b.body)

    exit(0)



    shots = []

    while True:
        inp = input("Take your shot?\n")
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(8, 8, shots)