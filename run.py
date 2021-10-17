from random import randrange

def check_ok(boat,taken):

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break


    return boat

def check_boat(b, start,dirn,taken):

    
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_ok(boat,taken)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_ok(boat,taken)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_ok(boat,taken)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_ok(boat,taken)
    return boat

def create_boates():
    taken = []
    ships = []
    boats = [5,4,3,3,2,2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            print(b,boat_start,boat_direction)
            boat = check_boat(b,boat_start,boat_direction,taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)

    return ships,taken

def show_board_c(taken):
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

def get_shot_comp(guesses):

    print("Add a number between 0 and 99")
    ok = "n"
    while ok == "n":
        try:
            shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
            
        except:
            print("inccorrect entry - please enter again!!")
    return shot,guesses

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

def check_shot(shot,ships,hit,miss,comp):
    
    missed = 1
    for i in range(len(ships)):

        if shot in ships[i]:
            ships[i].remove(shot)
            missed = 0
            if len(ships[i]) > 0:
                hit.append(shot)
            else:
                comp.append(shot)
    if missed == 1:
        miss.append(shot)

    return ships,hit,miss,comp

hit = []
miss = []
comp = []
guesses = []
ships, taken = create_boates()
show_board_c(taken)

for i in range(50):
    shot,guesses = get_shot_comp(guesses)
    ships,hit,miss,comp = check_shot(shot,ships,hit,miss,comp)
    show_board(hit,miss,comp)



