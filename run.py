
# Computer random for boat
from random import randrange
import random
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
# computer boat range and med the computer not to overlap the boats
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
# Create the boats fot computer
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
# show the boats on the board
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
# get shots function 
def get_shot_comp(guesses, tactics):

    print("Add a number between 0 and 99")
    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
            
        except:
            print("inccorrect entry - please enter again!!")
    return shot,guesses

# show the hit,miss marker on the board
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

# hot function - to track the shot and change the board
def check_shot(shot,ships,hit,miss,comp):
    
    missed = 0
    for i in range(len(ships)):

        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                comp.append(shot)
                missed = 2
    if missed == 0:
        miss.append(shot)

    return ships,hit,miss,comp,missed

# calculate shot base of hit or miss for the computer
def calc_tactics(shot,tactics,guesses,hit):

    temp = []
    if len(tactics) < 1:
        temp = [shot-1,shot+1,shot-10,shot+10]
    else: 
        if shot-1 in hit:
            temp = [shot-2,shot+1]
        elif shot+1 in hit:
            temp = [shot+2,shot-1]
        elif shot-10 in hit:
            temp = [shot-20,shot+10]
        elif shot+10 in hit:
            temp = [shot+20,shot-10]
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)

    return cand

hit = []
miss = []
comp = []
guesses = []
ships, taken = create_boates()
tactics = []


# function for the computer shots count
for i in range(10):
    shot,guesses = get_shot_comp(guesses, tactics)
    ships,hit,miss,comp,missed = check_shot(shot,ships,hit,miss,comp)
  
    if missed == 1:
        tactics = calc_tactics(shot,tactics,guesses,hit)
    elif missed == 2:
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0)

show_board_c(taken)
show_board(hit,miss,comp)


