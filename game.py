
import random

#declares an empty list that will become the board!
board = []
#creating global variables free_spaces, first_time and win
free_spaces = []
first_time = True
win = False

#func creates a board by initializing a 2D array full of 0s in the first 
#loop and then filling it up in the second loop
def create_board():
    inc = 0
    for i in range(3):
        row = [0 for i in range(3)]
        board.append(row)
        
    for r in range(3):
        for num in range(3):
            board[r][num] = inc + 1
            inc+=1

#calling the func to populate board 
create_board()

def display_board(board):
#     The function accepts one parameter containing the board's current status
#     and prints it out to the console.
    

    print(str(board[0][0]) + "   " + str(board[0][1]) + "   " + str(board[0][2]))    #prints first row
    print(str(board[1][0]) + "   " + str(board[1][1]) + "   " + str(board[1][2]))    #prints second row
    print(str(board[2][0]) + "   " + str(board[2][1]) + "   " + str(board[2][2]))    #prints third row

def enter_move(board):
    is_valid = False
    move = int(input("Enter a VALID move here: "))#prompts user to type a num into console
    
    #checks user input to make sure it is within the range of 1-9 and is an empty space on the board by
    #iterating thru free_spaces list
    for space in free_spaces:
        if move == space:
            is_valid = True
        
    #if the input is a valid number 1-9, it will look 
    #for the input value in board and place the move as O
       
    if is_valid:
        for row in range(3):
            for col in range(3):
                if board[row][col] == move:
                    board[row][col] = "O"
    else:
        print("This move is invalid. Please type a valid number that is visible on the board (no X or O)")
    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    
    global first_time, free_spaces #mentions global vars initialized before so the code runs :P
    
    if first_time: #if its the first time calling the func, it will create a list with all the available spaces
        for r in range(3):
            for c in range(3):
                free_spaces.append(board[r][c])
        first_time = False  # now works correctly

    else: #it will check the list for spaces that are solely numbers and add them to the list
        free_spaces.clear() #clears the list so the length doesn't keep increasing (very important)
        for r in range(3):
            for c in range(3):
                if board[r][c] != "X" and board[r][c] != "O":
                    free_spaces.append(board[r][c])

    return free_spaces

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    is_valid = False
    move = 0
    
    #generates a random int 1-9 and checks to see if its not taken up by another space
    #loops until available space is found
    while is_valid == False:
        move = random.randint(1,9) 
    
        for space in free_spaces:
            if move == space:
                is_valid = True #stops loop!
    
    if is_valid: #checks each spot on the board to find the corresponding num and then marks with X
        for r in range(3):
            for c in range(3):
                if board[r][c] == move:
                    board[r][c] = "X"

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # Check columns for win
    global win #global variable win
    
    for col in range(3):
        tally = 0
        for row in range(3):
            if board[row][col] == sign:
                tally += 1
        if tally == 3:
            print("Victory for:", sign)
            win = True 
            return #stops

    # Check rows
    for row in range(3):
        tally = 0
        for col in range(3):
            if board[row][col] == sign:
                tally += 1
        if tally == 3:
            print("Victory for:", sign)
            win = True
            return

    # Check diagonal (top-left to bottom-right)
    tally = 0
    for i in range(3):
        if board[i][i] == sign:
            tally += 1
    if tally == 3:
        print("Victory for:", sign)
        win = True
        return

    # Check diagonal (top-right to bottom-left)
    tally = 0
    for i in range(3):
        if board[i][2 - i] == sign:
            tally += 1
    if tally == 3:
        print("Victory for:", sign)
        win = True
        return
    

def play_game(board):
    #puts all together to make a tic tac toe game until either one wins!
    global win
    
    while win != True:
        display_board(board)
        make_list_of_free_fields(board)
        enter_move(board)
        make_list_of_free_fields(board)
        draw_move(board)
        victory_for(board, "O")
        victory_for(board, "X")
        
play_game(board)
