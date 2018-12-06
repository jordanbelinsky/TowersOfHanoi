"""
File Name: iterative.py
Description: iterative implementation of towers of hanoi
"""

#############
# Game Logo #
#############
print("""
  _______                                  __   _    _                   _ 
 |__   __|                                / _| | |  | |                 (_)
    | | _____      _____ _ __ ___    ___ | |_  | |__| | __ _ _ __   ___  _ 
    | |/ _ \ \ /\ / / _ \ '__/ __|  / _ \|  _| |  __  |/ _` | '_ \ / _ \| |
    | | (_) \ V  V /  __/ |  \__ \ | (_) | |   | |  | | (_| | | | | (_) | |
    |_|\___/ \_/\_/ \___|_|  |___/  \___/|_|   |_|  |_|\__,_|_| |_|\___/|_|
 """)
print("       By: Jordan Belinsky")
print()
print("------------------------------------------------------------------------------")
print()

#############
# Variables #
#############
from iterativeStack import Stack
while True:
    try:
        user_input = int(input("How many discs would you like to sort? "))                     
        if user_input >= 1:                                                                     
            break
        else:
            print("Please input another number.")
    except:
        print("Please input another number.")
moves = 0
towers = [Stack("Tower 1"), Stack("Tower 2"), Stack("Tower 3")]

#############
# push Loop #
#############
for i in range(user_input, 0, -1):
    towers[0].push("=="*(i+1)+str(i)+"=="*(i+1))  # push first tower through allowed movement

##########################
# Movement Possibilities #
##########################
possible_moves_even = [[towers[0], towers[1], towers[2]], # tower 1 -> 2
                       [towers[0], towers[2], towers[2]], # tower 1 -> 3
                       [towers[1], towers[2], towers[2]]] # tower 2 -> 3

possible_moves_odd = [[towers[0], towers[2], towers[2]],  # tower 1 -> 3
                      [towers[0], towers[1], towers[2]],  # tower 1 -> 2
                      [towers[1], towers[2], towers[2]]]  # tower 2 -> 3


#####################
# moveEven Function #
#####################
def moveEven(possible_moves_even):
    for i in possible_moves_even:
        i[0].viableMove(i[1], i[2])
        printOutput(towers[0], towers[1], towers[2], towers[2].moves)
        proveMoves(i[0].name, i[1].name)

####################
# moveOdd Function #
####################
def moveOdd(possible_moves_odd):
    for i in possible_moves_odd:
        i[0].viableMove(i[1], i[2])
        printOutput(towers[0], towers[1], towers[2], towers[2].moves)
        proveMoves(i[0].name, i[1].name)
        if towers[2].size() == user_input:
            return False

#######################
# proveMoves Function #
#######################
def proveMoves(pos_1, pos_2):
    print("A disk has been moved between "+str(pos_1)+" and "+pos_2+".")    # check for what move was made

########################
# printOutput Function #
########################
def printOutput(tower1, tower2, tower3, moves):     
    if moves == 0:      # dont print move number if a move has not yet been made
        print("\n---- Initial Towers ----")
    else:                                     
        print("\n---- Move #"+str(moves)+" ----")   # print current move number
    print("\nTower 1:", str(tower1) + "\nTower 2:", str(tower2) + "\nTower 3:", str(tower3))    # print information for towers
    return moves                

##########
# Output #
##########
printOutput(towers[0], towers[1], towers[2], moves) # set printing output characteristics
while user_input != towers[2].size():
    if user_input%2 == 0:    # even
        moveEven(possible_moves_even)
    else:   # odd
        moveOdd(possible_moves_odd)

############
# End Game #
############
print()
print("Game Over! Thanks for Playing")
print()