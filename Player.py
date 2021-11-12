####################
#   Player Class   #
####################
# Holds all methods and packages related to automated player actions
import random

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
        
    # A function to return a random column in the given state's board
    def random_col(self,state):
        return random.randrange(state.board.COL_COUNT)


    # A function to choose a col for next move (depends on player type)
    def get_col_move(self,state):
        """ Choose a column for next move, depending on type of player.

            Params:     self - Player class instance 
                        state - State class instance for current state

            Returns:    column (int) - column for next move to be made
        """
        if self.type == 1:
            return self.random_col(state)



