import logging
import time
from logic import TicTacToeGame, HumanPlayer, BotPlayer

logging.basicConfig(level=logging.DEBUG,
                    filename=f'./logs/tictactoe_{int(time.time())}.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(filename)s- %(lineno)d  - %(message)s')
logger = logging.getLogger('tictactoe')

def main():
    logger.info('Game start')
    game = TicTacToeGame()
    player1 = HumanPlayer()
    player2 = BotPlayer()  # Change to HumanPlayer() for two-player mode

    while True:
        player = player1 if game.current_turn == 'X' else player2
        row, col = player.make_move(game)

        if game.play_turn(row, col):
            logger.info('Game finished')
            break

if __name__ == '__main__':
    main()
