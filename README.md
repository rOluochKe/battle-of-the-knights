# Battle Knights

Solving the battle knights coding challenge with Python.

## The game

- `run.py` - Executing this file will output the end game to the command line, save it to the file `final_state.json`, and show the game turn by turn in the command line. It creates a list of moves from the text file `moves.txt`, runs the welcome and process functions for each move, and then constructs the final game state.

- `setup.py` - Defines classes for knights and items, makes instances of each class for each knight and item, and then saves these objects in lists for quick access.

- `states.py` - It generates two state templates: board state, which generates an 8x8 board in the command line with text symbols to indicate the positions of any living knights and unequipped items, and game state, which generates a string in the JSON compatible format specified in the briefing and displays the states of each knight and item.

- `art.py` - Contains a method that generates a dictionary of images to represent each potential game action.

- `move_details.py` - Determines the outcomes based on a text input of a specific move, which includes the knight moving and the direction they are going in. They include picking up an item and dropping any less valuable items already held, moving to a new place on the board or moving off the board and drowning, attacking a knight leading to the defeat of either the mover or the defender, and so on.

- `process.py` - Creates a process function to analyze the results of a move and display the relevant board state and graphics in the command line. It has a welcome function that displays the initial board state and item artwork at the beginning of the game.

## Usage

To run the game:

    python game/run.py

Moves are read in from `moves.txt`

The output is written to `final_state.json`
