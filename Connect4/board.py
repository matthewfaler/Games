import numpy

colors = ('●', '○')
class Board:
    def __init__(self):
        self.board = numpy.full([6, 7], '·', dtype='U1')
        self.player = 0 
        self.nextSpots = [5, 5, 5, 5, 5, 5, 5]


    def toggleColor(self):
        self.player = 1 - self.player

    def put(self, x: int):
        if self.nextSpots[x] == -1:
            print("\033[31mError: Column is full.\033[0m")
            return
        self.board[self.nextSpots[x]][x] = colors[self.player]
        self.toggleColor();
        self.nextSpots[x] -= 1

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore
