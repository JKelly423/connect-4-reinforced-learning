###############
# State Class #
###############


class State:
    """This class represents the state of the game.

    :param board: the actual board that belongs to this state 
    :type board: :class:`Board.Board`
    :param parent_state: the State that the current State came from after applying a legal move
    :type parent_state: :class:`State.State`
    :param depth: the depth of the current state (number of moves made)
    :type depth: int
    :param f-value: the priority order of the state; some heuristic function of the state. Defaults to *0*
    :type f-value: int, optional

    :Attributes:
        * :board (:class:`Board.Board`): number of rows
        * :parent_state (:class:`State.State`) the State prior to current state
        * :depth (*int*): depth of state
        * :fvalue (*int*): priorty order of the state. The value of some heuristic function. Defaults to *0*
    """

    # The representation of the current game state
    def __init__(self, board, parent_state, depth, fvalue=0):
        """Constructor Method"""
        self.board = board.duplicate()
        self.parent_state = parent_state
        self.depth = depth
        self.fvalue = fvalue

    # Checks if the f-value of this board is less than the f-value of another board
    def __lt__(self, other):
        """A function to check if the f-value of this board is less than the f-value of another board.

        :param other: State to compare this state to
        :type other: :class:`State.State`

        :return: *True* if self.fvalue < other.fvalue, *False* if self.fvalue > other.fvalue
        :rtype: bool
        """
        return self.fvalue < other.fvalue

    # Converts this State into a string
    def __str__(self):
        """A function to convert the current state to a string representation readable by humans.

        :return: string representation of state
        :rtype: str
        """
        return f"{self.board}\nf-value: {self.fvalue}\nsteps: {self.depth}\n"

    # A function to explain how the state is made
    def __repr__(self):
        """A function to explain how the state is made.
        
        :return: A string explaining how the state is made
        :rtype: str
        """
        if self.parent_state is self:
            return f'State({self.board!r}, "is own parent", {self.depth!r}, {self.fvalue!r})'
        try:
            return f'State({self.board!r}, {self.parent_state!r}, {self.depth!r}, {self.fvalue!r})'
        except RecursionError:
            return 'State("could not be represented due to RecursionError")'

    # Checks if two States are the same. This only compares the boards.
    def __eq__(self, other):
        """A function to check if two States are the same. This only compares the boards.

        :param other: State to compare self to
        :type other: :class:`State.State`

        :return: *True* if self.board is equal to other.board, *False* otherwise
        :rtype: bool
        """
        if type(other) is not State:
            return False
        return self.board == other.board

    # Function to print a completed path from the initial state to the solution state #
    def printPath(self):
        """A function to print a complated path from the initial state to the solution state. This function calls print() statements directly, rather than returning a string.

        :return: *None*
        """
        print(self.board)
        if self.parent_state is not None:
            self.parent_state.printPath()
