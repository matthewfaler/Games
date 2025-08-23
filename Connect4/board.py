import numpy

class Board:
    def __init__(self):
        self.board = numpy.full([6, 7], '◯', dtype='U1')

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore
