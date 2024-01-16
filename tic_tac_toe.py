class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(row)

    def check_win(self, player):
        # check horizontal, vertical, and diagonal winning conditions
        win_conditions = [
            [self.board[0][j] == player and self.board[1][j] == player and self.board[2][j] == player for j in
             range(3)],  # columns
            [self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player for i in
             range(3)],  # rows
            [self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player],  # main diag
            [self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player]  # second diag
        ]
        return any(any(row) for row in win_conditions)

    def change_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def start(self):
        self.print_board()
        while True:
            print("It's {} turn. Enter your move in the format (row, col):".format(self.current_player))
            move = input()
            i, j = map(int, move.split(','))

            if i < 0 or i >= 3 or j < 0 or j >= 3:
                print("Invalid move! Please, try again.")
            else:
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.current_player
                    self.print_board()
                    if self.check_win(self.current_player):
                        print("{} Wins!".format(self.current_player))
                        break
                    self.change_player()
                else:
                    print("Invalid move! Please, try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
