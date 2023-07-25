#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Tic-Tac-Toe game in Python.

Answer = str(input("wouuld you like to play with AI"))

if Answer == no:
    play_game_vs_player()
else:
    play_game_vs_ai()

play_game_vs_player()
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

board = [" " for x in range(9)]

play_game_vs_player(yes)

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    choice = int(input("Enter your move (1-9): ").strip())
    
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
        
play_game_vs_ai()

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        # Get the current player's move
        move = input("Player " + current_player + ", enter your move (1-9): ")

        # Validate the move
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move)-1] != ' ':
            print("Invalid move! Try again.")
            continue

        # Update the board
        board[int(move)-1] = current_player

        # Check if the current player has won
        if check_win(current_player):
            print_board()
            print("Player", current_player, "wins!")
            game_over = True
        # Check if it's a tie (no more empty cells)
        elif ' ' not in board:
            print_board()
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()   

