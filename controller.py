def check_valid_coord(dim):
    # row coordinate
    valid_coord = False

    while not valid_coord:
        try:
            coord = int(input('set the ' + dim + ' position (1-3): ')) - 1
            if coord < 0 or coord > 2:
                raise ValueError
            valid_coord = True
        except ValueError:
            print('invalid input! try again...')

    return coord


def move_player(tictactoe, player):
    free_position = False
    while not free_position:
        # row coordinate
        r_coord = check_valid_coord('row')

        # column coordinate
        c_coord = check_valid_coord('column')

        if tictactoe.check_position(r_coord, c_coord):
            tictactoe.set_move(player, r_coord, c_coord)
            tictactoe.print_board()

            if tictactoe.check_game(player, r_coord, c_coord):
                return True
            free_position = True
        else:
            print()
            print('reserved table position! please set again...')
