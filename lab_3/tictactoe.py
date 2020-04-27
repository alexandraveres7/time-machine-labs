import os


class Game:
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.move_count = 0

    def __str__(self):
        text = ""
        text += "Game(" + os.linesep
        text += "     " + str(self.board[0]) + os.linesep
        text += "     " + str(self.board[1]) + os.linesep
        text += "     " + str(self.board[2]) + os.linesep
        text += ')' + os.linesep

        return text

    def __repr__(self):
        return {
            f"""Game(
                {self.board[0]}
                {self.board[1]}
                {self.board[2]}
            )"""
        }

    def won(self):
        if self.board[0] == ['X', 'X', 'X'] or self.board[0] == ['O', 'O', 'O']:
            return True
        else:
            return False

    def mark(self, x, y):
        self.move_count += 1
        if self.move_count % 2 == 1:
            symbol = 'X'
        else:
            symbol = 'O'
        self.board[x][y] = symbol
        if self.won():
            print(symbol, 'won')


g = Game()
g.mark(0, 0)
g.mark(1, 2)
g.mark(0, 1)
g.mark(1, 2)
g.mark(0, 2)
print(str(g))
