import time


def rules():
    return 'The object of Tic Tac Toe is to get three in a row.' \
          '\nYou play on a three by three game board.' \
          '\nThe first player is known as X and the second is O.' \
          '\nPlayers alternate placing Xs and Os on the game board until' \
          '\neither opponent has three in a row or all nine squares are filled.\n'


def board():
    print('\nHere is the board:')
    print(' --- --- --- ')
    print('|   |   |   |')
    print(' --- --- --- ')
    print('|   |   |   |')
    print(' --- --- --- ')
    print('|   |   |   |')
    print(' --- --- --- ')


def main():
    print(rules())
    print("The game will start in 3 seconds. PREPARE YOURSELF!")
    time.sleep(3)
    board()
    question = int(input('where you want to place your X (row,col)?'))


if __name__ == '__main__':
    main()
