#################
#   GUI Class   #
#################
# Holds all methods and packages related to pygame and a GUI

import pygame
import Board

# Get layout from board class so that there are not multiple instances of magic numbers
COL_COUNT = Board.COL_COUNT
ROW_COUNT = Board.ROW_COUNT

# COLORS defined with RGB values
BLUE = (0, 0, 255)  # Background
BLACK = (0, 0, 0)  # Player Slots
RED = (255, 0, 0)  # Player 1
YELLOW = (255, 255, 0)  # Player 2

# Square size in px (one side)
SQUARESIZE = 100
# COL_COUNT * SQUARESIZE
WIDTH = COL_COUNT * SQUARESIZE
# (ROW_COUNT+1) * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
# Tuple to initilize pygame.display
SIZE = (WIDTH, HEIGHT)

# Best formula I found for good looking player slots
RADIUS = int(SQUARESIZE / 2 - 5)


class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        self.SQUARESIZE = SQUARESIZE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SIZE = SIZE
        self.RADIUS = RADIUS
        self.BLUE = BLUE
        self.BLACK = BLACK
        self.RED = RED
        self.YELLOW = YELLOW
        self.FONT = pygame.font.SysFont("monospace", 75)

    def draw_board(self, board):
        # Change title bar of pygame window for visual effect
        pygame.display.set_caption("Connect-4")

        # Draw black bar to cover any previous pieces above game board
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))

        for r in range(ROW_COUNT):
            for c in range(COL_COUNT):

                # Draw blue background
                pygame.draw.rect(self.screen, BLUE,
                                 (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE,
                                  SQUARESIZE, SQUARESIZE))

                if board.matrix[r][c] == 0:
                    # Draw BLACK circle if position is empty
                    pygame.draw.circle(
                        self.screen, BLACK,
                        (int(c * SQUARESIZE + SQUARESIZE / 2),
                         int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                        RADIUS)
                elif board.matrix[r][c] == 1:
                    # Draw RED circle if position belongs to Player 1
                    pygame.draw.circle(
                        self.screen, RED,
                        (int(c * SQUARESIZE + SQUARESIZE / 2),
                         int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                        RADIUS)
                elif board.matrix[r][c] == 2:
                    # Draw YELLOW circle if position belongs to Player 2
                    pygame.draw.circle(
                        self.screen, YELLOW,
                        (int(c * SQUARESIZE + SQUARESIZE / 2),
                         int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                        RADIUS)

        # Update the pygame display so that the drawings show in window
        pygame.display.update()

    # A function to display the appropriate piece at the player's
    def mouse_piece(self, mousePosition, turn):
        # Draw black bar to cover any previous pieces above game board
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
        if turn % 2 == 0:
            # Draw Red piece if it is Player 1's turn
            pygame.draw.circle(self.screen, RED,
                               (mousePosition, int(SQUARESIZE / 2)), RADIUS)
        else:
            # Draw Yellow piece if it is Player 1's turn
            mousePosition = (int(mousePosition * SQUARESIZE + SQUARESIZE / 2))
            pygame.draw.circle(self.screen, YELLOW,
                               (mousePosition, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    # A function to display a message to the winner, and close the game
    def game_over(self, winner, waitTime):
        """ Display message to winner, wait a few seconds, then close the game Window. 

            Params:     winner (int): player who won the game
                        waitTime (int): time to wait before closing window (milliseconds)
            Returns:    does not return aything
        """
        # Print win message on screen
        if winner == 1:
            winMessage = self.FONT.render("Player 1 Wins!", 1, RED)
            self.screen.blit(winMessage, (18, 5))
        else:
            winMessage = self.FONT.render("Player 2 Wins!", 1, YELLOW)
            self.screen.blit(winMessage, (18, 5))

        # Update the window to display blit
        pygame.display.update()

        # Wait before closing window
        self.wait(waitTime)

    def wait(self, waitTime):
        """ Helper function to make screen wait for given time in milliseconds
            
            Params:     
                        waitTime (int): time to wait before closing window (milliseconds)
        """
        # Wait using pygame's time.wait function
        pygame.time.wait(waitTime)
