from Game import TicTacToe


def move_player(tictactoe, player):
    free_position = False
    while not free_position:
        # row coordinate
        valid_row_coord = False
        while not valid_row_coord:
            try:
                r_coord = int(input('set the row position (1-3): ')) - 1

                if r_coord < 0 or r_coord > 2:
                    raise ValueError
                valid_row_coord = True
            except ValueError:
                print('invalid input! try again...')

        # column coordinate
        valid_col_coord = False
        while not valid_col_coord:
            try:
                c_coord = int(input('set the column position (1-3): ')) - 1

                if c_coord < 0 or c_coord > 2:
                    raise ValueError
                valid_col_coord = True
            except ValueError:
                print('invalid input! try again...')

        if tictactoe.check_position(r_coord, c_coord):
            tictactoe.set_move(player, r_coord, c_coord)
            tictactoe.print_board()
            print()
            if tictactoe.check_game(player, r_coord, c_coord):
                return True
            free_position = True
        else:
            print('reserved table position! please set again...')

        return False


def main():
    tictactoe = TicTacToe()

    while True:
        print()
        print('x player move...')
        if move_player(tictactoe, 'x'):
            break

        print()
        print('o player move...')
        if move_player(tictactoe, 'o'):
            break


if __name__ == '__main__':
    main()