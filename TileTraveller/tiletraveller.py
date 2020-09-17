# Player starts in tile [1,1]
# Player selects moves (n/N, e/E, s/S, w/W) and the program should print the player's travel options
#this is a change

x_start, y_start = 1, 1

north, south, east, west = 1, -1, 1, -1

def start_tile(x_hnit, y_hnit):
    victory = False
    if x_hnit == 1 and y_hnit ==1:         #1,1
        dir_map = "(N)orth"
        valid_input = "n"
    
    elif x_hnit == 1 and y_hnit == 2:      #1,2
        dir_map = "(S)outh, (E)ast, (W)est"
        valid_input = "s", "e", "w"

    elif x_hnit == 1 and y_hnit == 3:      #1,3
        dir_map = "(S)outh, (E)ast"
        valid_input = "s", "e"
    
    elif x_hnit == 2 and y_hnit == 3:      #2,3
        dir_map = "(W)est, (E)ast"
        valid_input = "w", "e"

    elif x_hnit == 2 and y_hnit == 2:      #2,2
        dir_map = "(W)est, (S)outh"
        valid_input = "w", "s"
    
    elif x_hnit == 2 and y_hnit == 1:      #2,1
        dir_map = "(N)orth"
        valid_input = "n"

    elif x_hnit == 3 and y_hnit == 1:      #3,1
        dir_map = "(N)orth"
        valid_input = "n"
        victory = True

    elif x_hnit == 3 and y_hnit == 2:      #3,2
        dir_map = "(N)orth, (S)outh"
        valid_input = "n", "s"

    elif x_hnit == 3 and y_hnit == 3:      #3,3
        dir_map = "(W)est, (S)outh"
        valid_input = "w", "s"
    return dir_map, valid_input, victory

def dir_invalid():
    print("Not a valid direction!")


def play(my_dir, valid_dir, x, y):
    
    if(my_dir in valid_dir):

        if my_dir == "s" or my_dir == "n":
            y += int(my_dir)
        
        else: 
            x += int(my_dir)
    
    else:
        dir_invalid
    
    return x, y

def input(valid_dir):

    dir = input("Direction: ").lower()

    while dir not in valid_dir:
        dir_invalid()
        dir = input("Direction: ").lower()
    return dir

def guide(possible_dir, victory):
    
    if victory = True:
        print("Victory!")
    else:
        print("You can travel: ", possible_dir)


