####################
#   Player Class   #
####################
# Holds all methods and packages related to automated player actions
import random
import State

class Player:
    """ Player object to handle logic of automated player actions
        
        Properties:     playerType (int) - type of Player
                        playerType =    0: UserInput, 
                                        1: Random,
                                        2: Minimax,
                                        3: undefined (not sure what algorithm yet),

                        playerValue (int) - val of Player (1 or 2)
    """

    # A Dictionary to hold strings for playerType, will be used for __str__
    playerTypeStrings = {
        0: "User Input",
        1: "Random",
        2: "Minimax",
        3: "{ToBeImplimentedLater}"
    }

    # A function to initlizie the player 
    def __init__(self,playerType,playerValue):
        """Create new instance of player class"""
        self.type = playerType
        self.playerValue = playerValue
        

    # A function to represent the player instance as a string
    def __str__(self):
        """A function to represent a Player instance as a String"""
        pass

    # Random_Col will be used when playerType = 1 ("Random" player type)
    # A function to return a random column in the given state's board
    def random_col(self,state):
        return random.randrange(state.board.COL_COUNT)

    # A function to get the best move for minimax based on state and self.playerValue
    def minimax_get_best_move(self,state,minORmax):
        """ A function to get the best move for minimax based on state and self.playerValue

            Params:     self - Player instance
                        state - State instance
                        minORMAX - 0 = min, 1 = max

            Returns:    column - int location of best column move for minimax player
                        None - if no moves can be made
        """
        if state is None:
            raise ValueError("State cannot be None!")

        if minORmax != 1 and minORmax != 0:
            raise ValueError("Invalid minORmax value!")

        # List of [col,score] move pairs
        move_states = []

        board = state.board
        # List of valid columns on the board
        valid_positions = board.get_valid_positions()
        for col in valid_positions:
            row = board.isValidMove(col)
            # Continue if no valid move exists for this col
            if row is None:
                continue

            moveBoard = board.makeMove(col,self.playerValue)
            score = moveBoard.score_board(self.playerValue)

            # Create state for new board with fvalue = score
            #move_state = State.State(moveBoard,state,(state.depth+1),score)
            
            # Append list containing [state,col]
            move_states.append( (score,col) )
        

        # Sort moves based on state fvalue and if min/max
        if minORmax == 0:
            # Sort by lowest fvalue if Min
            move_states.sort(key=lambda x:x[0])
        else:
            # Sort by highest fvalue if Max
            move_states.sort(key=lambda x:x[0],reverse=True)

        
        # Return None if sortedMoves is empty
        try:
            move_states[0]
        except (ValueError, IndexError):
            return None
        

        # Get first item from sortedMoves
        bestMove = move_states[0]
        
        # Return column of best move
        return bestMove[1]

    # A function to choose a col for next move (depends on player type)
    def get_col_move(self,state):
        """ Choose a column for next move, depending on type of player.

            Params:     self - Player class instance 
                        state - State class instance for current state

            Returns:    column (int) - column for next move to be made
        """
        if self.type == 1:
            return self.random_col(state)
        
        if self.type == 2:
            return self.minimax_get_best_move(state)


