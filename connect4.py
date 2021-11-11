# main driver file that imports all other classes and calls main loop
# edit player/AI, AI/AI, or AI/input, or input/input game modes here.

import Board # numpy is imported in the Board.py file, and does not need to be imported here
import State

path = []

def makeMove(state,col,player):
    newB = state.board.makeMove(col,player)
    st = State.State(newB,state,(state.depth+1))
    path.append(st)
    return st

# code here will be ran when connect4.py is ran
if __name__ == '__main__':
    point = None

    board = Board.Board()
    state = State.State(board,None,0)
    path.append(state)

    turn = 0
    winner = path[-1].board.winner
    while winner is None:
        print(path[-1])
        print("Winner: " + str(path[-1].board.winner))
        if turn%2 == 0:

            x = int(input("[Player 1] Enter a Column: "))
            while 0 > x > 6:
                print("Invalid Entry. Please enter a column 1-7.")
                x = int(input("[Player 1] Enter a Column: "))

            makeMove(path[-1],x,1)
            turn += 1
            winner = path[-1].board.winner
            continue
        else:
        
            y = int(input("[Player 2] Enter a Column: "))
            while 0 > y > 6:
                print("Invalid Entry. Please enter a column 1-7.")
                y = int(input("[Player 2] Enter a Column: "))

            makeMove(path[-1],y,2)
            turn += 1
            winner = path[-1].board.winner
            continue
    print("\n=======================")
    if winner == 1:
        print("Player 1 Won!")
    else:
        print("Player 2 Won!")
        
    