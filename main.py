import numpy as np


class Game:
    def __init__(self, height: int = 6, width: int = 7, players: int = 2):
        self.board = np.zeros((height, width))
        self.rows = height
        self.cols = width
        self.players_total = players
        self.round_counter = 1
        self.direction_pairs = (((0, 1), (0, -1)), ((1, 0), (-1, 0)),
                                ((1, 1), (-1, -1)), ((-1, 1), (1, -1)))
        self.current_player = 1

    def add_chip(self, player_id: int, column: int) -> bool:
        row = self.rows - 1
        column = column - 1
        if 0 > column or column >= self.cols:
            print("Invalid column number!")
            return False
        while self.board[row][column] != 0:
            row -= 1
            if row < 0:
                print("No place for a new chip in this column!")
                return False
        self.board[row][column] = player_id
        print(self.board)
        self.win_check(player_id, row, column)
        return True

    def win_check(self, player_id: int, row: int, column: int):
        for direction_pair in self.direction_pairs:
            line_length = 1
            for direction in direction_pair:
                current_row = row + direction[0]
                current_col = column + direction[1]
                while 0 <= current_row < self.rows and 0 <= current_col < self.cols and \
                        self.board[current_row][current_col] == player_id:
                    line_length += 1
                    if line_length > 3:
                        print(f"Player #{player_id} has won! It took {self.round_counter} rounds.")
                        exit(0)
                    current_row += direction[0]
                    current_col += direction[1]

    def play(self):
        print("Welcome to the Connect4 CLI.\n"
              f"The current settings are: {self.rows} X {self.cols} board "
              f"for {self.players_total} players")
        print(self.board)
        while True:
            column = int(input(
                f"Player #{self.current_player}, enter a column number (1 to {self.cols}): "))
            while not self.add_chip(self.current_player, column):
                column = int(
                    input(f"Please, player #{self.current_player}, enter a valid column number:"))
            self.current_player += 1
            if self.current_player > self.players_total:
                self.current_player = 1
                self.round_counter += 1


if __name__ == '__main__':
    g = Game()
    g.play()
