#                                   Tic_Tac_Toe 

#-> Prompting the user to press any key/q.

#-> Displaying the empty table filled with - .

#-> Getting Players names as input.

#-> Switch player.

#-> Getting Input from player 1.

#-> Checking for win/draw.

#-> Update and display the table.

#-> Switch player.

#-> Checking for win/draw.

SIZE = 3

List = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def user_prompt():
    """ Function prompting the user to press any key to start and q to quit """

    char = input("Press any key to start / q to quit. ")
    if char == "q":
        quit()
    else:
        pass

def get_name(p):
    """ Getting Players names as input. """
    while True:
        player_name = input(f"Enter {p}'s name: ").strip().capitalize()

        if player_name.isalpha():
            return player_name

        else:
            print("Please enter a valid name.")


def switch():
    """" Switching players. """
    pass

def get_Input(player_0):
    """ Getting Input from player 1. """
    print(f"{player_0}'s turn!")
    while True:
        try:
            inp = int(input("Enter a number from (1-9): "))
            return inp
        except:
            print("Invalid input! ")
    

def check_win_draw():
    """ Checking for win/draw. """
    pass

def disp_table():
    """ Update and display the table. """
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





""" Main function"""
def main():

    user_prompt()
    p1 = get_name("Player1")
    p2 = get_name("Player2")
    disp_table()
    Input = get_Input(p1)

    




if __name__ == "__main__":
    main()