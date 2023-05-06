<p style="text-align: center; font-size:40px;"><b>Slide</b></p>

<p style="text-align: center;"> A classic puzzle game by Laith Striegher</p>

<div style="text-align: center;">

![Preview]

![MSC]
![laith.striegher]  
[![License][License: GPL v3]][License URL] 

</div>

---

<div style="page-break-after: always;"></div>

<div style="padding-top: 30%"></div>


---

## License

Distributed under the GNU Public License. See `LICENSE.txt` for more information

---

<div style="page-break-after: always;"></div>

---
# Planning

## Objective

The slide puzzle game is a game where you have to move tiles on a board to arrange them in a certain order. The purpose of the game is to arrange the tiles in a specific pattern, usually a picture or an image.

The rules of the game are very simple. You have a board with several tiles, and one tile is missing. You can move the tiles in any direction, as long as there is an empty space for the tile to move into. The objective of the game is to move the tiles around until they are in the correct order.

The game does not have a specific winner or score. The objective is simply to solve the puzzle as quickly as possible. There are some advanced techniques and strategies that can be used to solve the puzzle faster, such as solving the puzzle in sections, or using a specific sequence of moves.

Overall, the slide puzzle game is a fun and challenging puzzle game that can be enjoyed by anyone, regardless of their skill level.

### Statagies

