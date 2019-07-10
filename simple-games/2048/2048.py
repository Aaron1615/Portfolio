"""
Clone of 2048 game.
"""

import random

OFFSETS = {"UP": (1, 0),
           "DOWN": (-1, 0),
           "LEFT": (0, 1),
           "RIGHT": (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = []
    for dummy_num in range(len(line)):
        result.append(0) 
    for part in line:
        if part > 0:
            for piece in range(len(result)):
                if result[piece] == 0:
                    result[piece] = part
                    break
    final = result[:]
    for number in range(len(final)-1):
        if final[number] == final[number + 1]:
            final[number] = final[number] * 2
            final.pop(number + 1)
            final.append(0)
    return final

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        self._coordinates = []
        self.get_available_tiles()
        self._direction_dict = {}
        self.initialize_direction_dict()

        
    def initialize_direction_dict(self):
        """
        Creates a dictionary of direction keys with list values of the initial
        tiles of that direction. 
        """
        self._direction_dict["UP"] = self._coordinates[0]
        self._direction_dict["DOWN"] = self._coordinates[self._grid_height - 1]
        self._direction_dict["RIGHT"] = []
        self._direction_dict["LEFT"] = []
        
        for row in self._coordinates: 
            self._direction_dict["RIGHT"].append(row[self._grid_width - 1])
            self._direction_dict["LEFT"].append(row[0])
        
        
    def empty_grid(self):
        """
        Creates a grid of zeroes to the specific width and height the object
        is initialized with.
        """
        return [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)] 
    
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        self._grid = self.empty_grid()
        for dummy_repeat in range(2):
            self.new_tile()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for dummy_value in range(self._grid_height):
            string += str( self._grid[dummy_value]) + "\n"
        return string
    

    
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        test_grid = self.empty_grid()
        for initial_tile in self._direction_dict[direction]:
            iterated_list = []
            
            if direction == "UP" or direction == "DOWN":
                change = self._grid_height
            else:
                change = self._grid_width
                
            for step in range(0, change):
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                iterated_list.append(self._grid[row][col])
            merged_list = merge(iterated_list)
            
            for step in range(0, change):
                row = initial_tile[0] + step * OFFSETS[direction][0]
                col = initial_tile[1] + step * OFFSETS[direction][1]
                test_grid[row][col] = merged_list[step]

        if test_grid != self._grid:
            self._grid = test_grid
            self.new_tile()

    def get_available_tiles(self):
        """
        Returns a list of coordinates of the unused values
        in the grid.
        """
        self._coordinates = []
        available_tiles = []
        row = -1
        
        for segment in self._grid:
            temp_coordinates = []
            col = -1
            row += 1
            
            for tile in segment:
                col += 1
                temp_coordinates.append([row,col])
                
                if tile == 0:
                    available_tiles.append([row,col])
            self._coordinates.append(temp_coordinates)
            
        return available_tiles
    
    def available_tiles(self):
        """
        Returns True if there are available tiles remaining.
        """
        tiles = self.get_available_tiles()
        if len(tiles) > 0:
            return True
        else:
            return False
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if self.available_tiles:
            tiles = self.get_available_tiles()
            selected_coordinate = random.randint(0, len(tiles)-1)
            coordinate = tiles[selected_coordinate]
            selection_percent = random.randint(0, 100)
            if  selection_percent > 90:
                number = 4
            else:
                number = 2

            self._grid[coordinate[0]][coordinate[1]]  = number

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        
        return self._grid[row][col]

    def play_round(self):
        """
        Plays a round of TwentyFortyEight
        """
        
        if self.available_tiles():
            move = ""
            while move != "LEFT" and\
                  move != "RIGHT" and\
                  move != "UP" and\
                  move != "DOWN":
                      
                      move =  input("LEFT, RIGHT, UP, or DOWN?")
            self.move(move)
            return True
        else:
            return False



def run_TwentyFortyEight():
    """
    Plays a game of TwentyFortyEight.
    """
    print("Welcome to TwentyFortyEight!")
    while True:
        try:
            height = int(input("From 3 to 10, how tall do you want the board to be?"))
            width = int(input("From 3 to 10, how long do you want the board to be?"))
            if 2 < height < 11 and 2 < width < 11:
                break
            else:
                print("Between 3 and 10 please.")
        except ValueError:
            print("A number please.")
        

        
    play = TwentyFortyEight(height, width)
    run = True
    while run:
        play_round = ""
        while play_round != "Y" and play_round!= "N":    
            play_round = input("Play another round (Y or N)? ")
        if play_round == "N":
            break
        print(play)
        run = play.play_round()
        print(play)
        
        
run_TwentyFortyEight()