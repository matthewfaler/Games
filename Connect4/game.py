import board

class Game:
    def __init__(self):
        self.board = board.Board()
        self.nextSpots = [5, 5, 5, 5, 5, 5, 5]

    def turn(self):
        inp = input("Choose which column to play (A-G): ")
        match inp:
            case 'A':
                self.board.put(0, self.nextSpots[0])
                self.nextSpots[0] -= 1
            case 'B':
                self.board.put(1, self.nextSpots[1])
                self.nextSpots[1] -= 1
            case 'C':
                self.board.put(2, self.nextSpots[2])
                self.nextSpots[2] -= 1
            case 'D':
                self.board.put(3, self.nextSpots[3])
                self.nextSpots[3] -= 1
            case 'E':
                self.board.put(4, self.nextSpots[4])
                self.nextSpots[4] -= 1
            case 'F':
                self.board.put(5, self.nextSpots[5])
                self.nextSpots[5] -= 1
            case 'G':
                self.board.put(6, self.nextSpots[6])
                self.nextSpots[6] -= 1
            case _:
                print("Please choose a valid option.")

if __name__ == "__main__":
    g = Game()
    while(True):
        g.board.out()
        g.turn()
