import numpy

x_or_o = ('X', 'O')

class Board:
    def __init__(self):
        self.board = numpy.full([3, 3], ' ', dtype='U1')
        self.player = 0

    def put(self, x, y):
        if self.board[y, x] != ' ':
            print("\033[31mPlease select empty space.\033[0m")
            return -1
        self.board[y, x] = x_or_o[self.player]
        self.togglePlayer()
        if self.checkVictory(): return 2
        if self.checkFull(): return 1
        return 0

    def checkVictory(self):
        if self.board[0][0] == self.board[0][1] and self.board[0][1] == self.board[0][2] and self.board[0][1] != ' ': return True
        if self.board[1][0] == self.board[1][1] and self.board[1][1] == self.board[1][2] and self.board[1][1] != ' ': return True
        if self.board[2][0] == self.board[2][1] and self.board[2][1] == self.board[2][2] and self.board[2][1] != ' ': return True
        if self.board[0][0] == self.board[1][0] and self.board[1][0] == self.board[2][0] and self.board[1][0] != ' ': return True
        if self.board[0][1] == self.board[1][1] and self.board[1][1] == self.board[2][1] and self.board[1][1] != ' ': return True
        if self.board[0][2] == self.board[1][2] and self.board[1][2] == self.board[2][2] and self.board[1][2] != ' ': return True
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] != ' ': return True
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][1] != ' ': return True
        return False

    def checkFull(self):
        return not numpy.any(self.board == ' ')

    def togglePlayer(self):
        self.player = 1 - self.player

    def out(self):
        print("   1   2   3")
        print(f" 1 {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}")
        print("  -----------")
        print(f" 2 {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}")
        print("  -----------")
        print(f" 3 {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")

    def get(self):
        return 
if __name__ == "__main__":
    b = Board()
    b.out()
