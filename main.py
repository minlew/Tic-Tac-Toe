import os


logo = """ .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |
| |  _________   | || |     _____    | || |     ______   | | | |  _________   | || |      __      | || |     ______   | | | |  _________   | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |    |_   _|   | || |   .' ___  |  | | | | |  _   _  |  | || |     /  \     | || |   .' ___  |  | | | | |  _   _  |  | || |   .'    `.   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |      | |     | || |  / .'   \_|  | | | | |_/ | | \_|  | || |    / /\ \    | || |  / .'   \_|  | | | | |_/ | | \_|  | || |  /  .--.  \  | || |   | |_  \_|  | |
| |     | |      | || |      | |     | || |  | |         | | | |     | |      | || |   / ____ \   | || |  | |         | | | |     | |      | || |  | |    | |  | || |   |  _|  _   | |
| |    _| |_     | || |     _| |_    | || |  \ `.___.'\  | | | |    _| |_     | || | _/ /    \ \_ | || |  \ `.___.'\  | | | |    _| |_     | || |  \  `--'  /  | || |  _| |___/ |  | |
| |   |_____|    | || |    |_____|   | || |   `._____.'  | | | |   |_____|    | || ||____|  |____|| || |   `._____.'  | | | |   |_____|    | || |   `.____.'   | || | |_________|  | |
| |              | || |              | || |              | | | |              | || |              | || |              | | | |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------' """

board_string = """
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     """


# Map user inputs to positions on the board

board_positions = {
    "1a": 40,
    "1b": 46,
    "1c": 52,
    "2a": 97,
    "2b": 103,
    "2c": 109,
    "3a": 154,
    "3b": 160,
    "3c": 166
}


game_running = True
turn_number = 0


# Set environment variable in order to use clear function
os.environ["TERM"] = "xterm-color"

def clear():
    os.system('clear')


# Define function to make board update in response to user input
def update_board():
    global board_string
    global turn_number

    clear()
    print(logo)
    print(board_string)

    # Determine current player
    if turn_number % 2 == 0:
        player_number = "1"
        player_mark = "X"
    else:
        player_number = "2"
        player_mark = "O"

    board_list = list(board_string)

    user_input = input(f"Player {player_number}, type a row number, and  a column letter. E.g. '1a'\n")

    # Determine user input is valid
    while True:
        if user_input in board_positions:
            if board_list[board_positions[user_input]] == "-":
                break

        # Handle cases where input is invalid or already taken
            else:
                clear()
                print(logo)
                print(board_string)
                user_input = input("Position already taken. Try again.\n")
        else:
            clear()
            print(logo)
            print(board_string)
            user_input = input("Invalid position. Try again.\n")

    board_list[board_positions[user_input]] = player_mark
    board_string = "".join(board_list)
    print(board_string)
    turn_number += 1


# Define function to check if winning combination has been made
def check_win():
    if (
            board_string[40] == board_string[46] == board_string[52] != "-" or
            board_string[97] == board_string[103] == board_string[109] != "-" or
            board_string[154] == board_string[160] == board_string[166] != "-" or
            board_string[40] == board_string[97] == board_string[154] != "-" or
            board_string[46] == board_string[103] == board_string[160] != "-" or
            board_string[52] == board_string[109] == board_string[166] != "-" or
            board_string[40] == board_string[103] == board_string[166] != "-" or
            board_string[52] == board_string[103] == board_string[154] != "-"
    ):
        if turn_number % 2 != 0:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        return True
    else:
        return False


# Define function to check if every position on board is taken (draw)
def check_draw():
    if (
            board_string[40] != "-" and
            board_string[46] != "-" and
            board_string[52] != "-" and
            board_string[97] != "-" and
            board_string[103] != "-" and
            board_string[109] != "-" and
            board_string[154] != "-" and
            board_string[160] != "-" and
            board_string[166] != "-"
    ):
        print("Draw!")
        return True
    else:
        return False


# Call functions
while game_running:
    update_board()
    if check_win():
        game_running = False
    if check_draw():
        game_running = False
