#printing the game board
#choose player input
#checking for a win or a tie
#switching the player
#playing with the computer
#checking for a win or a tie again

import random

board = ["-","-","-",
        "-","-","-"
        "-","-","-"]

current_Player =  "x"
winer = None
game_running =  True

#printing the game board

def printBoard(board):
    print(board [0] + "|" + board[1] + "|" + board[2])
    print("______")
    print(board [3] + "|" + board[4] + "|" + board[5])
    print("______")
    print(board [6] + "|" + board[7] + "|" + board[8])
    printBoard(board)


# choose player input

def playerinput(board):
    inp = int(input("Enter a number from 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_Player
    else:
        print("Sorry player is already placed in the spot!")


#check for a win or a tie

def check_horizon (board):
    global winner
    if board[0] == board[1] == board[2] and board[1]!="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!="-":
        winner = board[6]
        return True


def check_row (board):
    global winner
    if board[0] == board[3]== board[6] and board[0]!="-":
        winner = board[0]
        return True
    elif board[1] == board [4] == board[7] and board[1] !="-":
        winner = board[1] 
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner = board[2]
        return True

def check_diag (board):
    global winer
    if board [0] == board[4] == board[3] and board[0] != "-":
        winner = board [0]
        return True
    elif board [2] == board[4] == board[6] and board[2] != "-":
        winner = board [2]
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        printboard (board)
        print("It is a tie!")
        game_running = False


#playing with computer
while current_Player == "0":
    position = random. randint(0,8)
    if board[position] == "-":
        board[position] = "0"
        switch_player()
        


def check_win():
    if check_diag(board) or check_horizon(board) or check_row(board):
        print(f"The winner is {winner}")




# switching player

def switch_player():
    global current_Player
    if current_Player == "x":
        current_Player = "O"
    else:
        current_Player = "x"

while game_running:
    printBoard (board)
    playerinput(board)
    check_win()
    check_tie(board)
    switch_player()
    check_win()
    check_tie(board)
    













