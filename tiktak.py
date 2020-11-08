import random


class Board:
    def __init__(self):
        self.positions = [' ' for element in range(10)]

    def redraw(self):
        h_line = '---+---+---'
        v_line = '  |'
        print(self.positions[7] + v_line + self.positions[8] + v_line + self.positions[9])
        print(h_line)
        print(self.positions[4] + v_line + self.positions[5] + v_line + self.positions[6])
        print(h_line)
        print(self.positions[1] + v_line + self.positions[2] + v_line + self.positions[3])


if __name__ == '__main__':
    board = Board()
    board.redraw()
