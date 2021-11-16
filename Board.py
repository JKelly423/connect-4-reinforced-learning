####################
#   Board Class    #
####################
# Properties of Board class (accessed with Board.propertyName)
# 1.    Matrix - 2D Array (Numpy.Array) with state of current board.
# 2.    depth (int) - levels
import numpy as np

ROW_COUNT = 6
COL_COUNT = 7


class Board:
    """
        This class represents the actual Board of the game

        matrix- double sub-scripted list containing description of the current game State with 0 = blank, 1 = playerOne, and 2 = playerTwo

        winner (int) - player who won the game, None if game not won

        ROW_COUNT (int) - # of Rows 
        COL_COUNT (int) - # of Columns
    """

    # The connect-4 puzzle board representation
    def __init__(self, matrix=None, winner=None):
        """
            Create the board object

        Paramaters: matrix - numpy 2D matrix representing the board state.
                    winner - winner of game, None if game not won

        Returns: Creates board, returns nothing
        """
        self.ROW_COUNT = ROW_COUNT
        self.COL_COUNT = COL_COUNT

        if matrix is None:
            self.matrix = np.zeros((ROW_COUNT, COL_COUNT))
        else:
            self.matrix = matrix

        if winner is None:
            self.winner = None
        else:
            self.winner = winner

        self.score = None

        for index, element in np.ndenumerate(self.matrix):
            # confirm that the matrix all contains valid values
            if element != 0 and element != 1 and element != 2:
                print("Invalid Element: " + str(element))
                raise ValueError("Invalid Matrix!")

    # A function to checks if two Boards are equal
    def __eq__(self, other):
        """
            Params:     other (Board) - other board to compare self to
            
            Returns:    True if the two boards are equal
        """
        if not isinstance(other, Board):
            return False
        return self.matrix == other.matrix

    # A function to check if the move is valid
    def isValidMove(self, col):
        """
            Params:     point (tuple) - containing valid (row,col) position on board

            Returns:    row - row containing valid move for col
                        False - if no move is valid for col
        """

        for row in range((ROW_COUNT - 1), -1, -1):
            # Verify that the index of point actually exists in the matrix
            try:
                self.matrix[row][col]
            except (ValueError, IndexError):
                continue

            # Since we know the point exists, check it's value
            if self.matrix[row][col] == 0:
                return row

        return False

    # Function to return array of points located next to  input point
    def neighbors(self, point, position):
        """
            Params:     point (tuple) - containing valid (row,col) position on board
                        position (int) - int specifiying which neighbor to check
                        
            
            Returns:    array of valid (they exist on the board) points neighboring the paramater point
            Returns:    None neighbor does not exist
        """
        # Set point to first tuple in *point args
        row, col = point

        # Verify that the index of point actually exists in the matrix
        try:
            self.matrix[row][col]
        except (ValueError, IndexError):
            raise ValueError("Point Does not Exist in Board!")

        # Verify the position is valid
        if not 0 <= position <= 8:
            raise ValueError("Position Invalid!")

        # Top Left = 0
        # Top Middle = 1
        # Top Right = 2
        # Direct Left = 3
        # Direct Right = 4
        # Bottom Left = 5
        # Bottom middle = 6
        # Bottom right = 7
        neighborVals = {
            0: (row - 1, col - 1),
            1: (row - 1, col),
            2: (row - 1, col + 1),
            3: (row, col - 1),
            4: (row, col + 1),
            5: (row + 1, col - 1),
            6: (row + 1, col),
            7: (row + 1, col + 1),
        }

        # If position is not 8, get value of specified position
        if position != 8:
            elem = neighborVals.get(position)
            r, c = elem
            if 0 <= r < ROW_COUNT:
                if 0 <= c < COL_COUNT:
                    return elem
                return None
            return None

        # If position is 8, get array of all neighbors
        neighbors = neighborVals.values()
        goodNeighbors = []
        for elem in neighbors:
            r, c = elem
            if 0 <= r < ROW_COUNT:
                if 0 <= c < COL_COUNT:
                    goodNeighbors.append(elem)

        return goodNeighbors

    # A function to create a copy of the Board object itself
    def duplicate(self):
        """ A function to create a copy of the Board object itself.

            Used to create duplicates of each Board in order to ensure each State's board is unique to when the state was initilized.

            Params:     self - Board instance

            Returns:    duplicate new board instance
        """
        new_matrix = [row.copy() for row in self.matrix]
        return Board(new_matrix, self.winner)

    def makeMove(self, col, playerValue):
        """ A function to make a move on the board in the given column for the given player value.

            Params:     col (int) - column position of position on board
                        player (int) - value of player for board (1 or 2) - used for coloring pieces
            
            Returns:    Board (Board) - representing the new state of the game after the move
                        Returns None if no move can be made
        """
        moveBoard = self.duplicate()
        # Set point to first tuple in *point args
        row = moveBoard.isValidMove(col)

        # If move is invalid, return None
        if row is False:
            return None

        # Verify the player number is valid
        if playerValue != 1 and playerValue != 2:
            return ValueError("Invalid playerValue!")

        # Since the playerValue and point is valid, make the move
        moveBoard.matrix[row][col] = playerValue

        point = (row, col)
        # If someone won, set winner value
        if moveBoard.win_state(point) is not None:
            moveBoard.winner = playerValue

        return moveBoard

    # A function to return a list of valid col positions for moves
    def get_valid_positions(self):
        """ A function to return a list of valid columns positions on board

            Params:     self - Board instance

            Returns:    valid_positions - list of valid columns on the board 

            Valid means that the columns are not entirely filled up and that a move can be made there
        """
        valid_positions = []
        for c in range(self.COL_COUNT):
            # Since a move is valid as long as the entire row is not filled, we only have to check that row 0 (the top row) in each column is valid.
            if self.matrix[0][c] == 0:
                valid_positions.append(c)
        return valid_positions

    # A function to check if the move made resulted in a winning state
    def win_state(self, point):
        """ A function to check if the move made resulted in a winning state.

            Params:     point (tuple) - containing valid (row,col) position on board
            
            Returns:    point (tuple) - final point of winning streak
                        None if no win state is achieved
        """
        row, col = point
        # Verify point is valid
        if point is None:
            return None

        # A tail recursive helper function
        def win_state_helper(winningPt, streak=2):

            point, position = winningPt
            row, col = point

            neighbor = self.neighbors(point, position)
            if neighbor is not None:
                nR, nC = neighbor
                if self.matrix[nR][nC] == self.matrix[row][col]:
                    streak += 1
                    if streak == 4:
                        return neighbor
                    return win_state_helper((neighbor, position), (streak))
            return None

        playerVal = self.matrix[row][col]

        for i in range(COL_COUNT + 1):
            neighbor = self.neighbors(point, i)
            if neighbor is None:
                continue

            nR, nC = neighbor
            neighborVal = self.matrix[nR][nC]
            if neighborVal == playerVal:
                helper = win_state_helper((neighbor, i))
                if helper is not None:
                    return helper
        return None

    # A function to score a list of 4 neighboring points
    def score_neighbors(self, neighbors, playerValue):
        score = 0

        oppValue = 2
        if playerValue == 2:
            oppValue = 1

        # If all 4 pieces are = playerValue, score is increased by 100
        if neighbors.count(playerValue) == 4:
            score += 100

        # If 3 pieces are playerValue and one piece is unplayed, score += 5
        if neighbors.count(playerValue) == 3 and neighbors.count(0) == 1:
            score += 5

        # If 2 pieces are playerValue and 2 pieces are unplayed, score += 2
        if neighbors.count(playerValue) == 2 and neighbors.count(0) == 2:
            score += 2

        # If 3 pieces are oppValue and 1 piece is unplayed, score -= 4
        if neighbors.count(oppValue) == 3 and neighbors.count(0) == 1:
            score -= 4

        # If opponent won game, score -= 100
        if neighbors.count(oppValue) == 4:
            score -= 100

        return score

    # A function to score the board for a given playerValue for minimax
    def score_board(self, playerValue):
        """ A function to score the board for a given playerValue
            Params:     
            
            Returns:    
                        
        """
        # Number of pieces in a row needed to win
        WIN_PIECE_COUNT = 4

        # Set variable to hold np array of board Matrix
        board_array = np.array(self.matrix)

        score = 0

        # Score multiplier for center board position
        CENTER_PIECE_MULTIPLIER = 3

        # Positions in the center of the board are more advantagous

        ## Score Center Column
        center_pieces = [int(i) for i in list(board_array[:, COL_COUNT // 2])]
        center_piece_count = center_pieces.count(playerValue)
        score += center_piece_count * CENTER_PIECE_MULTIPLIER

        ## Score Horizontal
        for row in range(ROW_COUNT):
            row_values = [int(i) for i in list(board_array[row, :])]
            # Remove 3 from col count since 3rd to last col will check up to last column
            for col in range(COL_COUNT - 3):
                next_4_neighbors = row_values[col:col + WIN_PIECE_COUNT]
                score += self.score_neighbors(next_4_neighbors, playerValue)

        ## Score Vertical
        for col in range(COL_COUNT):
            col_values = [int(i) for i in list(board_array[:, col])]
            # Remove 3 from row count since 3rd to last row will check up to last row
            for row in range(ROW_COUNT - 3):
                next_4_neighbors = col_values[row:row + WIN_PIECE_COUNT]
                score += self.score_neighbors(next_4_neighbors, playerValue)

        ## Score Positive Diagonal
        for row in range(ROW_COUNT - 3):
            for col in range(COL_COUNT - 3):
                next_4_neighbors = [
                    board_array[row + i][col + i]
                    for i in range(WIN_PIECE_COUNT)
                ]
                score += self.score_neighbors(next_4_neighbors, playerValue)

        ## Score Negative Diagonal
        for row in range(ROW_COUNT - 3):
            for col in range(COL_COUNT - 3):
                next_4_neighbors = [
                    self.matrix[row + 3 - i][col + i]
                    for i in range(WIN_PIECE_COUNT)
                ]
                score += self.score_neighbors(next_4_neighbors, playerValue)

        return score

    # A function to provide a string representation of the board
    def __str__(self):
        # s will be used to hold everything we are returning, and will be returned at the end
        s = '\n'

        # String with "-" characters sized according to board size to serve as horizontal bar
        bar = ''
        # + (ROW_COUNT*4) since for each row there are 4 characters added (" | "), etc
        for i in range(COL_COUNT + (ROW_COUNT * 4)):
            bar += "-"
        bar += '\n'

        # Similar to bar, but used to box in the top and bottom of game board
        border = ''
        for i in range(COL_COUNT + (ROW_COUNT * 4)):
            border += "="
        border += '\n'

        # Draw Row Numbers
        # String to hold entire Row #'s section seperaetly'
        colNums = "Col Index's\n" + bar + '|| '

        # Add row index values to colNums string, formatted properly
        for i in range(COL_COUNT):
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
