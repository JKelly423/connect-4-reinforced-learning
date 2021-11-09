####################
#   Board Class    #
####################
# Properties of Board class (accessed with Board.propertyName)
# 1.    Matrix - 2D Array (Numpy.Array) with state of current board.
# 2.    depth (int) - levels  
import numpy as np

# global variables to change row count and col count
# used global variables to avoid magic numbers
ROW_COUNT = 6
COL_COUNT = 7

class Board:
    """
        This class represents the actual Board of the game

        matrix- double sub-scripted list containing description of the current game State with 0 = blank, 1 = playerOne, and 2 = playerTwo
    """
    # The connect-4 puzzle board representation
    def __init__(self, matrix=None, depth=0):
        """
            Create the board object

        Paramaters: matrix - numpy 2D matrix representing the board state.

        Returns: Creates board, returns nothing
        """
        if matrix is None:
            self.matrix = np.zeros((ROW_COUNT,COL_COUNT))
        else:
            self.matrix = matrix

        if depth == 0:
            self.depth = 0
        else:
            self.depth = depth

        for index, element in np.ndenumerate(self.matrix):
            # confirm that the matrix all contains valid values
            if element != 0 and element != 1 and element != 2:

                raise ValueError("Invalid Matrix!")
    

    def isValidMove(self,point):
        """
            Params: point (tuple) - containing valid (row,col) position on board

            Returns: True/False, True = matrix[row][col] is 0, False = matrix[row][col] == 1 | 2
        """
        # Set point to first tuple in *point args
        row,col = point

        # Verify that the index of point actually exists in the matrix
        try:
            self.matrix[row][col]
        except (ValueError, IndexError):
            return False
        
        # Since we know the point exists, check it's value
        # Since the move is valid as long as the column is not completly filled up, we can assume row = 0
        if self.matrix[0][col] == 0:
            return True
        
        return False

    def makeMove(self,point,playerValue):
        """
            Params:     point (tuple) - containing valid (row,col) position on board
                        player (int) - value of player for board (1 or 2) - used for coloring pieces
            
            Returns:    Board (Board) - representing the new state of the game after the move
                        Returns None if no move can be made
        """
        # Set point to first tuple in *point args
        row,col = point

        # If move is invalid, return None
        if not self.isValidMove(point):
            return None
        
        # Verify the player number is valid
        if playerValue != 1 and playerValue != 2:
            return ValueError("Invalid playerValue!")

        # Since the playerValue and point is valid, make the move
        self.matrix[row][col] = playerValue
        self.depth += 1
        return self

        




    # A function to provide a string representation of the board
    def __str__(self):
        # s will be used to hold everything we are returning, and will be returned at the end
        s = '\n'

        # String with "-" characters sized according to board size to serve as horizontal bar
        bar = ''
        # + (ROW_COUNT*4) since for each row there are 4 characters added (" | "), etc
        for i in range (COL_COUNT + (ROW_COUNT*4)):
            bar += "-"
        bar += '\n'
        
        # Similar to bar, but used to box in the top and bottom of game board
        border = ''
        for i in range (COL_COUNT + (ROW_COUNT*4)):
            border += "="
        border += '\n'

        # Draw Row Numbers
        # String to hold entire Row #'s section seperaetly'
        colNums = "Col Index's\n" + bar +  '|| '

        # Add row index values to colNums string, formatted properly
        for i in range (COL_COUNT):
            if i == 0:
                colNums += str(i)
            else:
                colNums += " | " + str(i)
        colNums += " ||     (Row Index's)\n"
        
        # Add colNums and bar strings to s, so that they will be returned
        s += colNums + bar


        # Iterate matrix and add formatted strings to s
        s += '\n'
        for row in range(ROW_COUNT):
            s += "|| "
            for col in range(COL_COUNT):
                if col == 0:
                    s += str(int(self.matrix[row][col]))
                else:
                    s += " | " + str(int(self.matrix[row][col]))
            s += ' ||       [' + str(row) + "]\n\n"
        return s + '\n\n'


