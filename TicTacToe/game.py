from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.finished = False

    def turn(self):
        
