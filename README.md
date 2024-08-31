# Tic-Tac-Toe Game

## Description
This Python script implements a simple command-line Tic-Tac-Toe game. The game allows two players to take turns marking their respective symbols (X and O) on a 3x3 grid. The game continues until one player achieves a winning combination or the game ends in a draw.

### Features

- **Two-Player Mode**: Play against a friend by taking turns.
- **Command-Line Interface**: Simple and easy-to-use interface that runs directly in your terminal.
- **ASCII Art**: Enjoy a nostalgic look with an ASCII art logo.
- **Input Validation**: Ensures valid and unique moves.

### Technologies
* Python

### Python Libs
* OS

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Run [script](main.py) in Python. 

## Usage
1. The game will start by displaying the Tic-Tac-Toe board and prompting the first player to make a move.
2. Players take turns entering a row number and a column letter (e.g., `1a`, `2b`, `3c`) to mark their respective symbol on the board.
3. The game will continue until one player achieves a winning combination (three consecutive marks in a row, column, or diagonal) or the game ends in a draw.
4. The game will display the final result (winner or draw) and then exit.

## Game Logic
The script defines the following functions to handle the game logic:

1. `update_board()`: This function updates the game board based on the player's move and displays the current state of the board.
2. `check_win()`: This function checks if a player has achieved a winning combination and returns the winner.
3. `check_draw()`: This function checks if the game has ended in a draw.

The game loop continues until a winner is determined or the game ends in a draw.

## Customization
You can customize the appearance of the Tic-Tac-Toe board by modifying the `board_string` variable in the script. The current implementation uses ASCII art to display the board, but you can replace it with a different representation if desired.
