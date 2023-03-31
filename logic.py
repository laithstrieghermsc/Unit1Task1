##########################################################################
#                                                                        #
#                        Mindarie Senior College                         #
#                            Laith Striegher                             #
#                            Task 1 - Unit 1                             #
#                               'Shuffle'                                #
#                         Game Logic -- logic.py                         #
#                                                                        #
##########################################################################

# Import random for shuffling
import random


# create an enclosing class
class logic:
    # Initiate variables as aspects of class
    size = 0
    board = None

    # Create object initialisation method
    def __init__(self, size=3, self_start=True):  # default size to 3 and self_start to one
        if size > 1:  # ensure size is more than 1
            self.size = size  # set object size
            if self_start:  # start logic debug
                self.create_board()  # Create board
                self.shuffle_board(pow(size, 6))  # Use testing shuffle function
                self.begin()

    def create_board(self):
        self.board = self.complete_board()  # Create a new board based on a complete board

    # Create automatic shuffle method
    def shuffle_board(self, moves):
        runs = 0
        while runs < moves:  # Repeat until shuffled <moves> amount of times
            moved = False
            null_pos = self.find_cell(-1)  # Find empty cell
            while not moved:  # Ensure at least one moves happens every cycle
                direct = random.randint(0, 3)  # Determine random to try
                if null_pos[0] != self.size - 1 and direct == 0:  # Determine if this move is possible
                    self.board[null_pos[0]][null_pos[1]], self.board[null_pos[0] + 1][null_pos[1]] = self.board[null_pos[0] + 1][null_pos[1]], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[1] != self.size - 1 and direct == 1:  # Determine if this move is possible
                    self.board[null_pos[0]][null_pos[1]], self.board[null_pos[0]][null_pos[1] + 1] = self.board[null_pos[0]][null_pos[1] + 1], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[0] != 0 and direct == 2:  # Determine if this move is possible
                    self.board[null_pos[0]][null_pos[1]], self.board[null_pos[0] - 1][null_pos[1]] = self.board[null_pos[0] - 1][null_pos[1]], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[1] != 0 and direct == 3:  # Determine if this move is possible
                    self.board[null_pos[0]][null_pos[1]], self.board[null_pos[0]][null_pos[1] - 1] = self.board[null_pos[0]][null_pos[1] - 1], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
            runs += 1

    # Create an id based move method
    def move(self, cell):
        # Find cell
        cell_pos = self.find_cell(cell)
        if cell_pos[0] < self.size - 1:  # Determine if cell is not on bottom edge
            if self.board[cell_pos[0] + 1][cell_pos[1]] == -1:  # Determine if move is otherwise possible
                self.board[cell_pos[0] + 1][cell_pos[1]], self.board[cell_pos[0]][cell_pos[1]] = cell, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[1] < self.size - 1:  # Determine if cell is not on right edge
            if self.board[cell_pos[0]][cell_pos[1] + 1] == -1:  # Determine if move is otherwise possible
                self.board[cell_pos[0]][cell_pos[1] + 1], self.board[cell_pos[0]][cell_pos[1]] = cell, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[0] != 0:  # Determine if cell is not on top edge
            if self.board[cell_pos[0] - 1][cell_pos[1]] == -1:  # Determine if move is otherwise possible
                self.board[cell_pos[0] - 1][cell_pos[1]], self.board[cell_pos[0]][cell_pos[1]] = cell, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[1] != 0:  # Determine if cell is not on left edge
            if self.board[cell_pos[0]][cell_pos[1] - 1] == -1:  # Determine if move is otherwise possible
                self.board[cell_pos[0]][cell_pos[1] - 1], self.board[cell_pos[0]][cell_pos[1]] = cell, -1  # Flip values
                return 0  # Skip unnecessary checks
        return 1  # Cell can't be moved

    # Create an id based find method
    def find_cell(self, cell):
        for y in range(0, self.size):  # Scan columns
            for x in range(0, self.size):  # Scan rows
                if self.board[y][x] == cell:
                    return [y, x]  # Return location
        return 1  # Error

    # Create an id based find method for a complete board
    def find_cell_complete(self, cell):
        for y in range(0, self.size):  # Scan columns
            for x in range(0, self.size):  # Scan rows
                if self.complete_board()[y][x] == cell:
                    return [y, x]  # Return location
        return 1  # Error

    # Create a method to represent a complete board
    def complete_board(self):
        complete_board = [[i for i in range(self.size * j, self.size * j + self.size)] for j in range(0, self.size)]  # Create a new 2D incremental list
        complete_board[self.size - 1][self.size - 1] = -1  # Set the last value to be blank
        return complete_board

    # Create a method to represent the active board as a string
    def board_string(self):
        strike = "-"  # Create a new line strike
        for d in range(0, self.size):
            strike += "---"  # Customize strike to board size
        string = strike + "\n"  # Begin the string with a strike
        for i in range(0, self.size):  # Begin a row
            for j in range(0, self.size):
                if self.board[i][j] != -1:  # Determine if cell is empty
                    string += "|" + str(self.board[i][j]).zfill(2)  # Add a vertical bar and a value
                else:
                    string += "|  "  # Add a vertical bar and space
            string += "|\n" + strike + "\n"  # Finish the row and add a strike
        return string

    # Create a method to check if the current board is complete
    def is_complete(self):
        return self.board == self.complete_board()

    # Create a location based find method
    def get_value(self, row, col):
        return self.board[row][col]

    # Create a location based move method
    def make_move(self, row, column):
        if self.board[column][row] >= 0 or self.board[column][row] <= pow(self.size, 2) - 1:
            return self.move(self.board[column][row])

    # Simple game interface method
    def begin(self):
        while True:  # Loop until complete
            print(self.board_string())  # Print Board
            if self.move(int(input("What to move: "))) == 0:  # Ask user for cell to move and move it
                print("\nMoved\n\n")  # Tell user cell has been moved
            else:
                print("\nCan't move that\n\n")  # If unable to move than tell user
            if self.is_complete():  # Check if the current board is complete
                print("Complete!\n")  # Tell user that the current board is complete
                print(self.board_string())  # Print Board
                break  # Break loop