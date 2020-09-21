import random

#Defining Board
board = [' ' for _ in range(10)]

#Function to return random Value from a list
def select_random(lst):
    index = random.randrange(0,len(lst))
    return lst[index]

#Function to insert moves in board
def insert_move(pos,letter):
    global board
    board[pos] = letter

#Function  to check Position is free or not
def free_space(pos):
    return board[pos] == " "

#Function to check board is full or not
def full_board():
    return not board.count(" ") > 1

#Function to check the Winner
def is_winner(board,letter):
    #Check Horizontal / Vertical / Diagonal Same Letter
    return (board[1] == letter and\
            board[2] == letter and\
            board[3] == letter) or\
           (board[4] == letter and\
            board[5] == letter and\
            board[6] == letter) or\
           (board[7] == letter and\
            board[8] == letter and\
            board[9] == letter) or \
           (board[1] == letter and\
            board[4] == letter and\
            board[7] == letter) or\
           (board[2] == letter and\
            board[5] == letter and\
            board[8] == letter) or\
           (board[3] == letter and\
            board[6] == letter and\
            board[9] == letter) or\
           (board[1] == letter and\
            board[5] == letter and\
            board[9] == letter) or\
           (board[3] == letter and\
            board[5] == letter and\
            board[7] == letter)

#Function to Print the board
def print_board(board):
    print("-"*14)
    #Row1
    print("|   |   |   |")
    print("| "+ board[1] + " | " + board[2] + " | " + board[3]+" |")
    print("|   |   |   |")
    print("-"*14)
    #Row2
    print("|   |   |   |")
    print("| "+ board[4] + " | " + board[5] + " | " + board[6]+" |")
    print("|   |   |   |")
    print("------------")
    #Row3
    print("|   |   |   |")
    print("| "+ board[7] + " | " + board[8] + " | " + board[9]+" |")
    print("|   |   |   |")
    print("-"*14)

#Function to define Computer Move
def computer_move():
    #Take Free Spaces
    possible_moves = [ x for x,letter in enumerate(board)\
                       if letter == ' ' and x !=0]
    #Stop Player from being a Winner or Get Move for Computer to become Winner
    for letter in ['0','X']:
        for move in possible_moves:
            temp_board = board[:]
            temp_board[move] = letter
            if is_winner(temp_board,letter):
                return move
    #Corners
    possible_corners = []
    #Take Available Corners
    for move in possible_moves:
        if move in [1,3,7,9]:
            possible_corners.append(move)
    #Select one random Corner if any corner is available
    if len(possible_corners) > 0:
        move = select_random(possible_corners)
        return move
    
    #Middle - If Avaialable Return Middle
    if 5 in possible_moves:
        return 5
    
    #Edges
    possible_edges = []
    #Take Available Edges
    for move in possible_moves:
        if move in [2,4,6,8]:
            possible_edges.append(move)
    #Select one random Edge if any corner is availabl
    if len(possible_edges) > 0:
        move = select_random(possible_edges)
        return move

#Function to define Player Move
def player_move():
    run = True
    while run:
        move = input("Please Select a position to enter the X between (1-9):")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False #Player Turn Done
                    insert_move(move,"X")
                else:
                    print("Sorry, Space is not free")
            else:
                print("Sorry, Please choose the position between 1-9")
        except ValueError:
            print("Please enter a valid Number")

#Function - Main Logic of Game
def main():
    print("Welcome to Tic - Tac - Toe Game") #Greeting
    print_board(board) #Print the Board
    while not full_board():
        if not is_winner(board,'0'): #If board is not Winner
            player_move() #Player Plays
            print_board(board) #Print Board
        else: #Computer Won the Game
            print("Sorry, You Lose. Computer Wins")
            break
        if not is_winner(board,'X'): #If Player is not Winner
            move = computer_move() #Get Move
            if move ==None: #If move is 0, board is full
                print("Tie Game")
            else:
                insert_move(move,'0') #Computer Plays
                print("Computer Placed 0 in",move,"position")
                print_board(board)
        else: #Player Wins
            print("You Win!!")
    if full_board(): #Board full or not
        print("Game is Tied")

#Interface of Tic-Tac-Toe
while True:
    choice = input("Do you want to Play Tic-Tac-Toe(y/n):")
    if choice == 'y' or choice == 'Y':
        board = [' ' for _ in range(10)]
        print("-"*20)
    else:
        break
    main()
    
