import random
from rich.console import Console
from rich import traceback


class Board:
    def __init__(self):
        self.positions = [' ' for element in range(10)]

    def redraw(self):
        h_line = '---+---+---'
        v_line = '|'
        print(f' {self.positions[7]} {v_line} {self.positions[8]} {v_line} {self.positions[9]}')
        print(h_line)
        print(f' {self.positions[4]} {v_line} {self.positions[5]} {v_line} {self.positions[6]}')
        print(h_line)
        print(f' {self.positions[1]} {v_line} {self.positions[2]} {v_line} {self.positions[3]}')

    def get_current_frame(self):
        return self.positions.copy()

    def is_free(self, pos):
        return self.positions[pos] == ' '

    def set_board_positions(self, pos_arr):
        self.positions = pos_arr

    def is_full(self):
        return True if ' ' not in set(self.positions) else False

    def clear(self):
        self.positions = [' ' for element in range(10)]


class Player:
    marker = ()

    def __init__(self, name='Human', human_mode=True):
        self.human_mode = human_mode
        self.name = name if human_mode else 'Computer'
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
        self.human_player = Player(input('Enter your nick -> '))
        self.ai_player = Player(human_mode=False)
        self.turn = None
        self.is_playing = False

    def first_move(self):
        if random.randint(0, 1):
            return self.ai_player
        else:
            return self.human_player

    def set_move(self, new_position, board=None):
        if not board:
            board = self.board
        board.positions[new_position] = self.turn.get_mark()

    def is_winner(self, board=None):
        if not board:
            board = self.board
        for combination in self.WIN_POSITIONS:
            seq = set([board.positions[item] for item in combination])
            if (len(seq) == 1) and (' ' not in seq):
                return True
        return False

    def engage_human_move(self):
        while (move := int(input('Your next move ( 1-9) -> '))) not in range(1, 10) or not self.board.is_free(move):
            print('Illegal move! Try again ...')
        return move

    def get_random_move(self, moves_arr):
        legal_moves = []
        for board_cell in moves_arr:
            if self.board.is_free(board_cell):
                legal_moves.append(board_cell)
        return random.choice(legal_moves) if legal_moves else None

    # AI Implementation. Has to be refactored
    def engage_ai_move(self):
        tmp_board = Board()

        for move in range(1, 10):
            tmp_board.set_board_positions(self.board.get_current_frame())
            if tmp_board.is_free(move):
                self.set_move(move, tmp_board)
                if self.is_winner(tmp_board):
                    return move

        for move in range(1, 10):
            tmp_board.set_board_positions(self.board.get_current_frame())
            if tmp_board.is_free(move):
                self.set_move(move, tmp_board)
                if self.is_winner(tmp_board): return move

        if move := self.get_random_move([1, 3, 7, 9]): return move

        if self.board.is_free(5):
            return 5

        return self.get_random_move([2, 4, 6, 8])

    def loop(self):
        while True:
            self.turn = self.first_move()
            print(f'{self.turn.name} moves first!')
            self.is_playing = True
            while self.is_playing:
                if self.turn.human_mode:
                    self.board.redraw()
                    move = self.engage_human_move()
                    self.set_move(move)
                    if self.is_winner():
                        self.board.redraw()
                        print(f'Congrats! {self.turn.name} WON !!!')
                        self.is_playing = False
                    else:
                        if self.board.is_full():
                            self.board.redraw()
                            print('O-o-ops! DRAW !!!')
                            break
                        else:
                            self.turn = self.ai_player
                else:
                    move = self.engage_ai_move()
                    self.set_move(move)
                    if self.is_winner():
                        self.board.redraw()
                        print(f'{self.turn.name} WON !!!')
                        self.is_playing = False

                    else:
                        if self.board.is_full():
                            self.board.redraw()
                            print('O-o-ops! DRAW !!!')
                            break
                        else:
                            self.turn = self.human_player
            if input('Play again ? ( y / n) ').lower().startswith('y'):
                self.board.clear()
            else:
                break


def main():
    game = Game()
    game.loop()


if __name__ == '__main__':
    traceback.install()
    console = Console()
    main()
