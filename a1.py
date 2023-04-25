"""
CSSE1001 
Semester 2, 2022
"""
from a1_support import *


# Fill these in with your details
__author__ = "Yizhu Zhou"
__email__ = "yizhu.zhou@uqconnect.edu.au"
__date__ = "14/08/2022"


# Write your functions here

board_one = "68513294773459821621976485392687153485134967247325618956842739134291576819768342 "
board_two = "68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4  "
board_three = [
[6, 8, 5, 1, 3, 2, 9, 4, 7],
[7, 3, 4, 5, 9, 8, 2, 1, 6],
[2, 1, 9, 7, 6, 4, 8, 5, 3],
[9, 2, 6, 8, 7, 1, 5, 3, 4],
[8, 5, 1, 3, 4, 9, 6, 7, 2],
[4, 7, 3, 2, 5, 6, 1, 8, 9],
[5, 6, 8, 4, 2, 7, 3, 9, 1],
[3, 4, 2, 9, 1, 5, 7, 6, 8],
[1, 9, 7, 6, 8, 3, 4, 2, None]
]
board_four = [
[6, 8, 5, 1, 3, None, None, 4, 7],
[7, None, None, None, None, None, None, 1, None],
[None, 1, None, 7, 6, 4, None, 5, None],
[9, None, None, None, 7, None, 5, None, 4],
[8, None, 1, None, None, 9, None, 7, 2],
[4, None, 3, None, None, 6, None, None, None],
[None, None, None, 4, 2, 7, 3, 9, None],
[None, 4, None, 9, None, None, None, 6, 8],
[1, None, 7, None, None, None, 4, None, None]
]

def is_empty(position: tuple[int,int],board: Board) -> bool:
    r = position[0]
    c = position[1]
    if board[r][c] == None:
        return True
    else:
        return False
 
def num_hours() -> float:
    """
    Return the number of hours since user start to 
    """
    return 30.0

def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
    r = position[0]
    c = position[1]
    board[r][c] = value
 
def clear_position(position: tuple[int, int], board: Board) -> None:
    r = position[0]
    c = position[1]
    board[r][c] = None 

def read_board(raw_board: str) -> Board:
    switched_board = list(raw_board)  
    board1 = []
    for i in switched_board:
        if i == ' ':
            i = None
            board1.append(i)
        else:
            i = int(i)
            board1.append(i)
    board2 = []
    for n in range(0,9):
        board2.append(board1[n*9:n*9+9])#每行9个，输出完，转行
    return board2

def print_board(board: Board) -> None:
    for rid in range(9):
        row = board[rid]
        for i in range(len(row)):
            if row[i]:
                print(row[i], end="")
            else:
                print(" ", end="")
            if i == 2 or i == 5:
                print("|", end="")
            elif i == 8:
                print(" ", end="")
        print(rid)
        if rid == 2 or rid == 5:
            print("-----------")
        elif rid == 8:
            print()
    print("012 345 678")       
    """
    board_temp = []
    for n in board:
        if n == None:
            n = ' '
            board_temp.append(n)
        else:
            board_temp.append(n)
    for i, board in enumerate(board_temp):
        board.insert(3,'|')
        board.insert(7,'|')
        board.insert(11,' ')
        board.insert(12,i)
    board_temp.insert(3,'-----------')
    board_temp.insert(7,'-----------')
    board_temp.insert(11,'\n012 345 678')
    #board_temp.insert(12,'012 345 678')
    str ="".join(board_temp)    #need to import sth.
    print(str)
    """

def has_won(board: Board) -> bool:
    """
    test rows to see if match the ans
    test columns .....
    test 3*3 blocks ....

    """
    board1 = []
    board2 = []
    board3 = []
    ans = []
    ans1 = []
    ans2 = []
    w1 = 0
    w2 = 0
    w3 = 0
    for i in range(0,9):    # judge wheather there are duplicates in rows
        for j in range(0,9):
            board1.append(board[i][j])#load the board
            for x in board1 :
                if x not in ans:
                    ans.append(x)
        if ans == board1 and (None not in board1):
            w1 = 1
            board1 = []
            ans = []
        else:
            w1 = 0
            break                                                   
    for i in range(0,9):    #wheather duplicates in columns
        for j in range(0,9):
            board2.append(board[j][i])
            for x in  board2 :
                if x not in ans1:
                    ans1.append(x)
        if ans1 == board2 and (None not in board2) :
            w2 = 1
            board2 = []
            ans1 = []
        else:
            w2 = 0
            break 
    for h in [0,3,6]:   #judge wheather there are duplicates in every blocks
        for q in [0,3,6]:
            for i in range(h,h+3):
                for j in range(q,q+3):
                    board3.append(board[i][j])
                    for x in  board3 :
                        if x not in ans2:
                            ans2.append(x)
            if ans2 == board3 and (None not in board3) :
                w3 = 1
                board3 = []
                ans2 = []
            else:
                w3 = 0
                break    
    if w1 == 1 and w2 == 1 and w3 == 1:  #Meet the situation that there are no duplicates in rows, columns and 3*3 blocks.
        return True            
    else:
        return False


def main():
    board_name = input('Please insert the name of a board file: ')
    board_temp = load_board(board_name)
    board_game = read_board(board_temp)#the board that user is playing 
    board_temp2 = read_board(board_temp)
    print_board(board_game)
    while (has_won(board_game) == False):
        move = input('Please input your move: ')
        movement = move.split()# separate move into three numbers
        if move == 'H':
            print('Need help?\nH = Help\nQ = Quit\nHint: Make sure each row, column, and square contains only one of each number from 1 to 9.\n')
            print_board(board_game)
        elif move == 'Q':
            break
        else:
            if is_empty((int(movement[0]),int(movement[1])),board_temp2) == True:
                if movement[2] == 'C':  #contain invalid number
                    clear_position((int(movement[0]),int(movement[1])),board_game)
                    #print('That move is invalid. Try again!')
                    print_board(board_game)
                else:
                    update_board((int(movement[0]),int(movement[1])),int(movement[2]),board_game)
                    print_board(board_game)
            elif is_empty((int(movement[0]),int(movement[1])),board_temp2) == False:   #cannot change the original number   
                print('That move is invalid. Try again!')
                print_board(board_game)
            
    if has_won(board_game) == True: 
        print('Congratulations, you won!')
        ans = input('Would you like to start a new game (y/n)? ')
        if ans == 'y':
            main()
        elif ans == 'n':
            return

if __name__ == "__main__":
    main() 

 #D:/Python/task/a1/boards/board_one.txt
