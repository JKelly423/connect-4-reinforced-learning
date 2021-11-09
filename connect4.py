# main driver file that imports all other classes and calls main loop
# edit player/AI, AI/AI, or AI/input, or input/input game modes here.

import Board # numpy is imported in the Board.py file, and does not need to be imported here





# code here will be ran when connect4.py is ran
if __name__ == '__main__':
    b = Board.Board()
    print(b)
    print("Board Depth: " + str(b.depth) + '\n\n')

    point = (0,0)
    p1,p2 = point
    print("Move\n====")
    print("Point: (" + str(p1) + "," + str(p2) + ")")
    gV = b.isValidMove(point)
    print("Valid? : " + str(gV))
    print("Making Move - " + "Point: (" + str(p1) + "," + str(p2) + ")" + " Value: " + str(1))
    g = b.makeMove(point,1)
    print(g)
    print("Board Depth: " + str(g.depth))