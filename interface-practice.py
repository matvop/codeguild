class DictTTTBoard:
    def __init__(self):
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, token):
        if x == 0:
            key_part1 = 'a'
        if x == 1:
            key_part1 = 'b'
        if x == 2:
            key_part1 = 'c'
        if y == 0:
            key_part2 = '1'
        if y == 1:
            key_part2 = '2'
        if y == 2:
            key_part2 = '3'
        key = key_part1 + key_part2
        self.pos_to_token[key] = token
        return self.pos_to_token

    def won(self):
        check_list = []
        sorted_keys = sorted(list(self.pos_to_token))
        sorted_value_list = list(map(self.pos_to_token.get, sorted_keys))
        col_list = [sorted_value_list[i:i+3] for i in range(
                    0, len(sorted_value_list), 3)]
        check_list += col_list
        row_list = [list(i) for i in list(zip(*col_list))]
        check_list += row_list
        diag_list = [[row_list[0][0], row_list[1][1], row_list[2][2]],
                     [row_list[0][2], row_list[1][1], row_list[2][0]]]
        check_list += diag_list
        for i in check_list:
            if i == ['X', 'X', 'X']:
                return 'X'
            if i == ['O', 'O', 'O']:
                return 'O'
        return None

    def __str__(self):
        return '{}|{}|{}\n{}|{}|{}\n{}|{}|{}\n'.format(
        (self.pos_to_token['a1']),
        (self.pos_to_token['b1']),
        (self.pos_to_token['c1']),
        (self.pos_to_token['a2']),
        (self.pos_to_token['b2']),
        (self.pos_to_token['c2']),
        (self.pos_to_token['a3']),
        (self.pos_to_token['b3']),
        (self.pos_to_token['c3']))


class ListListTTTBoard:
    def __init__(self):
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, token):
        if self.rows[y][x] == ' ':
            self.rows[y][x] = token
        return self.rows

    def won(self):
        check_list = []
        check_list += self.rows
        check_list += [list(i) for i in list(zip(*self.rows))]
        check_list += [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                       [self.rows[0][2], self.rows[1][1], self.rows[2][0]]]
        for i in check_list:
            if i == ['X', 'X', 'X']:
                return 'X'
            if i == ['O', 'O', 'O']:
                return 'O'
        return None

    def __str__(self):
        return '{}\n{}\n{}\n'.format(
        '|'.join(self.rows[0]),
        '|'.join(self.rows[1]),
        '|'.join(self.rows[2]))


class CoordsTTTBoard:
    def __init__(self):
        """Initializes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, token):
        self.x_y_token_triplets.append((x, y, token))

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        check_list = []
        row_list = [[' ' for i in range(3)]for i in range(3)]
        for i in self.x_y_token_triplets:
            x = i[0]
            y = i[1]
            token = i[2]
            if row_list[y][x] == ' ':
            	row_list[y][x] = token
        check_list += row_list
        check_list += [list(i) for i in list(zip(*row_list))]
        check_list += [[row_list[0][0], row_list[1][1], row_list[2][2]],
                       [row_list[0][2], row_list[1][1], row_list[2][0]]]
        for i in check_list:
            if i == ['X', 'X', 'X']:
                return 'X'
            if i == ['O', 'O', 'O']:
                return 'O'
        return None

    def __str__(self):
        board = [[' ' for i in range(3)]for i in range(3)]
        for i in self.x_y_token_triplets:
            x = i[0]
            y = i[1]
            token = i[2]
            if board[y][x] == ' ':
                board[y][x] = token
        return '{}\n{}\n{}\n'.format(
        '|'.join(board[0]),
        '|'.join(board[1]),
        '|'.join(board[2]))


def play(board):
    """Plays a test game on an empty board.

    Asserts that the board is working properly.
    """
    board.place(1, 1, 'X')
    board.place(0, 0, 'O')
    board.place(1, 0, 'X')
    print(board)
    assert str(board) == "O|X| \n |X| \n | | \n"
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'


def main():
    board1 = DictTTTBoard()
    play(board1)
    board2 = ListListTTTBoard()
    play(board2)
    board3 = CoordsTTTBoard()
    play(board3)


main()
