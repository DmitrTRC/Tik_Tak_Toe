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


class Player:
    marker = ()

    def __init__(self, name='Human', human_mode=True):
        self.human_mode = human_mode
        self.name = name
        self.set_marker()

    def set_marker(self):
        try:
            if self.human_mode:
                while (tmp_marker := input('Enter your SIGN ( X or 0 ) -> ').upper()) not in ('0', 'X'):
                    print('Only "X" or "0" possible. Try again...')
                Player.marker = (tmp_marker, '0' if tmp_marker == 'X' else 'X')
            else:
                print(f'Computer SIGN is: {Player.marker[1]}\n')
        except IndexError:
            print(f'You have to call Human init before .')


if __name__ == '__main__':
    board = Board()

    human_player = Player(input('Enter your nick -> '))
    ai_player = Player(human_mode=False)

    board.redraw()
