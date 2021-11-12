###############
# State Class #   
###############

class State:
    """
        This class represents the state of each board in the game

        board - the actual board that belongs to this state (See Board Class)
        parent_state - the State that the current State came from after applying a legal move
        depth - the depth in the move tree from the original board that this board
                can be found in (the # of moves the puzzle has undergone)
        f-value - the priority order of the state; some evaluation function of the state
    """

    # The representation of the current game state
    def __init__(self, board, parent_state, depth, fvalue=0):
        self.board = board.duplicate()
        self.parent_state = parent_state
        self.depth = depth
        self.fvalue = fvalue


    # Checks if the f-value of this board is less than the f-value of another board
    def __lt__(self, other):
        return self.fvalue < other.fvalue

    # Converts this State into a string
    def __str__(self):
        return f"{self.board}\nf-value: {self.fvalue}\nsteps: {self.depth}\n"

    # A function to explain how the state is made
    def __repr__(self):
        if self.parent_state is self:
            return f'State({self.board!r}, "is own parent", {self.depth!r}, {self.fvalue!r})'
        try:
            return f'State({self.board!r}, {self.parent_state!r}, {self.depth!r}, {self.fvalue!r})'
        except RecursionError:
            return 'State("could not be represented due to RecursionError")'

    # Checks if two States are the same. This only compares the boards.
    def __eq__(self, other):
        if type(other) is not State:
            return False
        return self.board == other.board

    # Function to print a completed path from the initial state to the solution state #
    def printPath(self):
        print(self.board)
        if self.parent_state is not None:
            self.parent_state.printPath()