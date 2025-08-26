import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.finished = False

    def turn(self):
        inp = input("Choose which column to play (A-G): ").upper()
        colmap = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

        if inp not in colmap:
            print("Please choose a valid option.")
            return

        status = self.board.put(colmap[inp])
        if status == 2:
            self.board.out()
            print(f"Player {board.colors[self.board.player]} wins!")
            self.finished = True
        elif status == 1:
            self.board.out()
            print("It's a draw!")
            self.finished = True

if __name__ == "__main__":
    g = Game()
    while not g.finished:
        g.board.out()
        g.turn()
