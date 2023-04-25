"""
CSSE1001 
Support File
Semester 2, 2022
"""
from typing import Optional

Board = list[list[Optional[int]]]

# Constants


HELP = "H" 
QUIT = "Q"
CLEAR = "C"

VERTICAL_WALL = "|"
HORIZONTAL_WALL = "-"
BLANK = " "

START_GAME_PROMPT = "Please insert the name of a board file: "
INPUT_PROMPT = "Please input your move: "
INVALID_MOVE_MESSAGE = "That move is invalid. Try again!"
WIN_MESSAGE = "Congratulations, you won!"
NEW_GAME_PROMPT = "Would you like to start a new game (y/n)? "
HELP_MESSAGE = "Need help?\nH = Help\nQ = Quit\nHint: Make sure each row, column, and square contains only one of each number from 1 to 9."


# Provided Functions
def load_board(filename: str) -> str:
    """ Reads a board file and creates a string containing all the rows in order.

    Parameters:
        filename: The path to the game file

    Returns:
        A single string containing of all rows in the board.

    >>> load_board("../boards/board_one.txt")
    '68513  477      1  1 764 5 9   7 5 48 1  9 724 3  6      42739  4 9   681 7   4  '
    """
    board = ""
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('-'):
                line = line.replace("|","")
                line = line.replace("\n","") # BW file.readlines() should do this
                board += line
    return board
