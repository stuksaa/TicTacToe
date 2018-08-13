
from Game import TicTacToe


def main():

    tictactoe = TicTacToe()

    tictactoe.print_board()

    tictactoe.set_move('x', 0, 0)

    tictactoe.print_board()


if __name__ == '__main__':
    main()



