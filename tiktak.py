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

    def copy(self):
        return self.positions.copy()

    def is_free(self, pos):
        return self.positions[pos] == ' '


class Player:
    marker = ()

    def __init__(self, name='Human', human_mode=True):
        self.human_mode = human_mode
        self.name = name
        self.set_mark()

    def set_mark(self):
        try:
            if self.human_mode:
                while (tmp_marker := input('Enter your SIGN ( X or 0 ) -> ').upper()) not in ('0', 'X'):
                    print('Only "X" or "0" possible. Try again...')
                Player.marker = (tmp_marker, '0' if tmp_marker == 'X' else 'X')
            else:
                print(f'Computer SIGN is: {Player.marker[1]}\n')
        except IndexError:
            print(f'You have to call Human init before .')

    def get_mark(self):
        return Player.marker[0] if self.human_mode else Player.marker[1]


class Game:
    WIN_POSITIONS = [
        [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]
    ]

    def __init__(self):
        self.board = Board()

    @staticmethod
    def first_move():
        return random.randint(0, 1)

    def next_move(self, new_position, player):
        self.board.positions[new_position] = player.get_mark()

    def is_winner(self, player):
        for combination in self.WIN_POSITIONS:
            if len(set(combination)) == 1: return True
        return False


if __name__ == '__main__':
    human_player = Player(input('Enter your nick -> '))
    ai_player = Player(human_mode=False)
