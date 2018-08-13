class TicTacToe:

    board_size = 3

    def __init__(self):
        self.tictactoe_board = [['.' for x in range(self.board_size)] for y in range(self.board_size)]

    def print_board(self):
        print()
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.tictactoe_board[i][j], end=' ')
            print()

    def set_move(self, player, r_coord, c_coord):
        self.tictactoe_board[r_coord][c_coord] = player