1.  Start by moving the closer pieces into place. Look for the pieces that are already close to their correct position, and move them there first. This will give you more space to work with as you continue solving the puzzle.
2.  Work on one section at a time. Divide the puzzle into smaller sections and solve them one by one.
3.  Look ahead to anticipate the next move. Don't just move tiles randomly - try to think ahead to the next move and how it will affect the rest of the puzzle. This can help you avoid getting stuck.
4.  Use a specific sequence of moves. There is a specific sequence of moves that can be used to solve the puzzle quickly (I am not patient enough to find them).
5.  Use trial and error. If you get stuck, sometimes a seemingly random move can lead to a breakthrough (I could make it so that you cant move the same tile twice in a row but that would be mean ( \`∀` )Ψ *evilface.

### Requirements

To program a slide puzzle game, I would need to use data types, control structures, functions, and modules.
I would also need to create algorithms for searching, sorting, and manipulating arrays and lists.

Here are some more  the basic requirements:

1.  Define the game board: I would need to create a data structure to represent the game board, such as a two-dimensional list.
2.  Generate a random puzzle: I would need to create a function to generate a random starting puzzle that is solvable. I will do this by shuffling the tiles from a valid finishing position.
3.  Create a function to move the tiles: I would need to write a function that moves the tiles on the board according to the player's input. This function would need to check if the move is legal (i.e., there is an empty space adjacent to the tile to be moved). 
4.  Check for a winning solution: I would need to create a function to check if the puzzle has been solved. This function would check if all the tiles are in the correct position.
5.  Implement a game loop: I would need to implement a loop that continually updates the game board and checks for a winning solution. This loop would continue until the player solves the puzzle or quits the game.
    

Overall, programming a slide puzzle game in Python without a GUI can be a challenging task, but it is a great way to develop your programming skills and learn more about algorithms and data structures.

## Develpment Schedule

1. Conceptualization Phase (10 minutes)
2. Design (2 hours)
   - Design Data Structures
     - Methods
     - Verification statements
   - Design and test algorithms
     - Test boundary of methods and functions etc.
     - Test object key inputs (eg use internal numbers that represent errors, non-standard inputs. Remove bugs before they occur.)
3. Logic programming / Rule development phase (2 hours)
   - Develop and debug code.
   - Group methods and connected attributes of code (create data pathways, and use same method localised variable names for readability)
   - Unit testing and use of live/test data (Data should be representative of all extremes boundaries both in and out as well as medians. eg if possible inputs are `0,1,2 ... 98,99,100` test data should be numbers `-1, 0 ,1 ,49, 50 ,51, 99, 100, 101`)
4. Interface programming / Assembling classes phase (2 hours (tkinter and pillow are dumb))
   - Assemble classes, object structures
   - Split large operation parts into different classes and files (eg launcher, interface, logic/computation)
   - Assemble cross file interfaces (eg `import`)
   - Decide object structures and variable scopes.
   - Create configuration options.
5. Launcher creation phase (3 minutes)
   - Create user tests
   - Create object tests and startup files/scripts
6. Evaluation (4 weeks)
   - Use data that tests all pathways of the algorithm
   - Test boundary conditions / data ranges
   - Desk checking / trace tables
   - Check errors
     - Syntax errors
       - Misspelling of keywords
       - Invalid formatting and use of keywords
     - Runtime errors
       - Errors during program runtime
       - Arithmatic error (x/0 etc)
       - Uninitiated variables
       - Adding different data types
       - NoneType Objects
     - Logic errors
       - Unexpected results
       - Statements not satisfying when meant to
       - Statements satisfying when not meant to
       - Program is functional but inaccurate
     - Add debugging statements
       - Interrogate variables
       - Add print statements to show variables
   - User acceptance testing
   - Developer retrospective

## Programming
### Good programming practices
All programming practices used within the development of the game will be marked with a check of used or empty box if not.
 - [x] Validate user input before processing
   - All user input that could break the program are:
     - Immobile button (Covered by `if` statements that check if a given tile is surrounded or on an edge, as well as users inability to press a non-existent button.)
     - Immobile tile id (Covered by `if` statements that check if a given tile is surrounded or on an edge.)
     - Tile id out of possible range (Covered by `if statements that check if a given tile is within applicable range.)
     - Non integer given as tile id by user (Covered by `try` `except` statements that try to convert input to integer and ask user to input proper data.)
   - No string are required by user so format checking is unnecessary.
 - [x] Use of meaningful variable and method names
 - [x] Use of comments for readability and maintenance
   - Satisfied in python files helping:
     - Clarity
     - Maintenance
     - Collaboration (Less than others)
     - Debugging
 - [x] Use of operators
   - [x] Arithmetic
     - [x] `+`
     - [x] `-`
     - [x] `/` (Present in interface objects)
     - [x] `*`
     - [ ] `%`
   - [x] Relational
     - [x] `==`
     - [x] `!=`
     - [x] `>`
     - [x] `<`
     - [x] `<=`
     - [x] `>=`
   - [x] Logical
     - [x] `and`
     - [x] `or`
     - [x] `not`
 - [x] Appropriate use of control structures.
   - Program ensures verification at all modules using:
     - [x] `if`
     - [x] `else if` (These control structures are not used explicitly, however are effectively used through `return` and `continue` statements which have the exact same function and use making explicit `else if` statements redundant.)
     - [x] `else`
     - [x] `while`
     - [x] `for`
     - [x] `try`
     - [x] `except`
     - [x] `def`
     - [x] `return`
 - [x] Proper Indentation and space
 - [x] One logical task per module
 - [x] Exception handling (used when necessary at user input and when pillow and tkinter act on the program)
 - [x] Structural algorithms
   - Satisfied in python files helping:
     - Ease of understanding
     - Ease of modification

# Data Tracing
#### Full Psudocode can be found at the bottom of the document

Due to the complexity of the program trace tables will only trace one module at a time. If you wish to see a full trace with gui see `FULL TRACE.TXT` (Do not open on old computer it is a larger file (25.1 MB (26,406,912 bytes)))
Additionally traces will be made on the python `logic` class for automation purposes. For reflection within pseudocode to find correlating lines, add 8 to the line number. This may not always be accurate.

### `shuffle_game_board`

We will start with the first significant module shuffle game board `ln. 19`.
This method is used to shuffle `game_board`. The method takes `moves` which specifies the number of times the board should be shuffled. The method swaps the empty tile with one of its neighbors randomly until it has been shuffled `moves` times. The purpose of this method is to randomize the board so that it can be used for a new game each time it is played.

We are going to assume that `3` moves will be made to shuffle a `2x2` game board. More realistic numbers would be `729` times (`3^6`) for a `3x3` game board.

| Event  | Line  | `moves`  | `game_board`      | `runs` | `moved` | `null_pos` | `direct` | `board_size` |
|--------|-------|----------|-------------------|--------|---------|------------|----------|--------------|
| call   | 32    | 3        | [[0, 1], [2, -1]] | None   | None    | None       | None     | 2            |
| line   | 33    | 3        | [[0, 1], [2, -1]] | None   | None    | None       | None     | 2            |
| line   | 34    | 3        | [[0, 1], [2, -1]] | 0      | None    | None       | None     | 2            |
| line   | 35    | 3        | [[0, 1], [2, -1]] | 0      | None    | None       | None     | 2            |
| line   | 36    | 3        | [[0, 1], [2, -1]] | 0      | False   | None       | None     | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | None     | 2            |
| line   | 38    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | None     | 2            |
| line   | 39    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 43    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 47    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 51    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 38    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 1        | 2            |
| line   | 39    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 2        | 2            |
| line   | 43    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 2        | 2            |
| line   | 47    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 2        | 2            |
| line   | 48    | 3        | [[0, 1], [2, -1]] | 0      | False   | [1, 1]     | 2        | 2            |
| line   | 49    | 3        | [[0, -1], [2, 1]] | 0      | False   | [1, 1]     | 2        | 2            |
| line   | 50    | 3        | [[0, -1], [2, 1]] | 0      | True    | [1, 1]     | 2        | 2            |
| line   | 37    | 3        | [[0, -1], [2, 1]] | 0      | True    | [1, 1]     | 2        | 2            |
| line   | 55    | 3        | [[0, -1], [2, 1]] | 0      | True    | [1, 1]     | 2        | 2            |
| line   | 34    | 3        | [[0, -1], [2, 1]] | 1      | True    | [1, 1]     | 2        | 2            |
| line   | 35    | 3        | [[0, -1], [2, 1]] | 1      | True    | [1, 1]     | 2        | 2            |
| line   | 36    | 3        | [[0, -1], [2, 1]] | 1      | False   | [1, 1]     | 2        | 2            |
| line   | 37    | 3        | [[0, -1], [2, 1]] | 1      | False   | [0, 1]     | 2        | 2            |
| line   | 38    | 3        | [[0, -1], [2, 1]] | 1      | False   | [0, 1]     | 2        | 2            |
| line   | 39    | 3        | [[0, -1], [2, 1]] | 1      | False   | [0, 1]     | 0        | 2            |
| line   | 40    | 3        | [[0, -1], [2, 1]] | 1      | False   | [0, 1]     | 0        | 2            |
| line   | 41    | 3        | [[0, 1], [2, -1]] | 1      | False   | [0, 1]     | 0        | 2            |
| line   | 42    | 3        | [[0, 1], [2, -1]] | 1      | True    | [0, 1]     | 0        | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 1      | True    | [0, 1]     | 0        | 2            |
| line   | 55    | 3        | [[0, 1], [2, -1]] | 1      | True    | [0, 1]     | 0        | 2            |
| line   | 34    | 3        | [[0, 1], [2, -1]] | 2      | True    | [0, 1]     | 0        | 2            |
| line   | 35    | 3        | [[0, 1], [2, -1]] | 2      | True    | [0, 1]     | 0        | 2            |
| line   | 36    | 3        | [[0, 1], [2, -1]] | 2      | False   | [0, 1]     | 0        | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 38    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 39    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 43    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 47    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 51    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 38    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 1        | 2            |
| line   | 39    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 43    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 47    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 51    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 37    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 38    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 0        | 2            |
| line   | 39    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 43    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 47    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 51    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 52    | 3        | [[0, 1], [2, -1]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 53    | 3        | [[0, 1], [-1, 2]] | 2      | False   | [1, 1]     | 3        | 2            |
| line   | 54    | 3        | [[0, 1], [-1, 2]] | 2      | True    | [1, 1]     | 3        | 2            |
| line   | 37    | 3        | [[0, 1], [-1, 2]] | 2      | True    | [1, 1]     | 3        | 2            |
| line   | 55    | 3        | [[0, 1], [-1, 2]] | 2      | True    | [1, 1]     | 3        | 2            |
| line   | 34    | 3        | [[0, 1], [-1, 2]] | 3      | True    | [1, 1]     | 3        | 2            |
| return | 34    | 3        | [[0, 1], [-1, 2]] | 3      | True    | [1, 1]     | 3        | 2            |

As you can see the board has been randomly shuffled three moves in a way that ensures that the board is possible to complete.

### `move_tile_by_id`

The method `move_tile_by_id` is to move a tile with a given `tile_id` to an adjacent empty tile on the game board for text input.

The method first finds the location of the tile on the game board using the `find_tile_location` method. It then checks if the tile is not on the bottom, right, top, or left edges of the board, and if it is adjacent to an empty tile. If these conditions are satisfied, the method moves the tile to the empty tile by flipping the values of the two tiles. The method returns 0 to indicate that the move was successful, and 1 if the tile cannot be moved.

This method is used as part of the game logic to enable a player to move tiles on the game board and solve the puzzle.

We are going to assume that `3` moves will be made to shuffle a `2x2` game board, and we will attempt to move tile 1, given the random shuffle is `[[0, -1], [2, 1]]`.

| Event  | Line  | `tile_id` | `game_board`      | `tile_pos` |             |
|--------|-------|-----------|-------------------|------------|-------------|
| call   | 58    | 1         | [[0, -1], [2, 1]] | None       |
| line   | 60    | 1         | [[0, -1], [2, 1]] | None       |
| line   | 61    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 63    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 67    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 71    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 72    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 73    | 1         | [[0, -1], [2, 1]] | [1, 1]     |
| line   | 74    | 1         | [[0, 1], [2, -1]] | [1, 1]     |
| return | 74    | 1         | [[0, 1], [2, -1]] | [1, 1]     | returned: 0 |

As you can see tile `1` had exchanged its position with the empty tile `-1` and returned `0` to represent its success.

Now lets see what will happen if we try to move tile `0` from the finishing position of the last trace.

| Event  | Line | `tile_id` | `game_board`      | `tile_pos` | returned    |
|--------|------|-----------|-------------------|------------|-------------|
| call   | 58   | 0         | [[0, 1], [2, -1]] | None       |
| line   | 60   | 0         | [[0, 1], [2, -1]] | None       |
| line   | 61   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 63   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 64   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 67   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 68   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 71   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 75   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| line   | 79   | 0         | [[0, 1], [2, -1]] | [0, 0]     |
| return | 79   | 0         | [[0, 1], [2, -1]] | [0, 0]     | returned: 1 |

As you can see no changes were made to the game board as `0` has no place to move. the method also returned one representing a failure to complete task.

### `find_tile_location`

The purpose of the `find_tile_location` module is to locate the position of a given tile on the game board.

The module takes a `tile_id` as an argument, which is the identifier of a tile on the game board. It then iterates through each row and column of the board to find the location of the tile that matches the given `tile_id`. Once the location of the tile is found, the module returns a list containing the `y` and `x` coordinates of the tile on the board.

If the given `tile_id` cannot be found on the board, the module returns an error code of 1. This error code may indicate that the tile is not present on the board, or that there is an issue with the input value of `tile_id`.

The following trace table assumes a `board_size` of 5 and a random shuffle of:

```text
[[ 7,21, 8,16, 1],
 [-1,11, 9, 5,13],
 [15,22, 3, 2, 4],
 [12,14, 6,19,20],
 [23,18,10,17, 0]]
```

| Event  | Line | `tile_id` | `game_board`                                                                                                                    | `board_size` | `x`  | `y`  | returned |
|--------|------|-----------|---------------------------------------------------------------------------------------------------------------------------------|--------------|------|------|----------|
| call   | 82   |  11       |  [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`] | 5            | None | None |
| line   | 83   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | None | None |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | None | 0    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 0    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 0    | 0    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 1    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 1    | 0    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 2    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 2    | 0    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 3    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 3    | 0    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 4    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 4    | 0    |
| line   | 83   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 4    | 0    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 4    | 1    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 0    | 1    |
| line   | 84   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 0    | 1    |
| line   | 85   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 1    | 1    |
| line   | 86   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 1    | 1    |
| return | 86   | 11        | [`[7, 21, 8, 16, 1]`,<br>` [-1, 11, 9, 5, 13]`,<br>` [15, 22, 3, 2, 4]`,<br>` [12, 14, 6, 19, 20]`,<br>` [23, 18, 10, 17, 0]`]  | 5            | 1    | 1    | [1,1]    |

As you can see the method iterated through the board and found `11` at (1,1) and returned so in the format `[y,x]` (`[1,1]`).

Now let's see what happens with a `board_size` of 3 and a random shuffle of:

| Event  | Line | `tile_id` | `game_board`                                        | `board_size` | `x`   | `y`   | returned |
|--------|------|-----------|-----------------------------------------------------|--------------|-------|-------|----------|
| call   | 82   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | None  | None  |
| line   | 83   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | None  | None  |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | None  | 0     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 0     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 0     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 0     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 0     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 0     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 0     |
| line   | 83   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 0     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 1     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 1     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 1     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 1     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 1     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 1     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 1     |
| line   | 83   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 1     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 2     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 0     | 2     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 2     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 1     | 2     |
| line   | 85   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     |
| line   | 84   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     |
| line   | 83   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     |
| line   | 87   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     |
| return | 87   | 11        | [` [1, 4, 6]`,<br> ` [-1, 7, 5]`,<br> ` [2, 0, 3]`] | 3            | 2     | 2     | 1        |

As you can see the method iterated through the board and failed to find `11` so it returned 1 to indicate failure to find the tile. Note that with in the GUI version of the program a returned value of one is impossible as the users only being able to select existing tiles acts as a natural filter.

The method `find_tile_location_on_complete_board` will not be the subject of a trace table due to its similarity to `find_tile_location`. (15 character difference on lines `85` and `93`)

### `get_complete_game_board`

`get_complete_game_board` returns a two-dimensional list representing the complete game board, i.e., the board that the player should try to achieve.

The `complete_board` list is created as a two-dimensional incremental list, where each element in the `i`th row of the list is `board_size` times the row number plus `i`. This results in a board with the numbers 0 to board_size<sup>2</sup> - 1 arranged in a square grid.

The last value in the `complete_board` list is set to `-1`, which represents the blank tile. This is the tile that can be moved around the board during gameplay to try to solve the puzzle. From this point `complete_board` is a generated array.

Overall, the purpose of this module is to provide the initial state of the Shuffle game board before the player starts shuffling and solving the puzzle.

We are going to assume that `board_size` = 3 for the below trace table

| Event  | Line  | `complete_board`                   | `board_size`      | i      | j    | returned                           |
|--------|-------|------------------------------------|-------------------|--------|------|------------------------------------|
| call   | 98    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | None   | None |
| call   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | None   | None |
| call   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | 0      | None |
| line   | 99    | None                               | 3                 | 1      | None |
| line   | 99    | None                               | 3                 | 2      | None |
| return | 99    | None                               | 3                 | 2      | None |
| line   | 99    | None                               | 3                 | None   | 0    |
| call   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | 3      | None |
| line   | 99    | None                               | 3                 | 4      | None |
| line   | 99    | None                               | 3                 | 5      | None |
| return | 99    | None                               | 3                 | 5      | None |
| line   | 99    | None                               | 3                 | None   | 1    |
| call   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | None   | None |
| line   | 99    | None                               | 3                 | 6      | None |
| line   | 99    | None                               | 3                 | 7      | None |
| line   | 99    | None                               | 3                 | 8      | None |
| return | 99    | None                               | 3                 | 8      | None |
| line   | 99    | None                               | 3                 | None   | 2    |
| return | 99    | None                               | 3                 | None   | 2    |
| line   | 100   | [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  | 3                 | None   | None |
| line   | 101   | [[0, 1, 2], [3, 4, 5], [6, 7, -1]] | 3                 | None   | None |
| return | 101   | [[0, 1, 2], [3, 4, 5], [6, 7, -1]] | 3                 | None   | None | [[0, 1, 2], [3, 4, 5], [6, 7, -1]] |

As you can see a 3x3 2-dimensional array has been generated as of the return line 101 the values of the array are unchanging. It is now this array alone that will be used to verify the completion of the game board.

### `get_game_board_string`

This module defines a method called `get_game_board_string()` that returns a string representation of the game board. The purpose of this module is to provide a visual representation of the current state of the game board, which can be useful for debugging or for displaying the game board to the user.

The method creates a string variable `strike` which is used to separate the rows of the game board with a horizontal line. It then creates a string variable `string` that begins with the strike separator.

The method then uses nested loops to iterate over each tile in the game board and add its contents to the string representation. If the tile is empty (i.e., has a value of -1), the module adds two spaces to the string representation. Otherwise, it adds the value of the tile as a two-digit string with a vertical bar character.

Finally, the module appends the separator to the string and returns it as the final output. Overall, the module helps to visualize the current state of the game board by creating a formatted string that separates the rows of the game board with a horizontal line and adds vertical bars around the tile values.

A simple game board with the default size of three will be used 

| Event  | Line | `board_size` | strike       | string                                                                                                                       | i    | j    | Returned                                                                                                                      |
|--------|------|--------------|--------------|------------------------------------------------------------------------------------------------------------------------------|------|------|-------------------------------------------------------------------------------------------------------------------------------| 
| call   | 104  | 3            | None         | None                                                                                                                         | None | None |
| line   | 105  | 3            | None         | None                                                                                                                         | None | None |
| line   | 106  | 3            | `-`          | None                                                                                                                         | None | None |
| line   | 107  | 3            | `-`          | None                                                                                                                         | None | None |
| line   | 106  | 3            | `----`       | None                                                                                                                         | None | None |
| line   | 107  | 3            | `----`       | None                                                                                                                         | None | None |
| line   | 106  | 3            | `-------`    | None                                                                                                                         | None | None |
| line   | 107  | 3            | `-------`    | None                                                                                                                         | None | None |
| line   | 106  | 3            | `----------` | None                                                                                                                         | None | None |
| line   | 108  | 3            | `----------` | None                                                                                                                         | None | None |
| line   | 109  | 3            | `----------` | `----------`                                                                                                                 | None | None |
| line   | 110  | 3            | `----------` | `----------`                                                                                                                 | 0    | None |
| line   | 111  | 3            | `----------` | `----------`                                                                                                                 | 0    | 0    |
| line   | 112  | 3            | `----------` | `----------`                                                                                                                 | 0    | 0    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02`                                                                                                       | 0    | 0    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02`                                                                                                       | 0    | 1    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02`                                                                                                       | 0    | 1    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01`                                                                                                   | 0    | 1    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01`                                                                                                   | 0    | 2    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01`                                                                                                   | 0    | 2    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07`                                                                                               | 0    | 2    |
| line   | 115  | 3            | `----------` | `----------`<br>`\|02\|01\|07`                                                                                               | 0    | 2    |
| line   | 109  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`                                                                             | 0    | 2    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`                                                                             | 1    | 2    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`                                                                             | 1    | 0    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`                                                                             | 1    | 0    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06`                                                                   | 1    | 0    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06`                                                                   | 1    | 1    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06`                                                                   | 1    | 1    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04`                                                               | 1    | 1    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04`                                                               | 1    | 2    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04`                                                               | 1    | 2    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05`                                                           | 1    | 2    |
| line   | 115  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05`                                                           | 1    | 2    |
| line   | 109  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`                                         | 1    | 2    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`                                         | 2    | 2    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`                                         | 2    | 0    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`                                         | 2    | 0    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00`                               | 2    | 0    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00`                               | 2    | 1    |
| line   | 114  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00`                               | 2    | 1    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  `                           | 2    | 1    |
| line   | 111  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  `                           | 2    | 2    |
| line   | 112  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  `                           | 2    | 2    |
| line   | 110  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03`                       | 2    | 2    |
| line   | 115  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03`                       | 2    | 2    |
| line   | 109  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03\|`<br>`----------`<br> | 2    | 2    |
| line   | 116  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03\|`<br>`----------`<br> | 2    | 2    |
| return | 116  | 3            | `----------` | `----------`<br>`\|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03\|`<br>`----------`<br> | 2    | 2    | `----------`<br>` \|02\|01\|07\|`<br>`----------`<br>`\|06\|04\|05\|`<br>`----------`<br>`\|00\|  \|03\|`<br>`----------`<br> |

As you can see the method iterated through the game board and inserted values into a simple ascii table to create the string.

### Others

Due to the simplicity and importance of the explanations of some methods, the following methods have been omitted from the creation of trace tables:
`is_game_board_complete` (returns `game_board == get_complete_game_board()`)
`get_tile_value` (checks what tile is in a certain location)
`move_tile` (just calls `move_tile_by_id`)
`start_game` (is a default game loop)

# Test Run `logic.py`

The following is a full console output of running logic standalone with default settings (`board_size=3`, `self_start=True`)
In this case run.py represents a file containing:
```python
import logic
i = logic.logic()
```
A test run is below. Note that strings found in between two `~` represents user input and as such `~` is not an aspect of the input or output.

```text
"python.exe" "C:\<Working Directory>\run.py" 
----------
|07|00|02|
----------
|06|04|03|
----------
|05|  |01|
----------

What to move: ~1~

Moved


----------
|07|00|02|
----------
|06|04|03|
----------
|05|01|  |
----------

What to move: ~3~

Moved


----------
|07|00|02|
----------
|06|04|  |
----------
|05|01|03|
----------

What to move: ~4~

Moved


----------
|07|00|02|
----------
|06|  |04|
----------
|05|01|03|
----------

What to move: ~6~

Moved


----------
|07|00|02|
----------
|  |06|04|
----------
|05|01|03|
----------

What to move: ~7~

Moved


----------
|  |00|02|
----------
|07|06|04|
----------
|05|01|03|
----------

What to move: ~-1~

Can't move that


----------
|  |00|02|
----------
|07|06|04|
----------
|05|01|03|
----------

What to move: ~0~

Moved


----------
|00|  |02|
----------
|07|06|04|
----------
|05|01|03|
----------

What to move: ~6~

Moved


----------
|00|06|02|
----------
|07|  |04|
----------
|05|01|03|
----------

What to move: ~1~

Moved


----------
|00|06|02|
----------
|07|01|04|
----------
|05|  |03|
----------

What to move: ~3~

Moved


----------
|00|06|02|
----------
|07|01|04|
----------
|05|03|  |
----------

What to move: ~4~

Moved


----------
|00|06|02|
----------
|07|01|  |
----------
|05|03|04|
----------

What to move: ~1~

Moved


----------
|00|06|02|
----------
|07|  |01|
----------
|05|03|04|
----------

What to move: ~6~

Moved


----------
|00|  |02|
----------
|07|06|01|
----------
|05|03|04|
----------

What to move: ~2~

Moved


----------
|00|02|  |
----------
|07|06|01|
----------
|05|03|04|
----------

What to move: ~1~

Moved


----------
|00|02|01|
----------
|07|06|  |
----------
|05|03|04|
----------

What to move: ~6~

Moved


----------
|00|02|01|
----------
|07|  |06|
----------
|05|03|04|
----------

What to move: ~2~

Moved


----------
|00|  |01|
----------
|07|02|06|
----------
|05|03|04|
----------

What to move: ~1~

Moved


----------
|00|01|  |
----------
|07|02|06|
----------
|05|03|04|
----------

What to move: ~6~

Moved


----------
|00|01|06|
----------
|07|02|  |
----------
|05|03|04|
----------

What to move: ~4~

Moved


----------
|00|01|06|
----------
|07|02|04|
----------
|05|03|  |
----------

What to move: ~3~

Moved


----------
|00|01|06|
----------
|07|02|04|
----------
|05|  |03|
----------

What to move: ~2~

Moved


----------
|00|01|06|
----------
|07|  |04|
----------
|05|02|03|
----------

What to move: ~4~

Moved


----------
|00|01|06|
----------
|07|04|  |
----------
|05|02|03|
----------

What to move: ~3~

Moved


----------
|00|01|06|
----------
|07|04|03|
----------
|05|02|  |
----------

What to move: ~2~

Moved


----------
|00|01|06|
----------
|07|04|03|
----------
|05|  |02|
----------

What to move: ~4~

Moved


----------
|00|01|06|
----------
|07|  |03|
----------
|05|04|02|
----------

What to move: ~1~

Moved


----------
|00|  |06|
----------
|07|01|03|
----------
|05|04|02|
----------

What to move: ~6~

Moved


----------
|00|06|  |
----------
|07|01|03|
----------
|05|04|02|
----------

What to move: ~3~

Moved


----------
|00|06|03|
----------
|07|01|  |
----------
|05|04|02|
----------

What to move: ~2~

Moved


----------
|00|06|03|
----------
|07|01|02|
----------
|05|04|  |
----------

What to move: ~4~

Moved


----------
|00|06|03|
----------
|07|01|02|
----------
|05|  |04|
----------

What to move: ~5~

Moved


----------
|00|06|03|
----------
|07|01|02|
----------
|  |05|04|
----------

What to move: ~7~

Moved


----------
|00|06|03|
----------
|  |01|02|
----------
|07|05|04|
----------

What to move: ~1~

Moved


----------
|00|06|03|
----------
|01|  |02|
----------
|07|05|04|
----------

What to move: ~2~

Moved


----------
|00|06|03|
----------
|01|02|  |
----------
|07|05|04|
----------

What to move: ~6~

Can't move that


----------
|00|06|03|
----------
|01|02|  |
----------
|07|05|04|
----------

What to move: ~3~

Moved


----------
|00|06|  |
----------
|01|02|03|
----------
|07|05|04|
----------

What to move: ~6~

Moved


----------
|00|  |06|
----------
|01|02|03|
----------
|07|05|04|
----------

What to move: ~2~

Moved


----------
|00|02|06|
----------
|01|  |03|
----------
|07|05|04|
----------

What to move: ~1~

Moved


----------
|00|02|06|
----------
|  |01|03|
----------
|07|05|04|
----------

What to move: ~7~

Moved


----------
|00|02|06|
----------
|07|01|03|
----------
|  |05|04|
----------

What to move: ~5~

Moved


----------
|00|02|06|
----------
|07|01|03|
----------
|05|  |04|
----------

What to move: ~4~

Moved


----------
|00|02|06|
----------
|07|01|03|
----------
|05|04|  |
----------

What to move: ~3~

Moved


----------
|00|02|06|
----------
|07|01|  |
----------
|05|04|03|
----------

What to move: ~6~

Moved


----------
|00|02|  |
----------
|07|01|06|
----------
|05|04|03|
----------

What to move: ~2~

Moved


----------
|00|  |02|
----------
|07|01|06|
----------
|05|04|03|
----------

What to move: ~1~

Moved


----------
|00|01|02|
----------
|07|  |06|
----------
|05|04|03|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|07|04|06|
----------
|05|  |03|
----------

What to move: ~3~

Moved


----------
|00|01|02|
----------
|07|04|06|
----------
|05|03|  |
----------

What to move: ~6~

Moved


----------
|00|01|02|
----------
|07|04|  |
----------
|05|03|06|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|07|  |04|
----------
|05|03|06|
----------

What to move: ~3~

Moved


----------
|00|01|02|
----------
|07|03|04|
----------
|05|  |06|
----------

What to move: ~5~

Moved


----------
|00|01|02|
----------
|07|03|04|
----------
|  |05|06|
----------

What to move: ~7~

Moved


----------
|00|01|02|
----------
|  |03|04|
----------
|07|05|06|
----------

What to move: ~3~

Moved


----------
|00|01|02|
----------
|03|  |04|
----------
|07|05|06|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|03|04|  |
----------
|07|05|06|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|03|  |04|
----------
|07|05|06|
----------

What to move: ~5~

Moved


----------
|00|01|02|
----------
|03|05|04|
----------
|07|  |06|
----------

What to move: ~7~

Moved


----------
|00|01|02|
----------
|03|05|04|
----------
|  |07|06|
----------

What to move: ~3~

Moved


----------
|00|01|02|
----------
|  |05|04|
----------
|03|07|06|
----------

What to move: ~5~

Moved


----------
|00|01|02|
----------
|05|  |04|
----------
|03|07|06|
----------

What to move: ~7~

Moved


----------
|00|01|02|
----------
|05|07|04|
----------
|03|  |06|
----------

What to move: ~6~

Moved


----------
|00|01|02|
----------
|05|07|04|
----------
|03|06|  |
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|05|07|  |
----------
|03|06|04|
----------

What to move: ~7~

Moved


----------
|00|01|02|
----------
|05|  |07|
----------
|03|06|04|
----------

What to move: ~5~

Moved


----------
|00|01|02|
----------
|  |05|07|
----------
|03|06|04|
----------

What to move: ~3~

Moved


----------
|00|01|02|
----------
|03|05|07|
----------
|  |06|04|
----------

What to move: ~6~

Moved


----------
|00|01|02|
----------
|03|05|07|
----------
|06|  |04|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|03|05|07|
----------
|06|04|  |
----------

What to move: ~7~

Moved


----------
|00|01|02|
----------
|03|05|  |
----------
|06|04|07|
----------

What to move: ~5~

Moved


----------
|00|01|02|
----------
|03|  |05|
----------
|06|04|07|
----------

What to move: ~4~

Moved


----------
|00|01|02|
----------
|03|04|05|
----------
|06|  |07|
----------

What to move: ~7~

Moved


Complete!

----------
|00|01|02|
----------
|03|04|05|
----------
|06|07|  |
----------


Process finished with exit code 0

```

# Full logic pseudocode disassembled from the logic class:
```psudocade
#########################################################################
#                                                                       #
#                        Mindarie Senior College                        #
#                            Laith Striegher                            #
#                            Task 1 - Unit 1                            #
#                                 'Slide'                               #
#                     Game Logic -- logic_pseudo.txt                    #
#                                                                       #
#########################################################################



13. board_size=3
14. self_start_enabled=True
15. 
16. MODULE initialize_game_board():
17.     game_board = get_complete_game_board()
18. END initialize_game_board
19. 
20. MODULE shuffle_game_board(moves):
21.     runs = 0
22.     WHILE runs < moves:
23.         moved = False
24.         null_pos = find_tile_location(-1)
25.         WHILE not moved:
26.             direct = random(0, 3)
27.             IF null_pos[0] != board_size - 1 and direct = 0:
28.                 game_board[null_pos[0]][null_pos[1]], game_board[null_pos[0] + 1][null_pos[1]] = game_board[null_pos[0] + 1][null_pos[1]], -1
29.                 moved = True
30.                 continue
31.             END IF
32.             IF null_pos[1] != board_size - 1 and direct = 1:
33.                 game_board[null_pos[0]][null_pos[1]], game_board[null_pos[0]][null_pos[1] + 1] = game_board[null_pos[0]][null_pos[1] + 1], -1
34.                 moved = True
35.                 continue
36.             END IF
37.             IF null_pos[0] != 0 and direct = 2:
38.                 game_board[null_pos[0]][null_pos[1]], game_board[null_pos[0] - 1][null_pos[1]] = game_board[null_pos[0] - 1][null_pos[1]], -1
39.                 moved = True
40.                 continue
41.             END IF
42.             IF null_pos[1] != 0 and direct = 3:
43.                 game_board[null_pos[0]][null_pos[1]], game_board[null_pos[0]][null_pos[1] - 1] = game_board[null_pos[0]][null_pos[1] - 1], -1
44.                 moved = True
45.                 continue
46.             END IF
47.         runs += 1
48. END shuffle_game_board
49. 
50. MODULE move_tile_by_id(tile_id):
51.     tile_pos = find_tile_location(tile_id)
52.     IF tile_pos[0] < board_size - 1:
53.         IF game_board[tile_pos[0] + 1][tile_pos[1]] = -1:
54.             game_board[tile_pos[0] + 1][tile_pos[1]], game_board[tile_pos[0]][tile_pos[1]] = tile_id, -1
55.             RETURN 0
56.         END IF
57.     END IF
58.     IF tile_pos[1] < board_size - 1:
59.         IF game_board[tile_pos[0]][tile_pos[1] + 1] = -1:
60.             game_board[tile_pos[0]][tile_pos[1] + 1], game_board[tile_pos[0]][tile_pos[1]] = tile_id, -1
61.             RETURN 0
62.         END IF
63.     END IF
64.     IF tile_pos[0] != 0:
65.         IF game_board[tile_pos[0] - 1][tile_pos[1]] = -1:
66.             game_board[tile_pos[0] - 1][tile_pos[1]], game_board[tile_pos[0]][tile_pos[1]] = tile_id, -1
67.             RETURN 0
68.         END IF
69.     END IF
70.     IF tile_pos[1] != 0:
71.         IF game_board[tile_pos[0]][tile_pos[1] - 1] = -1:
72.             game_board[tile_pos[0]][tile_pos[1] - 1], game_board[tile_pos[0]][tile_pos[1]] = tile_id, -1
73.             RETURN 0
74.         END IF
75.     END IF
76.     RETURN 1
77. END move_tile_by_id
78. 
79. MODULE find_tile_location(tile_id):
80.     FOR y IN range(0, board_size):
81.         FOR x IN range(0, board_size):
82.             IF game_board[y][x] = tile_id:
83.                 RETURN [y, x]
84.             END IF
85.     RETURN 1
86. END find_tile_location
87. 
88. MODULE find_tile_location_on_complete_board(tile_id):
89.     FOR y IN range(0, board_size):
90.         FOR x IN range(0, board_size):
91.             IF get_complete_game_board()[y][x] = tile_id:
92.                 RETURN [y, x]
93.             END IF
94.     RETURN 1
95. END find_tile_location_on_complete_board
96. 
97. MODULE get_complete_game_board():
98.     complete_board = [[i FOR i IN range(board_size * j, board_size * j + board_size)] FOR j IN range(0, board_size)]
99.     complete_board[board_size - 1][board_size - 1] = -1
100.     RETURN complete_board
101. END get_complete_game_board
102. 
103. MODULE get_game_board_string():
104.     strike = "-"
105.     FOR d IN range(0, board_size):
106.         strike += "---"
107.     string = strike + "\n"
108.     FOR i IN range(0, board_size):
109.         FOR j IN range(0, board_size):
110.             IF game_board[i][j] != -1:
111.                 string += "|" + str(game_board[i][j]).zfill(2)
112.             ELSE:
113.                 string += "|  "
114.             END IF
115.         string += "|\n" + strike + "\n"
116.     RETURN string
117. END get_game_board_string
118. 
119. MODULE is_game_board_complete():
120.     RETURN game_board = get_complete_game_board()
121. END is_game_board_complete
122. 
123. MODULE get_tile_value(row, col):
124.     RETURN game_board[row][col]
125. END get_tile_value
126. 
127. MODULE move_tile(row, column):
128.     IF game_board[column][row] >= 0 or game_board[column][row] <= board_size^2 - 2:
129.         RETURN move_tile_by_id(game_board[column][row])
130.     END IF
131.     RETURN 1
132. END move_tile
133. 
134. MODULE start_game():
135.     WHILE True:
136.         OUTPUT get_game_board_string()
137.         INPUT move_tile
138.         IF move_tile_by_id(int(move_tile)) = 0:
139.             OUTPUT "Moved"
140.         ELSE:
141.             OUTPUT "Can't move that"
142.         END IF
143.         IF is_game_board_complete():
144.             OUTPUT "Complete!"
145.             OUTPUT get_game_board_string()
146.             break
147.         END IF
148. END start_game
149. 
150. IF board_size > 1:
151.     board_size = board_size
152.     game_board = None
153.     IF self_start_enabled:
154.         CALL initialize_game_board()
155.         CALL shuffle_game_board(pow(board_size, 6))
156.         CALL start_game()
157.     END IF
158. END IF
159. 
160. CALL initialize_game_board()
161. CALL shuffle_game_board(board_size^6)
162. CALL start_game()
```

---

#

<div style="page-break-after: always;"></div>


[License: GPL v3]: source/gplv3.svg
[MSC]: source/msc.svg
[laith.striegher]: source/laithstriegher.svg
[License URL]: https://www.gnu.org/licenses/gpl-3.0.en.html
[Pillow]: source/pillow.svg
[Pillow URL]: https://pypi.org/project/Pillow/
[tkinter]: source/tkinter.svg
[tkinter URL]: https://docs.python.org/3/library/tkinter.html
[random]: source/random.svg
[random URL]: https://docs.python.org/3/library/random.html
[Python3]: source/python3.svg
[Python3 URL]: https://www.python.org/
[Windows 10/11]: source/windows-10-11.svg
[MacOSX]: source/macosx.svg
[Debian]: source/debian.svg
[Preview]: source/preview.png
