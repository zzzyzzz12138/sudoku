# Sudoku Puzzle Game (Text-Based)

This is a Python-based implementation of the classic 9x9 Sudoku puzzle, developed as part of the CSSE1001/CSSE7030 course assignment.

## 📌 Features

- Load Sudoku boards from file (`.txt` format)
- Fill in cells, clear user-entered values
- Prevent modification of original cells
- Detect game completion and validate winning state
- Text-based board display and interactive prompt
- Help and Quit commands supported
- Replay feature after game end

## 🕹️ How to Play

1. Run `a1.py` in Python 3.10 environment.
2. Enter the name of a board file from the `boards/` folder (e.g., `boards/board_one.txt`).
3. Follow the prompts to:
   - Insert a value: `row col value` (e.g., `0 4 3`)
   - Clear a cell: `row col C` (e.g., `1 2 C`)
   - Display help: `H`
   - Quit game: `Q`


## ✅ Game Rules

- Each row, column, and 3×3 block must contain digits from 1 to 9 with no repetition.
- You can only modify cells that were empty in the original puzzle.
- When the board is fully filled and valid, the game declares a win.

## 🧠 Functions Implemented

- `read_board(raw_board: str) -> Board`
- `update_board(position, value, board)`
- `clear_position(position, board)`
- `is_empty(position, board)`
- `print_board(board)`
- `has_won(board)`
- `main()`

## 🛠️ Requirements

- Python 3.10
- No external libraries used

