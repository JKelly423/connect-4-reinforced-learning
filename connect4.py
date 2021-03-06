# main driver file that imports all other classes and calls main loop
# edit player/AI, AI/AI, or AI/input, or input/input game modes here.

# Import various classes needed for connect4 game
import Board  
import State
import GUI
import Player

# Import required python modules
import math
import sys

# Array of all board states in order
path = []


# A function to create a new state for each move and add it to the path
def makeMove(state, col, player):
    newB = state.board.makeMove(col, player)
    st = State.State(newB, state, (state.depth + 1))
    path.append(st)
    return st


# A function to play Connect-4 in the console
def play_console():

    # Set random starting player
    turn = Player.random.uniform(0, 1)

    # Set winner to the board.winner value of the most recent board in path[]
    # Winner = None if board is not at win state
    # Winner = playerValue if board at win state
    winner = path[-1].board.winner

    # While the board not in win state (aka. exit once board in win state)
    while winner is None:
        print(path[-1].board)

        if turn % 2 == 0:

            x = int(input("[Player 1] Enter a Column: "))
            while 0 > x > 6:
                print("Invalid Entry. Please enter a column 1-7.")
                x = int(input("[Player 1] Enter a Column: "))

            makeMove(path[-1], x, 1)
            turn += 1
            winner = path[-1].board.winner
            continue
        else:

            y = int(input("[Player 2] Enter a Column: "))
            while 0 > y > 6:
                print("Invalid Entry. Please enter a column 1-7.")
                y = int(input("[Player 2] Enter a Column: "))

            makeMove(path[-1], y, 2)
            turn += 1
            winner = path[-1].board.winner
            continue
    print("\n=======================")
    print(path[-1])
    if winner == 1:
        print("Player 1 Won!")
    else:
        print("Player 2 Won!")


# A function to play connect-4 in a GUI format
def play_GUI():

    # Create Player of type Random
    AI = Player.Player(2, 2)

    # Create Screen for GUI
    screen = GUI.GUI()

    # Draw initial black screen for gui
    screen.draw_board(path[-1].board)

    # Set random starting player
    turn = 0

    # Set winner to the board.winner value of the most recent board in path[]
    # Winner = None if board is not at win state
    # Winner = playerValue if board at win state
    winner = path[-1].board.winner

    # While the board not in win state (aka. exit once board in win state)
    while winner is None:

        for event in GUI.pygame.event.get():
            # Close window if window's 'x' button is clicked
            if event.type == GUI.pygame.QUIT:
                sys.exit()

            # Appropriate color piece follows mouse at top of window above board
            if event.type == GUI.pygame.MOUSEMOTION:
                # Get position of mouse in window
                mousePosition = event.pos[0]
                screen.mouse_piece(mousePosition, turn)

            # Draw new board with appropriate pieces when a player makes a move
            if event.type == GUI.pygame.MOUSEBUTTONDOWN:
                # Draw black bar to cover any previous pieces above game board
                GUI.pygame.draw.rect(screen.screen, screen.BLACK,
                                     (0, 0, screen.WIDTH, screen.SQUARESIZE))

                # Player 1 input
                if turn % 2 == 0:

                    # Get x position of where mouse was clicked to determine column
                    mouseClickPos = event.pos[0]

                    # Get col from mouseClickPos
                    col = int(math.floor(mouseClickPos /
                                             screen.SQUARESIZE))

                    if board.isValidMove(col):
                        makeMove(path[-1], col, 1)
                        winner = path[-1].board.winner
                        # Draw piece at top of column
                        screen.mouse_piece(mouseClickPos, turn)
                        # Wait 0.1 seconds after drawing piece at top of column
                        screen.wait(100)
                        screen.draw_board(path[-1].board)
                    turn += 1

                # Code for user input player 2, LEAVE IT HERE FOR NOW, I'll add to Player Class later
                """
                # Player 2 input
                if turn%2 == 1:
                    # Get x position of where mouse was clicked to determine column
                    mouseClickPos = event.pos[0] 
                    # Get col from mouseClickPos
                    col = int(math.floor(mouseClickPos/screen.SQUARESIZE))
                    if board.isValidMove(col):
                        makeMove(path[-1],col,2)
                        screen.draw_board(path[-1].board)
                """

        # If Player 1's move resulted in a win, break while before Player 2's move
        if winner is not None:
            break

        # Player 2 input
        if turn % 2 == 1:
            # Get column from AI player, move depends on type of player
            col = AI.get_col_move(path[-1])
            if board.isValidMove(col):
                makeMove(path[-1], col, AI.playerValue)
                winner = path[-1].board.winner
                # Wait for 2 seconds to make the move seem more natural, not instant
                #screen.wait(1000)
                # Draw piece at top of column
                screen.mouse_piece(col, turn)
                # Wait 0.8 seconds after drawing piece at top of column
                screen.wait(800)
                screen.draw_board(path[-1].board)
            turn += 1

    # Print win message in window, and close after 3.5 seconds
    screen.game_over(winner, 3500)


# code here will be ran when connect4.py is ran
if __name__ == '__main__':
    board = Board.Board()
    state = State.State(board, None, 0)
    path.append(state)
    play_GUI()
