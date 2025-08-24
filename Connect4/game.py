import board

class Game:
    def __init__(self):
        self.board = board.Board()


    def turn(self):
        inp = input("Choose which column to play (A-G): ")
        match inp:
            case 'A':
                self.board.put(0)
            case 'B':
                self.board.put(1)
            case 'C':
                self.board.put(2)
            case 'D':
                self.board.put(3)
            case 'E':
                self.board.put(4)
            case 'F':
                self.board.put(5)
            case 'G':
                self.board.put(6)
            case _:
                print("Please choose a valid option.")

if __name__ == "__main__":
    g = Game()
    while(True):
        g.board.out()
        g.turn()
