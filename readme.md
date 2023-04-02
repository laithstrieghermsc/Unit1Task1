# Shuffle 
![MSC]
![laith.striegher]
 [![License][License: GPL v3]][License URL]

A classic puzzle game by Laith Striegher


<!-- ABOUT THE PROJECT -->
## About The Project
This simple shuffle game was created for Computer Science ATAR Unit 1, Task 1 Year 11

<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

To run the program you require;

One of:

![Windows 10/11]
![MacOSX]
![Debian]

With a desktop environment and

All of:

![Python3]
[![RDM][random]][random URL]
[![TKN][tkinter]][tkinter URL]
[![PIL][Pillow]][Pillow URL]

## Installation

### Windows 10/11
This will show you how to install Python3, Pip3, and Pillow on Windows 10/11.

Step 1: Download Python3
* Go to the Python download page and click on the "Download Python 3.x.x" button (x.x.x represents the latest version).
* Scroll down and select the appropriate version for your operating system (32-bit or 64-bit).
* Click on the "Download" button to start the download.

Step 2: Install Python3
* Double-click the downloaded file to start the installation process.
* Select "Add Python X.X to PATH" (X.X represents the version number) and click on the "Customize installation" button.
* Choose the components you want to install and click on the "Next" button.
* Select the installation directory and click on the "Install" button.
* Wait for the installation to complete.

