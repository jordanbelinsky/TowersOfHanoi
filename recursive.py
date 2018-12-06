"""
File Name: recursive.py
Description: recursive implementation of towers of hanoi
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

########################
# Variables and Import #
########################
from recursiveStack import Stack    # import stack class
towers = [Stack("Tower 1"), Stack("Tower 2"), Stack("Tower 3")]
moves = 0     

#####################
# diskMove Function #
#####################
def diskMove(user_input, start_pos, end_pos, temp_pos):                                                      
    if user_input == 1:                                                 
        end_pos.push(start_pos.pop())                                                                  
        printOutput(towers[0], towers[1], towers[2], trackMoves(towers[0], towers[1], towers[2]))                              
        proveMoves(start_pos.name, end_pos.name)
    else:
        diskMove(user_input-1, start_pos, temp_pos, end_pos)
        end_pos.push(start_pos.pop())                                                                   
        printOutput(towers[0], towers[1], towers[2], trackMoves(towers[0], towers[1], towers[2]))                     
        proveMoves(start_pos.name, end_pos.name)
        diskMove(user_input-1, temp_pos, end_pos, start_pos)                                                 

#######################
# proveMoves Function #
#######################
def proveMoves(pos_1, pos_2):
    print("A disk has been moved between "+str(pos_1)+" and "+pos_2+".")    

########################
# printOutput Function #
########################
def printOutput(tower1, tower2, tower3, moves):                          
    if moves == 0:      
        print("\n---- Initial Towers ----")
    else:                                     
        print("\n---- Move #"+str(moves)+" ----")   
    print("\nTower 1:", str(tower1) + "\nTower 2:", str(tower2) + "\nTower 3:", str(tower3))   
    return moves 

#######################
# trackMoves Function #
#######################
def trackMoves(tower1, tower2, tower3):                                                       
    tower3.moves += 1
    moves = tower3.moves
    return moves                                                                                                                                                        

##################
# Input Handling #
##################
while True:
    try:
        user_input = int(input("How many discs would you like to sort? "))                     
        if user_input >= 1:                                                                     
            break
        else:
            print("Please input another number.")
    except:
        print("Please input another number.")

#############
# push Loop #
#############
for i in range(user_input, 0, -1):                                                            
    towers[0].push("=="*(i+1)+str(i)+"=="*(i+1))

##########
# Output #
##########
printOutput(towers[0], towers[1], towers[2], moves)                                                         
diskMove(user_input, towers[0], towers[2], towers[1])                                                   

############
# End Game #
############
print()
print("Game Over! Thanks for Playing")
print()