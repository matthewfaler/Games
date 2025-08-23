import board

class Game:
    def __init__(self):
        self.board = board.Board()


if __name__ == "__main__":
    g = Game()
    g.board.out()
