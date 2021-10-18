def check_ok(boat, taken):

    boat.sort()
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

        if i != 0:
            if boat[i] != boat[i -1] +1 and boat[i + 1] != boat[i] + 10:
                boat = [-1]
                break     
    return boat

#aks the user to enter numbers
def get_ship(long, taken):
    ok = True
    while ok:
        ship = []
        print( "enter your ship of length", long)
        for i in range(long):
            boat_num = input("please enter the number")
            ship.append(int(boat_num))

            ship = check_ok(ship, taken)
            if ship[0] != -1:
                taken = taken + ship 
                break
            else:
                print("Error - Please try again!")

    return ship

def create_ships():
    taken = []
    ships = []
    boats = [5, 4, 3, 3, 2, 2]

    for boat in boats:
        ship = get_ship(boat, taken)
        ships.append(ship)
    return ships


#before game
hit1 = []
miss1 = []
comp1 = []
guesses1 = []
missed1 = 0
tactics1 = []
taken1 = []

hit2 = []
miss2 = []
comp2 = []
guesses2 = []
missed2 = 0
tactics2 = []
taken2 = []
#computer creats a board for player 1
ships, taken = create_boates()

#user creates the ships for player 2 - show board
ships = create_ships()

#loop
# function for the computer shots count
for i in range(80):
#user shoots
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    ships,hit,miss,comp = check_shot(shot,boat1,boat2,hit,miss,comp)
    show_board(hit,miss,comp)

#computer shoots
#repeat until ships empty
    shot, guesses = get_shot_comp(guesses, tactics)
    ships, hit, miss, comp,missed = check_shot(shot, ships, hit, miss, comp)
  
    if missed == 1:
        tactics = calc_tactics(shot, tactics, guesses, hit)
    elif missed == 2:
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0)
# end of game and how meny rounds it took
    if chech_if_empty_2(ships):
        print("End Of Game",i)
        break


