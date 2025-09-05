import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.finished = False

    def turn(self):
        pname = "X" if self.board.player==0 else "O"
        col = input(f"Player {pname}, please enter the column of your move (1, 2, 3): ")
        row = input(f"Player {pname}, please enter the row of your move (1, 2, 3)(0 to escape): ")
        if row == 0:
            return
        if col not in (1, 2, 3) or row not in (1, 2, 3):
            print("\033[31mPlease enter a valid space.\033[0m")
