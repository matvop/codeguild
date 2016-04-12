# Andrew, Matt, Andrea
# Connect Four Game
#
# def convert_moves_to_index(move):
#     index = move - 1
#     return index


class Board(object):
    def __init__(self, move_list):
        self.the_board = [[0 for i in range(7)] for i in range(6)]
        self.move_list = move_list

    def __repr__(self): #this prints when you print the object i.e. print(my_game)
        return 'Board:\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        self.the_board[-1],
        self.the_board[-2],
        self.the_board[-3],
        self.the_board[-4],
        self.the_board[-5],
        self.the_board[-6])

    def find_column(self, move):
        column = move - 1
        return column

    def find_row_index(self, the_board, move):
        column = self.find_column(move)
        for index, row in enumerate(self.the_board):
            if row[column] == 0:
                return index

    def add_token(self, move_list):
        for index, move in enumerate(move_list):
            if index % 2 == 0:
                self.the_board[self.find_row_index(self.the_board, move)][self.find_column(move)] = 'R'
            else:
                self.the_board[self.find_row_index(self.the_board, move)][self.find_column(move)] = 'Y'
        return self.the_board #once this runs, i think __repr__ will print



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


def create_move_list():
    move_database = open_account_database()
    move_list = []
    for i in move_database[1:-1]:
        move_list.append(int(i))
    return move_list

def main():
    move_list = create_move_list()
    my_game = Board(move_list)
    my_game.add_token(move_list)
    print(my_game)

main()
