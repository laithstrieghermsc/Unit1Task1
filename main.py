#########################################################################
#                                                                       #
#                        Mindarie Senior College                        #
#                            Laith Striegher                            #
#                            Task 1 - Unit 1                            #
#                               'Shuffle'                               #
#                       Main controller -- main.py                      #
#                                                                       #
#########################################################################

# import the visual library
import tkinter as tk
from array import array

from PIL import ImageTk, Image
from random import randint
# import the logic module
from logic import logic


class shuffle:
    def __init__(self, board_size=3, window_size=1000, game_title="Shuffle Game", shuffle_rule=None, image_file=None,
                 default_bg_color="#f0f0f0", complete_bg_color="#00ff00", exit_on_complete=False, override=False,
                 pos_esp=False, highlight_thickness=1, photo_options=None):
        if photo_options is None:
            self.photo_options = (  # Array of photos
                ["demo\\0.png", "demo\\1.png", "demo\\2.png", "demo\\3.png", "demo\\4.png", "demo\\5.png",
                 "demo\\6.png",
                 "demo\\7.png", "demo\\8.png", "demo\\9.png", "demo\\a.png", "demo\\b.png", "demo\\c.png",
                 "demo\\d.png",
                 "demo\\e.png", "demo\\f.png", "demo\\10.png", "demo\\11.png", "demo\\12.png", "demo\\13.png",
                 "demo\\14.png",
                 "demo\\15.png", "demo\\16.png", "demo\\17.png", "demo\\18.png", "demo\\19.png", "demo\\1a.png",
                 "demo\\1b.png",
                 "demo\\1c.png", "demo\\1d.png", "demo\\1e.png", "demo\\1f.png", "demo\\20.png", "demo\\21.png",
                 "demo\\22.png",
                 "demo\\23.png", "demo\\24.png", "demo\\25.png", "demo\\26.png", "demo\\27.png", "demo\\28.png",
                 "demo\\29.png",
                 "demo\\2a.png", "demo\\2b.png", "demo\\2c.png", "demo\\2d.png", "demo\\2e.png", "demo\\2f.png",
                 "demo\\30.png"])
        else:
            self.photo_options = photo_options
        self.board_size = board_size
        self.window_size = window_size
        self.game_title = game_title
        self.exit_on_complete = exit_on_complete
        self.pos_esp = pos_esp
        self.highlight_thickness = highlight_thickness
        # set the shuffle_rule attribute to either the passed argument or a default value
        if shuffle_rule is not None:
            self.shuffle_rule = shuffle_rule
        else:
            self.shuffle_rule = pow(board_size, 6)

        # set the image_file attribute to either the passed argument or a default value
        if image_file is not None:
            self.image_file = image_file
        else:
            self.image_file = self.photo_options[randint(0, len(self.photo_options) - 1)]

        # set the button_size attribute based on the size of the window and the size of the game board
        self.button_size = int(window_size / board_size)
        self.num_moves = 0
        self.default_bg_color = default_bg_color
        self.complete_bg_color = complete_bg_color

        # initialize empty lists for the buttons and cell photos
        self.buttons_list = []
        self.photos_list = []

        # initialize a logic object for the game
        self.game_logic = logic(board_size, False)

        # create the main tkinter window
        self.root = tk.Tk()
        self.root.title(self.game_title)
        self.root.overrideredirect(override)

    def reset(self, size=3, window_size=1000, game_title="Shuffle Game", shuffle_rule=None, image_file=None,
              default_color="#f0f0f0", complete_color="#00ff00", exit_on_completion=False, overrideredirect=False,
              pos_esp=False, highlight_thickness=1, applicable_photos=None):
        self.__init__(board_size=size, window_size=window_size, game_title=game_title, shuffle_rule=shuffle_rule,
                      image_file=image_file, default_bg_color=default_color,
                      complete_bg_color=complete_color, exit_on_complete=exit_on_completion,
                      override=overrideredirect, pos_esp=pos_esp,
                      highlight_thickness=highlight_thickness, photo_options=applicable_photos)

    def start(self):
        # create and shuffle the game board
        self.game_logic.initialize_game_board()
        self.game_logic.shuffle_game_board(self.shuffle_rule)

        # open the image specified by the image_location attribute
        self.img = Image.open(self.image_file)

        # adjust the size of the image to fit the window if necessary
        if self.img.width > self.img.height:
            self.img = self.img \
                .crop(
                (int((self.img.width - self.img.height) / 2), 0,
                 int((self.img.width - self.img.height) / 2 + self.img.height), self.img.height)) \
                .resize((self.window_size, self.window_size))
        elif self.img.height > self.img.width:
            self.img = self.img \
                .crop((self.img.width, int(self.img.height - self.img.width / 2), self.img.width,
                       int(self.img.height - self.img.width / self.img.width))) \
                .resize((self.window_size, self.window_size))

        # create a blank image to represent the empty cell
        self.blank = ImageTk.PhotoImage(
            Image.new(mode="RGB",
                      size=(int(self.window_size / self.board_size), int(self.window_size / self.board_size)),
                      color=0xffffff))

        # create an image for each cell on the game board
        for cell in range(0, pow(self.board_size, 2) - 1):
            complete_cell_pos = self.game_logic.find_cell_location_on_complete_board(cell)
            self.photos_list.append(ImageTk.PhotoImage(self.img.crop((self.button_size * complete_cell_pos[1],
                                                                      self.button_size * complete_cell_pos[0],
                                                                      self.button_size * complete_cell_pos[
                                                                          1] + self.button_size,
                                                                      self.button_size * complete_cell_pos[
                                                                          0] + self.button_size)).resize(
                (self.button_size, self.button_size))))
        # create an image for the empty cell
        complete_cell_pos = self.game_logic.find_cell_location_on_complete_board(-1)
        self.photos_list.append(ImageTk.PhotoImage(self.img.crop((self.button_size * complete_cell_pos[1],
                                                                  self.button_size * complete_cell_pos[0],
                                                                  self.button_size * complete_cell_pos[
                                                                      1] + self.button_size,
                                                                  self.button_size * complete_cell_pos[
                                                                      0] + self.button_size)).resize(
            (self.button_size, self.button_size))))
        # iterate over each row
        for i in range(self.board_size):
            row = []  # create a new list for each row
            # iterate over each column
            for j in range(self.board_size):
                # create a new button for each cell in the grid
                # set the font, background color, width and height of the button
                # set the command to be executed when the button is clicked
                button = tk.Button(self.root, font=("Arial", 60), bg=self.default_bg_color, width=self.button_size,
                                   height=self.button_size,
                                   command=lambda i=i, j=j: self.handle_click(self.buttons_list[i][j]), border=0,
                                   highlightthickness=self.highlight_thickness)
                # set the position of the button on the grid
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)  # add the button to the current row
            self.buttons_list.append(row)  # add the row to the list of buttons

        # update the state of the buttons to match the current game state
        self.update_buttons()
        # start the main event loop, waiting for user input
        # self.root.config(b)
        self.root.mainloop()

    # create a method to handle button clicks
    def handle_click(self, clicked_button):
        # get the row and column of the clicked button
        row, col = clicked_button.grid_info()["row"], clicked_button.grid_info()["column"]
        # call the make_move method of the game object
        if self.game_logic.move_cell(col, row) == 0:
            self.num_moves += 1  # Increment the move counter
        # update the text of the buttons
        self.update_buttons()
        if self.num_moves != 1:  # if "s" is needed
            s = "s"  # make s available
        else:
            s = ""  # ensure s is blank and exists
        self.root.title(f"{self.game_title}  {self.num_moves} move{s}")  # Refresh the Toolbar to reflect game state

    # create a method to update the text of the buttons
    def update_buttons(self):
        global game, img  # Pull global variables
        for i in range(self.board_size):  # for every column
            for j in range(self.board_size):  # For every cell in the column
                # get the button at (i, j)
                updating_button = self.buttons_list[i][j]
                # get the value of the game board at (i, j)
                cell_value = self.game_logic.get_cell_value(i, j)
                if cell_value != -1:  # if cell is not blank
                    # set the text of the button to the value and the image of the button to the appropriate image
                    updating_button.config(text=str(cell_value), image=self.photos_list[cell_value],
                                           highlightthickness=self.highlight_thickness)
                else:
                    # set the text of the button to the value and the image of the button be blank
                    updating_button.config(text=str(cell_value), image=self.blank)
                # if pos_esp is on
                if self.pos_esp:
                    if self.game_logic.find_cell_location(
                            cell_value) == self.game_logic.find_cell_location_on_complete_board(cell_value):
                        updating_button.config(highlightthickness=0)
                # Check if game is complete
                if self.game_logic.is_game_board_complete():
                    # Set background color to complete color
                    updating_button.config(background=self.complete_bg_color, highlightthickness=0)
                    # Checks if cell is blank
                    if self.game_logic.get_cell_value(i, j) == -1:
                        # Sets the cell to the final image
                        updating_button.config(image=self.photos_list[len(self.photos_list) - 1])
                    if self.exit_on_complete:
                        exit(0)
                else:
                    # Set background color to default
                    updating_button.config(background=self.default_bg_color)
