#########################################################################
#                                                                       #
#                        Mindarie Senior College                        #
#                            Laith Striegher                            #
#                            Task 1 - Unit 1                            #
#                               'Shuffle'                               #
#                         Game Logic -- logic.py                        #
#                                                                       #
#########################################################################

# Import random for shuffling
import random


# create an enclosing class
class logic:

    # Create object initialisation method
    def __init__(self, board_size=3, self_start_enabled=True):  # default size to 3 and self_start to one
        if board_size > 1:  # ensure size is more than 1
            self.board_size = board_size  # set object size
            self.game_board = None
            if self_start_enabled:  # start logic debug
                self.initialize_game_board()  # Create board
                self.shuffle_game_board(pow(board_size, 6))  # Use testing shuffle function
                self.start_game()

    def initialize_game_board(self):
        self.game_board = self.get_complete_game_board()  # Create a new board based on a complete board

    # Create automatic shuffle method
    def shuffle_game_board(self, moves):
        runs = 0
        while runs < moves:  # Repeat until shuffled <moves> amount of times
            moved = False
            null_pos = self.find_cell_location(-1)  # Find empty cell
            while not moved:  # Ensure at least one moves happens every cycle
                direct = random.randint(0, 3)  # Determine random to try
                if null_pos[0] != self.board_size - 1 and direct == 0:  # Determine if this move is possible
                    self.game_board[null_pos[0]][null_pos[1]], self.game_board[null_pos[0] + 1][null_pos[1]] = self.game_board[null_pos[0] + 1][null_pos[1]], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[1] != self.board_size - 1 and direct == 1:  # Determine if this move is possible
                    self.game_board[null_pos[0]][null_pos[1]], self.game_board[null_pos[0]][null_pos[1] + 1] = self.game_board[null_pos[0]][null_pos[1] + 1], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[0] != 0 and direct == 2:  # Determine if this move is possible
                    self.game_board[null_pos[0]][null_pos[1]], self.game_board[null_pos[0] - 1][null_pos[1]] = self.game_board[null_pos[0] - 1][null_pos[1]], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
                if null_pos[1] != 0 and direct == 3:  # Determine if this move is possible
                    self.game_board[null_pos[0]][null_pos[1]], self.game_board[null_pos[0]][null_pos[1] - 1] = self.game_board[null_pos[0]][null_pos[1] - 1], -1  # Flip values
                    moved = True  # Signal complete cycle
                    continue  # Skip unnecessary checks
            runs += 1

    # Create an id based move method
    def move_cell_by_id(self, cell_id):
        # Find cell
        cell_pos = self.find_cell_location(cell_id)
        if cell_pos[0] < self.board_size - 1:  # Determine if cell is not on bottom edge
            if self.game_board[cell_pos[0] + 1][cell_pos[1]] == -1:  # Determine if move is otherwise possible
                self.game_board[cell_pos[0] + 1][cell_pos[1]], self.game_board[cell_pos[0]][cell_pos[1]] = cell_id, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[1] < self.board_size - 1:  # Determine if cell is not on right edge
            if self.game_board[cell_pos[0]][cell_pos[1] + 1] == -1:  # Determine if move is otherwise possible
                self.game_board[cell_pos[0]][cell_pos[1] + 1], self.game_board[cell_pos[0]][cell_pos[1]] = cell_id, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[0] != 0:  # Determine if cell is not on top edge
            if self.game_board[cell_pos[0] - 1][cell_pos[1]] == -1:  # Determine if move is otherwise possible
                self.game_board[cell_pos[0] - 1][cell_pos[1]], self.game_board[cell_pos[0]][cell_pos[1]] = cell_id, -1  # Flip values
                return 0  # Skip unnecessary checks
        if cell_pos[1] != 0:  # Determine if cell is not on left edge
            if self.game_board[cell_pos[0]][cell_pos[1] - 1] == -1:  # Determine if move is otherwise possible
                self.game_board[cell_pos[0]][cell_pos[1] - 1], self.game_board[cell_pos[0]][cell_pos[1]] = cell_id, -1  # Flip values
                return 0  # Skip unnecessary checks
        return 1  # Cell can't be moved

    # Create an id based find method
    def find_cell_location(self, cell_id):
        for y in range(0, self.board_size):  # Scan columns
            for x in range(0, self.board_size):  # Scan rows
                if self.game_board[y][x] == cell_id:
                    return [y, x]  # Return location
        return 1  # Error

    # Create an id based find method for a complete board
    def find_cell_location_on_complete_board(self, cell_id):
        for y in range(0, self.board_size):  # Scan columns
            for x in range(0, self.board_size):  # Scan rows
                if self.get_complete_game_board()[y][x] == cell_id:
                    return [y, x]  # Return location
        return 1  # Error

    # Create a method to represent a complete board
    def get_complete_game_board(self):
        complete_board = [[i for i in range(self.board_size * j, self.board_size * j + self.board_size)] for j in range(0, self.board_size)]  # Create a new 2D incremental list
        complete_board[self.board_size - 1][self.board_size - 1] = -1  # Set the last value to be blank
        return complete_board

    # Create a method to represent the active board as a string
    def get_game_board_string(self):
        strike = "-"  # Create a new line strike
        for d in range(0, self.board_size):
            strike += "---"  # Customize strike to board size
        string = strike + "\n"  # Begin the string with a strike
        for i in range(0, self.board_size):  # Begin a row
            for j in range(0, self.board_size):
                if self.game_board[i][j] != -1:  # Determine if cell is empty
                    string += "|" + str(self.game_board[i][j]).zfill(2)  # Add a vertical bar and a value
                else:
                    string += "|  "  # Add a vertical bar and space
            string += "|\n" + strike + "\n"  # Finish the row and add a strike
        return string

    # Create a method to check if the current board is complete
    def is_game_board_complete(self):
        return self.game_board == self.get_complete_game_board()

    # Create a location based find method
    def get_cell_value(self, row, col):
        return self.game_board[row][col]

    # Create a location based move method
    def move_cell(self, row, column):
        if self.game_board[column][row] >= 0 or self.game_board[column][row] <= pow(self.board_size, 2) - 1:
            return self.move_cell_by_id(self.game_board[column][row])
        return 1

    # Simple game interface method
    def start_game(self):
        while True:  # Loop until complete
            print(self.get_game_board_string())  # Print Board
            if self.move_cell_by_id(int(input("What to move: "))) == 0:  # Ask user for cell to move and move it
                print("\nMoved\n\n")  # Tell user cell has been moved
            else:
                print("\nCan't move that\n\n")  # If unable to move than tell user
            if self.is_game_board_complete():  # Check if the current board is complete
                print("Complete!\n")  # Tell user that the current board is complete
                print(self.get_game_board_string())  # Print Board
                break  # Break loop