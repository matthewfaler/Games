import numpy

class Board:
    board = numpy.full([6, 7], '◯', dtype='U1')

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore

if __name__ == "__main__":
    b = Board()
    b.out()
