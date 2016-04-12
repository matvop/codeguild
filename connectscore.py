

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





# def make_the_board():
#     the_board = []
#     for row_index in range(6):
#         row = []
#         for col_index in range(7):
#             row.append(0)
#         the_board.append(row)
#     return the_board
