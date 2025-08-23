import numpy

colors = ('●', '○')

class Board:
    def __init__(self):
        self.board = numpy.full([6, 7], '·', dtype='U1')
        self.player = 0

    def toggleColor(self):
        self.player = 1 - self.player

    def put(self, x: int, y: int):
        self.board[y][x] = colors[self.player]
        self.toggleColor();

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore
