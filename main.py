#                                                     Tic_Tac_Toe 

import sys

"Size of the table"
SIZE = 3

"List for storing the contents of the table"
List = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

"List which stores the names of the players"
List1 = []

"List which stores the Input values to avoid repitition"
List2 = []

"Counts the total no.of inputs to exit the program when match is in tie"
draw_count = []

        #-------------------------------------------------------------------#

def user_prompt():
    " Function prompting the user to press any key to start and q to quit "

    char = input("Press any key to continue / q to quit. ")
    if char == "q":
        sys.exit()
    else:
        pass

        #-------------------------------------------------------------------#

def get_name(p):
    " Getting Players names as input. "

    while True:
        player_name = input(f"Enter {p}'s name: ").strip().capitalize()

        if player_name.isalpha():
            return player_name

        else:
            print("Please enter a valid name.")

        #-------------------------------------------------------------------#

def switch(player):
    " Switching players. "

    if player ==  List1[0]:
        return "X"
    else:
        return "O"
    
        #-------------------------------------------------------------------#

    
def get_Input(player_0):
    """ Getting Input from player 1. """

    print(f"{player_0}'s turn!")
    while True:
        try:
            inp = int(input("Enter a number from (1-9): "))
            if len(List2) == 0:
                List2.append(inp)
                return inp
            
            elif len(List2) >= 1:
                if inp not in List2:
                    List2.append(inp)
                    return inp
                else:
                    print("Invalid Input! The entered input's place is already occupied\n")
                    continue

        except:
            print("Invalid input! ")

        #-------------------------------------------------------------------#

    
def check_Win_or_Tie():
    " Checking for Win/Tie. "

    "checking horizontally for a match"
    count = 0
    for i in range(SIZE):
        if List[count] == "-" or List[count+1] == "-" or List[count+2] == "-":
            count+=SIZE
            continue
        else:
            if List[count] == List[count+1] and List[count] == List[count+2]:
                if List[count] ==  "X":
                    count+=SIZE
                    print(f"{List1[0]} wins the game")
                    sys.exit("Game over.")
                
                
                else:
                    count+=SIZE
                    print(f"{List1[1]} wins the game")
                    sys.exit("Game over.")                

                
    "checking vertically for a match"
    count = 0
    for i in range(SIZE):
        if List[count] == "-" or List[count+SIZE] == "-" or List[count+SIZE*2] == "-":
            count+=1
            continue
        else:
            if List[count] == List[count+SIZE] and List[count] ==  List[count+SIZE*2]:
                if List[count] == "X":
                    count+=1
                    print(f"{List1[0]} wins the game")
                    sys.exit("Game over.")                
                else:
                    count+=1
                    print(f"{List1[1]} wins the game")
                    sys.exit("Game over.")                

    "checking diagonally for a match"
    Mid_val = 4
    for i in range(SIZE):
        if List[Mid_val] == "-":
            break
        else:
            if List[Mid_val] == List[Mid_val-Mid_val] and List[Mid_val] == List[Mid_val+Mid_val]:
                if List[Mid_val] == "X":
                    print(f"{List1[0]} wins the game")
                    sys.exit("Game over.")
                else:
                    print(f"{List1[1]} wins the game")
                    sys.exit("Game over.")                
                
            if List[Mid_val] == List[Mid_val-2] and List[Mid_val] == List[Mid_val+2]:
                if List[Mid_val] == "X":
                    print(f"{List1[0]} wins the game")
                    sys.exit("Game over.")                
                else:
                    print(f"{List1[1]} wins the game")
                    sys.exit("Game over.")
                
    draw_count.append(1)
    if len(draw_count) >= 8:
        print("Its a Tie :( ")
        sys.exit("Game over.")
    else:
        print(end = "")

        #-------------------------------------------------------------------#

def disp_table(current_player = None, Input = 0):
    " Update and display the table. "

    if Input != 0:
        key = switch(current_player)
        List[Input-1] = key

    num = 0
    print()
    for i in range(SIZE):
        for j in range(SIZE):
            if j < 2:
                print(List[num], end = " | ")
                num+=1
            else:
                if i < 2:
                    print(List[num], end = " ")
                else:
                    print(List[num])
                num+=1
        if i < 2:
            print("\n----------")
        else:
            print()

        #-------------------------------------------------------------------#

""" Main function """
def main():

    " Prompting the user to enter any key to play/ q to quit. "
    user_prompt()

    " Prompting the user to enter the name of player_1 and storing the player's name in p1 "
    p1 = get_name("Player_1")

    " Adding p1 to List1 "
    List1.append(p1)

    " Prompting the user to enter the name of player_2 and storing the player's name in p2 "
    p2 = get_name("Player_2")

    " Adding p2 to List1 "
    List1.append(p2)

    " Displaying empty table "
    disp_table()

    " looping over some statements "
    while True:

        "  Getting Input from Player_1 "
        Input = get_Input(p1)

        " Displaying the table "
        disp_table(p1, Input)

        " Checking for win or tie "
        check_Win_or_Tie()

        " Getting Input from Player_2 "
        Input = get_Input(p2)

        " Displaying the table "
        disp_table(p2, Input)

        "  Checking for win or tie "
        check_Win_or_Tie()

        #-------------------------------------------------------------------#

if __name__ == "__main__":
    main()

        #---------------------------X The-end X-----------------------------#
