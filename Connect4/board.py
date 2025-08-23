import numpy

class Board:
    board = numpy.array(numpy.zeros((6, 7)))

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(self.board)

