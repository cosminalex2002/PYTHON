class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.playerA = "X"
        self.playerAI = "O"
        self.currentPlayer = self.playerA
        self.winner = None
        self.gameOver = False
        self.score = {"playerA": 0, "playerAI": 0, "tie": 0}

    def printBoard(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def printScore(self):
        print("Player A: " + str(self.score["playerA"]))
        print("Player AI: " + str(self.score["playerAI"]))
        print("Tie: " + str(self.score["tie"]))

    def printResult(self):
        if self.winner == self.playerA:
            print("Player A won!")
        elif self.winner == self.playerAI:
            print("Player AI won!")
        else:
            print("Tie!")

    def printStatus(self):
        if self.gameOver:
            self.printResult()
        else:
            print("Player " + self.currentPlayer + " turn")




if __name__ == "__main__":
