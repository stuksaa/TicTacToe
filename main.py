from game import TicTacToe
import controller


def main():
    tictactoe = TicTacToe()

    while True:
        print()
        print('x player move...')
        if controller.move_player(tictactoe, 'x'):
            break

        print()
        print('o player move...')
        if controller.move_player(tictactoe, 'o'):
            break


if __name__ == '__main__':
    main()