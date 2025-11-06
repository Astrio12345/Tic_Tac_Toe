# game.py

import random

class TicTacToe:
    def __init__(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None

    def make_move(self, index):
        if self.board[index] or self.winner:
            return False
        self.board[index] = self.current_player
        if self.check_winner():
            self.winner = self.current_player
        elif "" not in self.board:
            self.winner = "Draw"
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_winner(self):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset(self):
        self.__init__()

    def get_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "winner": self.winner
        }

# ---- BOT LOGIC ----

def check_winner(board):
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None


def make_bot_move(board, bot):
    # 60% chance to play smart, 40% random
    if random.random() > 0.4:
        # Try to win
        for i in range(9):
            if board[i] == "":
                board[i] = bot
                if check_winner(board) == bot:
                    return i
                board[i] = ""

        # Try to block player
        player = 'O' if bot == 'X' else 'X'
        for i in range(9):
            if board[i] == "":
                board[i] = player
                if check_winner(board) == player:
                    board[i] = ""
                    return i
                board[i] = ""

    # Pick random move otherwise
    available = [i for i in range(9) if board[i] == ""]
    if not available:
        return None
    return random.choice(available)
