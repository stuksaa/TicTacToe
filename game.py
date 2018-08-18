class TicTacToe:
    board_size = 3
    nof_moves = 0

    def __init__(self):
        self.tictactoe_board = [['.' for x in range(self.board_size)] for y in range(self.board_size)]

    def print_board(self):
        print()
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.tictactoe_board[i][j], end=' ')
            print()

    def check_position(self, r_coord, c_coord):
        if self.tictactoe_board[r_coord][c_coord] == '.':
            return True
        else:
            return False

    def increase_moves(self):
        self.nof_moves = self.nof_moves + 1

    def check_game(self, player, r_coord, c_coord):
        self.increase_moves()
        # check row
        for j in range(self.board_size):
            if self.tictactoe_board[r_coord][j] != player:
                break
            if j == self.board_size - 1:
                print(player, ' nyert!')
                return True

        # check column
        for i in range(self.board_size):
            if self.tictactoe_board[i][c_coord] != player:
                break
            if i == self.board_size - 1:
                print(player, ' nyert!')
                return True

        # check diagonal
        if r_coord == c_coord:
            for i in range(self.board_size):
                if self.tictactoe_board[i][i] != player:
                    break
                if i == self.board_size - 1:
                    print(player, ' nyert!')
                    return True
        # check antidiagonal
        if r_coord + c_coord == self.board_size - 1:
            for i in range(self.board_size):
                if self.tictactoe_board[i][self.board_size - 1 - i] != player:
                    break
                if i == self.board_size - 1:
                    print(player, ' nyert!')
                    return True
        if self.nof_moves == self.board_size ** 2:
            print('dontetlen')
            return True

        return False

    def set_move(self, player, r_coord, c_coord):
        self.tictactoe_board[r_coord][c_coord] = player
