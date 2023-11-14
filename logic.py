from typing import List
import random

class TicTacToeGame:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_turn = 'X'

    def show_board(self):
        for row in self.board:
            print(row)

    def play_turn(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_turn
            self.current_turn = self.change_turn()
            self.show_board()
            return self.judge_winner()
        else:
            return False

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def change_turn(self):
        return 'Y' if self.current_turn == 'X' else 'X'

    def judge_winner(self):
        for i in range(3):
            if self.board[i][0] != ' ' and all(self.board[i][0] == self.board[i][j] for j in range(3)):
                print(self.board[i][0], 'Won')
                return True
            if self.board[0][i] != ' ' and all(self.board[0][i] == self.board[j][i] for j in range(3)):
                print(self.board[0][i], 'Won')
                return True

        if self.board[1][1] != ' ' and ((self.board[0][0] == self.board[1][1] == self.board[2][2]) or 
                                       (self.board[2][0] == self.board[1][1] == self.board[0][2])):
            print(self.board[1][1], 'Won')
            return True

        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            print('Draw')
            return True

        return False

class Player:
    def make_move(self, game: TicTacToeGame):
        raise NotImplementedError

class HumanPlayer(Player):
    def make_move(self, game: TicTacToeGame):
        while True:
            row = input("Input row index: ")
            col = input("Input col index: ")
            if row.isdigit() and col.isdigit():
                r, c = int(row), int(col)
                if game.is_valid_move(r, c):
                    return r, c
                else:
                    print("Invalid move, try again.")

class BotPlayer(Player):
    def make_move(self, game: TicTacToeGame):
        while True:
            r, c = random.randint(0, 2), random.randint(0, 2)
            if game.is_valid_move(r, c):
                print(f"Bot chose: {r}, {c}")
                return r, c
