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

    def set_move(self, player, r_coord, c_coord):
        self.tictactoe_board[r_coord][c_coord] = player
        
        check_game(player, r_coord, c_coord)

        self.nof_moves++


    def check_game(self, player, r_coord, c_coord):
        #check row
        for i in range(self.board_size):
            if(self.tictactoe_board[r_coor][i]!=player):
                break
            if i == self.board_size-1:
                #player nyert
        
        #check column
        for i in range(self.board_size):
            if(self.tictactoe_board[i][c_coord]!=player):
                break
            if i == self.board_size-1:
                #player nyert
        
        #check diagonal
        if r_coord == c_coord:
            for i in range(self.board_size):
                if self.tictactoe_board[i][i]!=player:
                    break
                if i == self.board_size-1
                    #player nyert

        #check antidiagonal
        if r_coord + c_coord == self.board_size-1:
            for i in rang(self.board_size):
                if self.tictactoe_board[i][self.board_size-1-i]!=player
                    break
                if i == self.board_size-1:
                    #player nyert
        
        if self.nof_moves == self.board_size ** 2:
            #dontetlen