Step 3: Download Pip3
* Go to the [Pip download page](https://bootstrap.pypa.io/get-pip.py) and download the "get-pip.py" file.
* Save the file to your computer.

Step 4: Install Pip3
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Right-click on the "Command Prompt" option and select "Run as administrator".
* Navigate to the directory where the "get-pip.py" file is saved using the "cd" command (e.g. `cd C:\Users\Username\Downloads`).
* Type `python3 get-pip.py` and press "Enter".
* Wait for the installation to complete.

Official installation guides [here](https://pip.pypa.io/en/stable/installation/)

Step 5: Download Pillow
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Right-click on the "Command Prompt" option and select "Run as administrator".
* Type `pip install pillow` and press "Enter".
* Wait for the installation to complete.

Step 6: Verify the Installation
* Open the command prompt by pressing the "Windows" key and typing "cmd".
* Type `python3` and press "Enter" to open the Python interpreter.
* Type `import pillow` and press "Enter".
* If no error message appears, Pillow has been installed successfully.

You have successfully installed Python3, Pip3, and Pillow on your Windows 10/11 system.


### Debian
Installing Python3 and pip3 on Debian

Step 1. First, update the package list using the following command:
```sh
sudo apt update
```

Step 2. Once the update process completes, install Python3 and pip3 by running the following command:
```sh
sudo apt install python3 python3-pip
```

Step 3. After the installation process completes, verify the installation of Python3 and pip3 using the following commands:
```sh
python3 --version
pip3 --version
```

Installing Pillow on Debian

Step 1. Install the required dependencies for Pillow using the following command:
```sh
sudo apt install libjpeg-dev zlib1g-dev libtiff-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
```

Step 2. Once the dependencies are installed, install Pillow using pip3:
```sh
sudo -H pip3 install Pillow
```

Step 3. After the installation process completes, verify the installation of Pillow using the following command:
```sh
python3 -c "import PIL; print(PIL.__version__)"
```

Pillow is now successfully installed on your Debian system.


### MacOSX

Step 1. Check if Python3 is already installed on your system by typing the following command in Terminal:
```sh
python3 --version
```

Step 2. If Python3 is not installed, download the latest version from the [official Python website](https://www.python.org/downloads/)

Step 3. Once the download is complete, double-click on the downloaded file to launch the Python installer and follow the instructions to complete the installation process.

Step 4. Check if pip3 is installed by typing the following command in Terminal:
```sh
pip3 --version
```

Step 5. If pip3 is not installed, download the get-pip.py script by typing the following command in Terminal:
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Step 6. Once the download is complete, navigate to the directory where the get-pip.py script is saved and run the following command in Terminal:
```sh
sudo python3 get-pip.py
```

Step 7. After pip3 is installed, you can use it to install Pillow by typing the following command in Terminal:
```sh
sudo pip3 install pillow
```

Step 8. Pillow should now be installed on your system. You can check its version by typing the following command in Terminal:
```sh
python3 -c "import PIL; print(PIL.version)"
```

That's it! You now have Python3, pip3, and Pillow installed on your MacOSX system.

<!-- USAGE EXAMPLES -->
## Usage

### logic.py

This code implements the logic of the Shuffle game, which is a tile puzzle game where a player moves numbered tiles on a board to form a particular pattern or sequence.
This file can be used by importing it into other Python scripts.

The `logic` class defines the game's logic and contains several methods to manipulate the game board. The class has the following methods:

#### \_\_init__(board_size, self_start_enabled)

The `__init__(board_size=3, self_start_enabled=True)` method is a constructor method in Python classes. It is called when an object of the class is created. In this specific code, `__init__` initializes the `logic` class by setting its `board_size` attribute to the value passed in the `board_size` parameter (which defaults to 3 if no value is passed), and its `game_board` attribute to `None`.

If the optional `self_start_enabled` parameter is `True` (which is also the default value), `initialize_game_board()`, `shuffle_game_board()`, and `start_game()` methods are called to create a complete board, shuffle it using the `shuffle` method, and then `start_game` the game. If `self_start_enabled` is `False`, these methods are not called, and it is up to the user to call them manually.

Overall, `__init__` initializes the attributes of the `logic` class, and if specified, sets up the game board and shuffles it, ready to start_game playing the game.

#### initialize_game_board()

The `initialize_game_board()` method in the logic class of the given program creates a new game board by calling the `get_complete_game_board()` method, which returns a complete, ordered board. The ordered board is then assigned to the `game_board` instance variable of the `logic` object, thus creating a new game board.

In summary, `initialize_game_board()` is responsible for initializing a new game board with an ordered state.

#### shuffle_game_board(moves)

The `shuffle_game_board(moves)` method in this Python program is responsible for shuffling the board game's pieces randomly based on the number of moves specified by the `moves` parameter.

It uses a while loop to repeat the shuffling process until the specified number of moves have been made. Within each iteration of the while loop, the method chooses a random direction (0, 1, 2, or 3) and determines if the empty cell (represented by -1) can be moved in that direction. If the move is possible, it swaps the empty cell with the adjacent piece, effectively shuffling the board.

This process is repeated for the specified number of moves until the board is shuffled to the desired degree. The method returns the shuffled board.

#### move_cell_by_id(cell_id)

The `move_cell_by_id(cell_id)` method is a method of the `logic` class that is responsible for moving a given cell on the board. The method takes in a cell value as its input and uses this value to find the position of the cell on the board using the `find_cell_location` method. The method then checks if the cell can be moved in any of the four directions (up, down, left, or right) and if so, it swaps the position of the cell with the empty cell (-1) on the board. The method returns a value of 0 if the move was successful and a value of 1 if the cell cannot be moved.

#### find_cell_location(cell_id)

The method `find_cell_location(cell_id)` is a method of the `logic` class in the `logic.py` program. This method is used to find the location of a cell in the `game_board` 2D list.

The input `cell_id` is the value that needs to be found in the `game_board`. The method iterates through each element of the 2D list by scanning each column and row using nested `for` loops. If the current element being scanned matches the input `cell_id`, the method returns the location of the element as a list of `[y, x]`, where `y` is the row index and `x` is the column index.

If the input `cell_id` is not found in the `game_board`, the method returns `1` as an error code.

Import the 'logic' class from 'logic.py' into your script using the following command:

#### get_complete_game_board()

The `get_complete_game_board()` method is a method defined within the `logic` class of the `logic.py`, which returns a two-dimensional list that represents the completed game board, in the form of a list of lists.

Each sub-list within the list contains integers that represent the values of the cells in the respective row of the completed game board. The method creates a new 2D list with `self.board_size` rows and `self.board_size` columns, where each cell in the game board is numbered sequentially from 0 to (board_size * board_size - 1), except for the last cell, which is set to -1.

This represents an empty cell that can be used to move adjacent cells around to solve the puzzle.

The method returns the generated 2D list as the completed game board that can be used to verify if the current game board matches the completed board, which is used to determine if the game has been completed successfully.

#### get_game_board_string()

The `get_game_board_string()` method in the `logic` class returns a string representation of the current game board. It creates a string that consists of a grid of cells that represent the game board. Each cell is either a number or an empty space, and each cell is separated by a vertical bar `|`. The method also adds a horizontal bar `-` between each row and at the top and bottom of the grid to make the grid look like a game board. The method uses the `self.board` attribute of the class to create the string, which represents the current state of the game board. The returned string can be printed to display the current state of the game board.

#### is_game_board_complete()

The method `is_game_board_complete()` in `logic.py` is a method of the `logic` class that checks if the current board state is complete by comparing it with the complete board state. It returns a boolean value `True` if the current board state is complete, i.e., if it is in the same state as the complete board, and `False` otherwise.

The `get_complete_game_board()` method creates a complete board, which is a 2D incremental list representing a completed board state of the game. This method is called by the `is_game_board_complete()` method to obtain the complete board state, which is then compared with the current board state.

The `is_game_board_complete()` method returns `True` if the current board state is equal to the complete board state, and `False` otherwise. If the current board is in the same state as the complete board, it means that the game has been completed successfully.

#### get_cell_value(row, col)

The `get_cell_value(row, col)` method in the given code is used to retrieve the value of a particular cell on the board based on its row and column indices. It takes two arguments: `row` and `col`, which represent the indices of the cell whose value is being retrieved. The method returns the value of the cell located at the given row and column indices on the current game board.

For example, if you want to retrieve the value of the cell located at row 2 and column 3, you would call `get_cell_value(2, 3)` and the method would return the value of the cell at that location on the board.

#### move_cell(row, column)

The `move_cell(row, column)` method is used to move a tile on the game board to an empty cell, if the move is valid. The method takes two arguments, `row` and `column`, which represent the coordinates of the tile to be moved.

The method first checks if the tile is a valid move, by checking if it is adjacent to the empty cell. If the move is valid, it calls the `move_cell_by_id(cell_id)` method to move the tile into the empty cell. The `move_cell_by_id` method returns 0 if the move is successful.

If the move is not valid, the `move_cell` method returns 1.

#### start_game()

The method `start_game()` is a method of the `logic` class that represents the game interface. This method allows the user to play the game by displaying the board and asking the user for input on which cell to move.

The method starts with an infinite loop that only exits when the game is complete. Within the loop, the method first prints the current state of the board using `print(self.get_game_board_string())`. The user is then prompted to input the number of the cell they want to move using `int(input("What to move: "))`. This value is passed to the `move_cell_by_id(cell_id)` method to move the selected cell.

If the `move_cell_by_id(cell_id)` method returns `0`, meaning the move was successful, the `start_game()` method prints `Moved`. If the move was unsuccessful, the method prints `Can't move that`. The loop then checks if the game is complete by calling the `is_game_board_complete()` method. If the game is complete, the method prints `Complete!` and displays the final board state using `print(self.get_game_board_string())`. The loop is then broken and the method exits.

### main.py

This is a program used to create a graphical user interface for the game. The program is implemented in Python using the `tkinter` library for creating the GUI and the logic module `logic.py` for implementing the core logic of the game.

The `shuffle` class is defined, and an object of this class is created when the program is run. The object has many attributes, including board size, window size, game title, shuffle rule, image file, background color, and more. The `shuffle_rule` attribute is used to set the number of shuffling moves for the puzzle.

The program initializes an empty list for the buttons and cell photos and a `logic` object for the game. The main `tkinter` window is created when the program is run.

The program uses the `logic` module to initialize and shuffle the game board. It then opens the image specified by the `image_location` attribute, crops and resizes it to fit the window when necessary. The class has the following methods:

#### \_\_init__(board_size, window_size, game_title, shuffle_rule, image_file, default_bg_color, complete_bg_color, exit_on_complete, override, pos_esp, highlight_thickness, photo_options)

The method `__init__([args])` is the constructor method of the `shuffle` class. It is called when an object of the class is created. It initializes the attributes of the class with the values passed as arguments or with default values.

The arguments that can be passed are:

* `board_size`: an integer value to set the size of the board. The default value is 3.
* `window_size`: an integer value to set the size of the window. The default value is 1000.
* `game_title`: a string value to set the title of the game window. The default value is "Shuffle Game".
* `shuffle_rule`: an integer value to set the number of shuffles the game board will undergo. The default value is None.
* `image_file`: a string value to specify the location of the image file used in the game. The default value is None.
* `default_bg_color`: a string value to set the default background color of the buttons in the game. The default value is "#f0f0f0".
* `complete_bg_color`: a string value to set the background color of the buttons when they are correctly placed. The default value is "#00ff00".
* `exit_on_complete`: a boolean value to specify whether the game window should close automatically when the game is completed. The default value is False.
* `override`: a boolean value to specify whether the game window should be decorated or not. The default value is False.
* `pos_esp`: a boolean value to specify whether the game board should contain an empty cell. The default value is False.
* `highlight_thickness`: an integer value to specify the thickness of the border around the buttons. The default value is 1.
* `photo_options`: an array of strings to specify the list of image files that can be used in the game (a random one will be selected from the list). The default value is an array of image files.

The `__init__([args])` function also initializes several other attributes of the `shuffle` class such as the button size, number of moves, list of buttons, list of cell photos, and a logic object for the game. It also creates the main tkinter window.

The `reset` function is also defined in the class to reset the attributes of the `shuffle` object.

#### reset([args])

The `reset([args])` method is part of the shuffle class and is used to reset the game by reinitializing the attributes of the class with new values.

This method takes several arguments, which are used to initialize the attributes of the class in the same way as the `__init__([args])` method.

#### start()

The `start()` method is responsible for starting the shuffle game by initializing and shuffling the game board, opening the image specified by the `image_file`, adjusting the size of the image to fit the window, creating the buttons and cell photos, and starting the main loop of the tkinter window.

In summary, this method is the main driver of the game, and it orchestrates the various components of the game to create a playable interface for the user.

#### handle_click(clicked_button)

The method `handle_click(clicked_button)`  is responsible for handling the event of clicking on a button.

When a button is clicked, this function extracts the row and column of the clicked button, and then calls the `move_cell(col, row)` method of the `game_logic` object (which is an instance of the `logic` class from the `logic` module) to move the clicked button to the empty cell. If the move is valid, it increments the `num_moves` counter.

After updating the state of the game, the function then calls the `update_buttons()` method to update the text and image of the buttons on the GUI.

#### update_buttons()

The method `update_buttons()` updates the text and images of the buttons on the game board based on the current state of the game. It is called every time a player makes a move by clicking on a button.

The function iterates through every button on the game board and gets the value of the cell at that button's position from the `game_logic` object. If the cell is not blank, the button's text is set to the value of the cell and its image is set to the corresponding image from the list of photos. If the cell is blank, the button's text is set to a blank string and its image is set to a blank image.

If the `pos_esp` attribute is set to `True`, the function checks if the current cell's location matches its location on the complete game board, and removes any highlighting if they match.

The function also checks if the game board is complete and sets the background color of the button to the complete color if it is. If the `exit_on_complete` attribute is set to `True`, the function terminates the program.

### run.py

The purpose of this program is to run the game and implement classes. It imports the `main` module and creates a game instance with specific configurations such as board size, window size, title, shuffle rule, colors, photos, and more. It then starts the game and runs it in an infinite loop, resetting the game after each completion.

## Usage

The following details how you can run the game without the `run.py` template

### Usage with user interface (main.py)
#### Here are some usage implementation examples for the "shuffle" class:

* Create a new instance of the "shuffle" class with default settings and start the game:

```python
from main import shuffle
game = shuffle()
game.start()
```
* Create a new instance of the "shuffle" class with custom settings and start the game:

```python
from main import shuffle
game = shuffle(board_size=4, window_size=1200, game_title="My Shuffle Game", shuffle_rule=100, image_file="myimage.jpg",
               default_bg_color="#000000", complete_bg_color="#ffffff", exit_on_complete=True)
game.start()
```

* Reset the settings of an existing game instance and start a new game:

```python
game.reset(board_size=5, window_size=1500, game_title="My New Shuffle Game", shuffle_rule=50, image_file="newimage.jpg",
           default_color="#ffffff", complete_color="#000000", exit_on_completion=True)
game.start()
```

### Usage without graphical user interface (standalone logic.py)
#### Here are some usage examples for the `logic` class:

* Creating a new instance of the game logic class:
```python
from logic import logic
game = logic()
```
This creates a new game with a board size of 3 (the default) and enables automatic shuffling and starting of the game.

* Creating a new instance of the game logic class with a larger board:
```python
from logic import logic
game = logic(board_size=4)
```
This creates a new game with a board size of 4 and enables automatic shuffling and starting of the game.

* Initializing a game board:
```python
game.initialize_game_board()
```
This creates a new game board based on a complete board (a board with the cells in numerical order from 1 to N^2-1, with the last cell empty).

* Shuffling a game board:
```python
game.shuffle_game_board(100)
```
This shuffles the game board by making 100 random moves.

* Moving a cell on the game board:
```python
game.move_cell_by_id(5)
```
This moves the cell with value 5 by swapping it with the empty space.

<!-- LICENSE -->
## License

Distributed under the GNU Public License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[Windows 10/11]: https://img.shields.io/badge/OS-Windows%2010%2F11-ff595e?style=for-the-badge
[MacOSX]: https://img.shields.io/badge/OS-MacOSX-ff595e?style=for-the-badge
[Debian]: https://img.shields.io/badge/OS-Debian-ff595e?style=for-the-badge
[Pillow]: https://img.shields.io/badge/PYPI-PILLOW-g?style=for-the-badge&logo=data:image/png;base64,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
[Pillow URL]: https://pypi.org/project/Pillow/
[tkinter]: https://img.shields.io/badge/BUILTIN-tkinter-g?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABzElEQVQ4jYWTP28TQRDF3x6HaI8eiYgSkOyCDiS7BqREygdI0lEGJEQJ6UH2R3BN5XwC24j0vhaaIArKuMr92XlvKO5sh7NEVho9aTU7vzc7uwGd9XI06yPqo5kNXcwsRkhcWaynd8vi7Xx8srqZn3QLIPpY5DlkC5pBImiWuXRcJHcm3fS0uyEaKA5k9lAUZAYn0RbLuvk7DihOaPaL0rloZxJBbpzsGE4B4NXn2US0fZIZY9wS/1HCKfifd3OEMIBsiiqcpK+/zD7R7Ihbm1viDXURDgEhAVQBqg+QxDyR8UDUDnHbOyES7g4guYQVGVgCVgAqhinF3pqglihjTmolWntYgIflxYf8HlT2oBpQDbAepF3yswdX70eHP58DyIAAOAGPAKsjeMzAClBsCigilZiT1mt6ZT46/PECCPsA2oMtbSciwDpPRE63c7YVHM2sWQEsARaAWmXZRtXcgcdJigRjyvYk7tFsCai/obIGPC62tlv1CkC4DE8vxqH7MPz3mzm8HoDVuvc53Bqq13l4/O30/39hY7ta6xB2HaByAbf+rU8Zur7czHkz7+iQHEiWtxYIj74eg8UZVOTNRRkAvw8kITz5ftrN/wssndHnwE4jjAAAAABJRU5ErkJggg==
[tkinter URL]: https://docs.python.org/3/library/tkinter.html
[random]: https://img.shields.io/badge/BUILTIN-random-g?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABzElEQVQ4jYWTP28TQRDF3x6HaI8eiYgSkOyCDiS7BqREygdI0lEGJEQJ6UH2R3BN5XwC24j0vhaaIArKuMr92XlvKO5sh7NEVho9aTU7vzc7uwGd9XI06yPqo5kNXcwsRkhcWaynd8vi7Xx8srqZn3QLIPpY5DlkC5pBImiWuXRcJHcm3fS0uyEaKA5k9lAUZAYn0RbLuvk7DihOaPaL0rloZxJBbpzsGE4B4NXn2US0fZIZY9wS/1HCKfifd3OEMIBsiiqcpK+/zD7R7Ihbm1viDXURDgEhAVQBqg+QxDyR8UDUDnHbOyES7g4guYQVGVgCVgAqhinF3pqglihjTmolWntYgIflxYf8HlT2oBpQDbAepF3yswdX70eHP58DyIAAOAGPAKsjeMzAClBsCigilZiT1mt6ZT46/PECCPsA2oMtbSciwDpPRE63c7YVHM2sWQEsARaAWmXZRtXcgcdJigRjyvYk7tFsCai/obIGPC62tlv1CkC4DE8vxqH7MPz3mzm8HoDVuvc53Bqq13l4/O30/39hY7ta6xB2HaByAbf+rU8Zur7czHkz7+iQHEiWtxYIj74eg8UZVOTNRRkAvw8kITz5ftrN/wssndHnwE4jjAAAAABJRU5ErkJggg==
[random URL]: https://docs.python.org/3/library/random.html
[Python3]: https://img.shields.io/badge/Language-PYTHON%203-informational?style=for-the-badge
[License: GPL v3]: https://img.shields.io/badge/License-GPLv3-7b4b94.svg?style=for-the-badge
[License URL]: https://www.gnu.org/licenses/gpl-3.0.en.html
[MSC]: https://img.shields.io/badge/SCHOOL-Mindarie%20Senior%20Collage-292e71?style=for-the-badge&logo=data:image/png;base64,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
[laith.striegher]: https://img.shields.io/badge/STUDENT-Laith%20Striegher-39375b?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA1VJREFUWIXtll1oXEUUx39z0900hfqiUPpilzStLdm7oU2EtqggFmlA4psEGrHGJA1ipdntNkaEBMGWZDehlKYRtLbZ7JoqpWBTu/GDNvTB+pBGNrs3fiA09qGJVhr8SLOb/RgfNrPemw9Mq1GQ/b/cM2fOnP+Z/5wZLuSRx7+Ek+e+aVzML1aS1Bc0JMBDa+1M/TpbmSYTRmhoyEFPjbMSYNVKEPuDo1JSEPfWlApViCDz8gN3E/YJ+4MF5tj7LsAXilUjRT+AIlJkh+bGx3qHH04VrOkXycRzttX2D/fvr0gCyfvlBMAfGuv3BQ3ZHohuVRKbyc3j9r6YBGgPRJ//W6RmAn9obMN8wvfOG4f8oZiF3B8clQDDw9J25PT1maVyLusIuvoie9JiVdgstbmI23Fqm/c6LXOS7FFXVIgkUATQEYiEC222JxOJVOHhfa7lXQBf0JC+kPHKsoLnrVN2R280Z38w8F0jgO9MViFNTRw9M1qu7LHxO+/7gobs6ItJb02p8O4tPXGvBQB0BUaq5/tu3km0AkiRFWDF3gHDkPZLX419TCq9LSPlM80vln0J0H46skPTtM+8L+hrzf20Iug+G93qD1qbE6D34rcLfHmg624JUFbm3qZsl8vTb55T3107X5+L9eSkdDn/tFXcwQOnPrKu9yyQXjMPdN0tMxlG5gddOH6gSCUBUEYk0ikAysu9r43GOoWuu2fNuS4PGVXmPAJwOQ9airAUIIS2LhrtWvRmmP3Tv8ep2O6VqqjkbOZodr2cMsdLYd2wEBkKC208Wu7NN+Hy8cSuhXKVOF66tlT8puL6HoCNxXUzAFs2N0iAkuL6RWXP9UDJxjpLUodj3+qlSL4fP7XzrwpfACHZVFy76G/Zf4pcZzscbUvu+J+GwwFDQ21xi/Ppp1qvAbxa190TePeT8OeDI5821HbfAqip7pzZ7mraA6DrTRPPVh2RACePX7zqcrq/VjmqKt+caGkJxR5/rCUMsHt32y3n3GOm8MONnyYGzn2xRY1zPTB5+7cmgBTgPzY4Xtd4oernH6emAYJnPUWzGWHMhb6VTqRuAPS8c6UB5NsqxyOb1zdfGhg5Eb+b7bfJyV+mtXTKstFEIrnmjdbz9fcsWx7/W/wBc6BY0QeRxc4AAAAASUVORK5CYII=