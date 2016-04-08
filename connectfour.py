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

    def add_r_token_to_board():

    def add_y_token_to_board():



# def check_the_board():
#     for i in the_board:
def open_account_database():
    with open('4-moves.txt') as data_file:
        database = data_file.read()
    return database



pre_existing_moves = [4, 3, 5, 6, 4, 4, 5, 3, 6, 2, 7, 7, 3, 7, 4, 5, 6, 5]

the_board = []
rows = []

for i in range(7):
    rows.append(0)

for columns in range(6):
    the_board.append(rows)

# move_database = open_account_database()
red_move_list = [i-1 for i in pre_existing_moves[::2]]
yellow_move_list = [i-1 for i in pre_existing_moves[1::2]]

def add_r_token_to_board(red_move_list, the_board):
    move_index = []
    for i in red_move_list:
        move_index.append(i - 1)
    for i in move_index:
        x = 0
        if the_board[-1][i] == 0:
            the_board[-1 - x][i] = 'R'
            print('R added token')
        elif the_board[-1 -x][i] != 0:
            x += 1
            the_board[-1 - x][i] = 'R'
            print(x)
            print('R added a token on top of another')
        elif:

        elif:
    return the_board


add_token_to_board(pre_existing_moves, the_board)
    # board[-1][0]

print(the_board[-6])
print(the_board[-5])
print(the_board[-4])
print(the_board[-3])
print(the_board[-2])
print(the_board[-1])
