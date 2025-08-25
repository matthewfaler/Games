import numpy

colors = ('●', '○')
below = 6
right = 7
left = -1
above = -1

class Board:
    def __init__(self):
        self.board = numpy.full([below, right], '·', dtype='U1')
        self.player = 0 
        self.nextSpots = [5, 5, 5, 5, 5, 5, 5]

    def toggleColor(self):
        self.player = 1 - self.player

    def put(self, x: int):
        if self.nextSpots[x] == above:
            print("\033[31mError: Column is full.\033[0m")
            return False
        self.board[self.nextSpots[x]][x] = colors[self.player]
        if self.checkVictory(x, self.nextSpots[x]):
            return True
        self.toggleColor();
        self.nextSpots[x] -= 1
        return False

    def checkVictory(self, x: int, y: int):
        hor, ver, diag, adiag = 1, 1, 1, 1
        connect = 4
        for i in range(1, connect):
            if y + i >= below or self.board[y + i][x] != colors[self.player]: break
            else: ver += 1
        if ver >= connect: return True

        for i in range(1, connect):
            if x + i >= right or self.board[y][x + i] != colors[self.player]: break
            else: hor += 1
        if hor >= connect: return True
        for i in range(1, connect):
            if x - i <= left or self.board[y][x - i] != colors[self.player]: break
            else: hor += 1
        if hor >= connect: return True

        for i in range(1, connect):
            if x - i <= left or y - i <= above or self.board[y - i][x - i] != colors[self.player]: break
            else: diag += 1
        if diag >= connect: return True
        for i in range(1, connect):
            if x + i >= right or y + i >= below or self.board[y + i][x + i] != colors[self.player]: break
            else: diag += 1
        if diag >= connect: return True

        for i in range(1, connect):
            if x - i <= left or y + i >= below or self.board[y + i][x - i] != colors[self.player]: break
            else: adiag += 1
        if adiag >= connect: return True
        for i in range(1, connect):
            if x + i >= right or y - i <= above or self.board[y - i][x + i] != colors[self.player]: break
            else: adiag += 1
        if adiag >= connect: return True

        return False

    def checkFull(self):
       return all(x == -1 for x in self.nextSpots)

    def out(self):
        print("  A  B  C  D  E  F  G")
        print(numpy.array2string(self.board, separator="  ", formatter={'all': lambda x: x}).replace("[", " ").replace("]", ""))     # type: ignore
