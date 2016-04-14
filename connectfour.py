# Andrew and Matt
# Connect Four Game

class Board(object):
    def __init__(self, move_list):
        self.the_board = [[' ' for i in range(7)] for i in range(6)]
        self.move_list = move_list

    def __str__(self):
        return '\nConnect Four:\n\n|{}|\n|{}|\n|{}|\n|{}|\n|{}|\n|{}|\n'.format(
        ' '.join(self.the_board[-1]),
        ' '.join(self.the_board[-2]),
        ' '.join(self.the_board[-3]),
        ' '.join(self.the_board[-4]),
        ' '.join(self.the_board[-5]),
        ' '.join(self.the_board[-6]))

    def find_column(self, move):
        column = move - 1
        return column

    def find_row_index(self, move):
        column = self.find_column(move)
        for index, row in enumerate(self.the_board):
            if row[column] == ' ':
                return index

    def add_token(self):
        for index, move in enumerate(self.move_list):
            if index % 2 == 0:
                self.the_board[self.find_row_index(move)][
                               self.find_column(move)] = 'R'
            else:
                self.the_board[self.find_row_index(move)][
                               self.find_column(move)] = 'Y'
        return self.the_board #once this runs, i think __repr__ will print

    def score_grids(self):
        grid = [[self.the_board[0][0:4],
                 self.the_board[1][0:4],
                 self.the_board[2][0:4],
                 self.the_board[3][0:4]],
                [self.the_board[0][1:5],
                 self.the_board[1][1:5],
                 self.the_board[2][1:5],
                 self.the_board[3][1:5]],
                [self.the_board[0][2:6],
                 self.the_board[1][2:6],
                 self.the_board[2][2:6],
                 self.the_board[3][2:6]],
                [self.the_board[0][3:7],
                 self.the_board[1][3:7],
                 self.the_board[2][3:7],
                 self.the_board[3][3:7]],
                [self.the_board[1][0:4],
                 self.the_board[2][0:4],
                 self.the_board[3][0:4],
                 self.the_board[4][0:4]],
                [self.the_board[1][1:5],
                 self.the_board[2][1:5],
                 self.the_board[3][1:5],
                 self.the_board[4][1:5]],
                [self.the_board[1][2:6],
                 self.the_board[2][2:6],
                 self.the_board[3][2:6],
                 self.the_board[4][2:6]],
                [self.the_board[1][3:7],
                 self.the_board[2][3:7],
                 self.the_board[3][3:7],
                 self.the_board[4][3:7]],
                [self.the_board[2][0:4],
                 self.the_board[3][0:4],
                 self.the_board[4][0:4],
                 self.the_board[5][0:4]],
                [self.the_board[2][1:5],
                  self.the_board[3][1:5],
                  self.the_board[4][1:5],
                  self.the_board[5][1:5]],
                 [self.the_board[2][2:6],
                  self.the_board[3][2:6],
                  self.the_board[4][2:6],
                  self.the_board[5][2:6]],
                 [self.the_board[2][3:7],
                  self.the_board[3][3:7],
                  self.the_board[4][3:7],
                  self.the_board[5][3:7]]]
        print(grid)


def open_account_database():
    with open('4-moves.txt') as data_file:
        database = data_file.read().split()
    return database


def create_move_list():
    move_database = open_account_database()
    move_list = []
    for i in move_database[1:-1]:
        move_list.append(int(i))
    return move_list

def main():
    move_list = create_move_list()
    my_game = Board(move_list)
    my_game.add_token()
    print(my_game)
    my_game.score_grids()

main()
