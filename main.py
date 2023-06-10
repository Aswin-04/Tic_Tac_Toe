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
List1 = []
draw_count = []

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


def switch(player):
    """" Switching players. """
    if player ==  List1[0]:
        return "X"
    else:
        return "O"
    

def get_Input(player_0):
    """ Getting Input from player 1. """
    print(f"{player_0}'s turn!")
    while True:
        try:
            inp = int(input("Enter a number from (1-9): "))
            return inp
        except:
            print("Invalid input! ")
    

def check_win_or_draw():
    """ Checking for win/draw. """

    #checking horizontally for a match
    count = 0
    for i in range(SIZE):
        if List[count] == "-" or List[count+1] == "-" or List[count+2] == "-":
            count+=SIZE
            continue
        else:
            if List[count] == List[count+1] and List[count] == List[count+2]:
                if List[count] ==  "X":
                    count+=SIZE
                    return f"{List1[0]} wins the game"
                
                else:
                    count+=SIZE
                    return f"{List[1]} wins the game"
                
    #checking vertically for a match
    count = 0
    for i in range(SIZE):
        if List[count] == "-" or List[count+SIZE] == "-" or List[count+SIZE*2] == "-":
            count+=1
            continue
        else:
            if List[count] == List[count+SIZE] and List[count] ==  List[count+SIZE*2]:
                if List[count] == "X":
                    count+=1
                    return f"{List1[0]} wins the game"
                else:
                    count+=1
                    return f"{List[1]} wins the game"

    #checking diagonally for a match
    Mid_val = 4
    for i in range(SIZE):
        if List[Mid_val] == "-":
            break
        else:
            if List[Mid_val] == List[Mid_val-Mid_val] and List[Mid_val] == List[Mid_val+Mid_val]:
                if List[Mid_val] == "X":
                    return f"{List1[0]} wins the game"
                else:
                    return f"{List[1]} wins the game"
                
            if List[Mid_val] == List[Mid_val-2] and List[Mid_val] == List[Mid_val+2]:
                if List[Mid_val] == "X":
                    return f"{List1[0]} wins the game"
                else:
                    return f"{List1[1]} wins the game"
                
    draw_count.append(1)
    if len(draw_count) == 8:
        return "Match draw"
    else:
        return "\n"








def disp_table(current_player = None, Input = 0):
    """ Update and display the table. """

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





""" Main function"""
def main():

    user_prompt()
    p1 = get_name("Player1")
    List1.append(p1)
    p2 = get_name("Player2")
    List1.append(p2)
    disp_table()

    while True:
        Input = get_Input(p1)
        disp_table(p1, Input)
        print(check_win_or_draw())
        Input = get_Input(p2)
        disp_table(p2, Input)
        print(check_win_or_draw())


    




if __name__ == "__main__":
    main()