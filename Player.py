####################
#   Player Class   #
####################
# Holds all methods and packages related to automated player actions
import random
import math


class Player:
    """This class encompases the Player object which handles the logic of automated player actions.
    
    :param playerType: type of Player (1: Random, 2: Minimax)
    :type playerType: int
    :param playerValue: number of Player (1 or 2)


    :Attributes:
        * :type (*int*): Player type (1: Random, 2: Minimax)
        * :playerValue (*int*): number of Player (1 or 2)
        * :oppValue (*int*): number of opposing Player (1 or 2)
    """

    # A Dictionary to hold strings for playerType, will be used for __str__
    playerTypeStrings = {
        0: "User Input",
        1: "Random",
        2: "Minimax",
        3: "{ToBeImplimentedLater}"
    }

    # A function to initlizie the player
    def __init__(self, playerType, playerValue):
        """Constructor Method."""
        self.type = playerType
        self.playerValue = playerValue

        if self.playerValue == 1:
            self.oppValue = 2
        else:
            self.oppValue = 1

    # A function to represent the player instance as a string
    def __str__(self):
        """A function to represent a Player instance as a String.
        
        :return: *None*
        """
        pass

    # Random_Col will be used when playerType = 1 ("Random" player type)
    # A function to return a random column in the given state's board
    def random_col(self, state):
        """A function to return a random column in the given state's board.

        :param state: State instance
        :type state: :class:`State.State`

        :return: random column on board
        :rtype: int
        """
        return random.randrange(state.board.COL_COUNT)

    # A function to get the best move for minimax based on state and self.playerValue
    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        """A function to get the best move for minimax player.

        :param self: Player instance
        :type self: :class:`Player.Player`
        :param board: Board instance
        :type board: :class:`Board.Board`
        :param alpha: alpha value
        :type alpha: int
        :param beta: beta value 
        :type beta: int
        :param maximizingPlayer: *True* if player is maximizing player, *False* if player is minimizing player
        :type maximizingPlayer: bool

        :return: column - int location of best column move for minimax player
                 value - score of board for move in returned column
        :rtype: (column,value) tuple
        """
        valid_positions = board.get_valid_positions()

        # If depth is 0, return score of board
        if depth == 0:
            return (None, board.score_board(self.playerValue))

        ## Maximizing Player
        if maximizingPlayer:
            value = -math.inf
            column = None
            for col in valid_positions:
                moveBoard = board.makeMove(col, self.playerValue)
                if moveBoard is None:
                    continue

                if moveBoard.winner == self.playerValue:
                    return (col, 100000000000000)
                elif moveBoard.winner == self.oppValue:
                    return (col, -100000000000000)

                moveBoard_score = self.minimax(moveBoard, (depth - 1), alpha,
                                               beta, False)[1]
                if moveBoard_score > value:
                    value = moveBoard_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return column, value

        ## Minimizing Player
        else:
            value = math.inf
            column = None
            for col in valid_positions:
                moveBoard = board.makeMove(col, self.oppValue)
                if moveBoard is None:
                    continue

                if moveBoard.winner == self.playerValue:
                    return (col, 100000000000000)
                elif moveBoard.winner == self.oppValue:
                    return (col, -100000000000000)

                moveBoard_score = self.minimax(moveBoard, (depth - 1), alpha,
                                               beta, True)[1]
                if moveBoard_score < value:
                    value = moveBoard_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break

            return column, value

    # A function to return the player's best move for a given state
    def get_best_move(self, state):
        """A function to return the player's best move for a given state.
        
        :param state: State instance
        :type state: :class:`State.State`

        :return: column index of best move
        :rtype: int
        """
        board = state.board
        valid_positions = board.get_valid_positions()
        top_score = -99999
        best_col = None
        for col in valid_positions:
            moveBoard = board.makeMove(col, self.playerValue)
            if moveBoard is None:
                continue
            score = moveBoard.score_board(self.playerValue)
            if score > top_score:
                top_score = score
                best_col = col

        return best_col

    # A function to choose a col for next move (depends on player type)
    def get_col_move(self, state):
        """A function to choose a column for next move depending on the type of player.

        :param state: State instance
        :type state: :class:`State.State`

        :return: column for next move to be made
        :rtype: int
        """
        if self.type == 1:
            print("RANDOM")
            return self.random_col(state)

        if self.type == 2:
            return self.minimax(state.board, 5, -math.inf, math.inf, True)[0]
       
