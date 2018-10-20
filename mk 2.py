#This is Manav's program to play battleships
import random
def create_empty_board(size):
    board = []
    for x in range(size):
        board = board + [[0]*size]
    return board

def display_board(board):
    for row in board:
        for column in row:
            print("{0:<5}".format(column), end="")
        print("")
    print("")

def display_fog_board(board):
    for row in board:
        for column in row:
            if column == "X":
                print("{0:<5}".format(column), end="")
            elif column < 0:
                print("{0:<5}".format(column), end="")
            else:
                print("{0:<5}".format("?"), end="")
        print("")
    print("")

def game_over(board):
    in_play = 0
    for row in board:
        for column in row:
            if column == "X":
                in_play = in_play#because try except blocks are overrated
            elif column > 0:
                in_play = in_play + 1
    #print(in_play)
    if in_play == 0:
        print("Game Over!")
        return True
    else:
        return False

def c_place(board):
    for n in ship_config:#change this to change up to what length of ship the program will place
        vertical = random.choice([True, False])
        if vertical == True:
            while True:
                invalid = 0
                temp1 = random.randrange(n-1,len(board)-1,1)
                temp2 = random.randrange(0,len(board)-1,1)
                for m in range(n):
                    if board[temp1-m][temp2] != 0:
                        invalid = invalid + 1
                if invalid == 0:
                    break
            for m in range(n):
                board[temp1-m][temp2] = n
        else:
            while True:#shit
                invalid = 0
                temp1 = random.randrange(0,len(board)-1,1)
                temp2 = random.randrange(n-1,len(board)-1,1)
                for m in range(n):
                    if board[temp1][temp2-m] != 0:
                        invalid = invalid + 1
                if invalid == 0:
                    break
            for m in range(n):
                board[temp1][temp2-m] = n
    return board

def p_place(board):
    print("Where would you like to place your ships? (Only input the location of the bottommost/rightmost tile  of the ship)")
    for n in ship_config: 
        print(n+1,"Length Ship:")
        vertical = input("Horizontal [h] or Vertical [v]?")
        if vertical == "v":
            while True:
                invalid = 0
                while True:
                    try:
                        temp2 = int(input("Column: ({0}-{1})".format(1,len(board)))) - 1
                        temp1 = int(input("Row: ({0}-{1})".format(n+1,len(board)))) - 1
                        if temp2 >= 0 and temp2 <= len(board)-1 and temp1 >= n and temp1 <= len(board)-1:
                            break
                        else:
                            print("Ships are not allowed to exceed the boundaries of the board! Please try again.")
                    except ValueError:
                        print("That was not a valid number! Please try again.")
                for m in range(n+1):
                    if board[temp1-m][temp2] != 0:
                        invalid = invalid + 1
                if invalid == 0:
                    break
                elif invalid > 0:
                    print("Invalid placement; ships are not allowed to overlap. Please try again.")
            for m in range(n+1):
                board[temp1-m][temp2] = n+1
        else:
            while True:
                invalid = 0
                while True:
                    try:
                        temp2 = int(input("Column: ({0}-{1})".format(n+1,len(board)))) - 1
                        temp1 = int(input("Row: ({0}-{1})".format(1,len(board)))) - 1
                        if temp2 >= n and temp2 <= len(board)-1 and temp1 >= 0 and temp1 <= len(board)-1:
                            break
                        else:
                            print("Ships are not allowed to exceed the boundaries of the board! Please try again.")
                    except ValueError:
                        print("That was not a valid number! Please try again.")
                for m in range(n+1):
                    if board[temp1][temp2-m] != 0:
                        invalid = invalid + 1
                if invalid == 0:
                    break
            for m in range(n+1):
                board[temp1][temp2-m] = n+1
    return board

def p_guess(board):
    while True:
        print("Take your shot.")
        while True:
            try:
                temp2 = int(input("Column: ({0}-{1})".format(1,len(board)))) - 1
                temp1 = int(input("Row: ({0}-{1})".format(1,len(board)))) - 1
                if temp2 >= 0 and temp2 <= len(board)-1 and temp1 >= 0 and temp1 <= len(board)-1:
                    break
                else:
                    print("Guesses are not allowed to exceed the boundaries of the board! Please try again.")
            except ValueError:
                print("That was not a valid number! Please try again.")
        #print("temp1",temp1)
        #print("temp2",temp1)
        if board[temp1][temp2] == "X" or board[temp1][temp2] < 0:
            print("You have already shot that tile before!")
        elif board[temp1][temp2] == 0:
            board[temp1][temp2] = "X"
            print("You missed!","No ship at column",temp2+1,"row",temp1+1)
            return board
        elif board[temp1][temp2] != "X" and board[temp1][temp2] > 0:
            board[temp1][temp2] = 0 - board[temp1][temp2]
            print("Shot hit!","Ship at column",temp2+1,"row",temp1+1)
            return board

def c_guess(board):
    while True:
        temp1 = random.randrange(0,len(board)-1,1)
        temp2 = random.randrange(0,len(board)-1,1)
        #print("temp1",temp1)
        #print("temp2",temp1)
        if board[temp1][temp2] == 0:
            board[temp1][temp2] = "X"
            print("Computer missed!","No ship at column",temp2+1,"row",temp1+1)
            return board
        elif board[temp1][temp2] != "X" and board[temp1][temp2] > 0:
            board[temp1][temp2] = 0 - board[temp1][temp2]
            print("Computer shot hit!","Ship at column",temp2+1,"row",temp1+1)
            return board
ship_config = [3,2]
#ship_config = [5,4,3,3,2]
print("Welcome to battleships.\nThe aim of this game is to sink the computer's ships before it sinks yours.\n\n|Key:\n|A number greater than 0 = A ship of length corresponding to said number\n|0 = Empty\n|X = Miss\n|Negative number = Shot ship\n|? = Fog of War\n")
c_board = c_place(create_empty_board(5))
print("The computer has placed it's ships. Time to place yours.")
p_board = p_place(create_empty_board(5))
print("Player board:")
display_board(p_board)
print("START SHOOTING!\n")
turn = 0
while True:
    turn = turn + 1
    print("Turn",turn,"\n-----------------------------------------")
    print("Computer board:")
    display_fog_board(c_board)
    p_guess(c_board)
    if game_over(c_board) == True:
        print("You win!")
        break
    c_guess(p_board)
    print("\nPlayer Board:")
    display_board(p_board)
    if game_over(p_board) == True:
        print("Computer wins!")
        break
