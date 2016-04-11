# Andrew, Matt, Andrea
# Connect Four Game
#
# def convert_moves_to_index(move):
#     index = move - 1
#     return index


class Board(object):
    def __init__(self):
        rows = self.rows
        columns = self.columns

    def __repr__(self):
        pass


class Token(object):
    def __init__(self):
        red_token = self.red_token
        yellow_token = self.yellow_token

    def __repr__(self):
        pass


# move_list = [4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5]
#
# the_board =[
# [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]
# ]
# def make_the_board():
#     the_board = []
#     for row_index in range(6):
#         row = []
#         for col_index in range(7):
#             row.append(0)
#         the_board.append(row)
#     return the_board


def open_account_database():
    with open('4-moves.txt') as data_file:
        database = data_file.read().split()
    return database


def make_the_board():
    the_board = [[0 for i in range(7)] for i in range(6)]
    return the_board


def find_column(move):
    column = move - 1
    return column


def find_row_index(the_board, move):
    column = find_column(move)
    for index, row in enumerate(the_board):
        if row[column] == 0:
            return index


def add_token(the_board, move_list):
    for index, move in enumerate(move_list):
        if index % 2 == 0:
            the_board[find_row_index(the_board, move)][find_column(move)] = 'R'
        else:
            the_board[find_row_index(the_board, move)][find_column(move)] = 'Y'
    return the_board


def convert_database_to_list():
    move_database = open_account_database()
    move_list = []
    for i in move_database[1:-1]:
        move_list.append(int(i))
    return move_list


def print_results(the_board):
    print(the_board[-1])
    print(the_board[-2])
    print(the_board[-3])
    print(the_board[-4])
    print(the_board[-5])
    print(the_board[-6])


move_list = convert_database_to_list()
the_board = make_the_board()
add_token(the_board, move_list)
print_results(the_board)
