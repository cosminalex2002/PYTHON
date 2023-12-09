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
        for i in range(3):
            row = self.board[i * 3:(i + 1) * 3]
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
    def startGame(self):
        while not self.gameOver:
            self.printBoard()
            self.printStatus()
            self.move()
            self.checkGameOver()
            self.changePlayer()
        self.printBoard()
        self.printResult()
        self.updateScore()
        self.printScore()
        self.playAgain()

    def move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                if self.board[move - 1] == " ":
                    self.board[move - 1] = self.currentPlayer
                    break
                else:
                    print("Invalid move!")
            except:
                print("Invalid move!")

    def changePlayer(self):
        if self.currentPlayer == self.playerA:
            self.currentPlayer = self.playerAI
        else:
            self.currentPlayer = self.playerA

    def checkGameOver(self):
        self.checkWin()
        self.checkTie()

    def checkWin(self):
        winCombination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))
        for combination in winCombination:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                self.winner = self.currentPlayer
                self.gameOver = True
                break

    def checkTie(self):
        if " " not in self.board:
            self.winner = "tie"
            self.gameOver = True

    def playAgain(self):
        while True:
            playAgain = input("Play again? (y/n): ")
            if playAgain == "y":
                self.board = [" " for _ in range(9)]
                self.gameOver = False
                self.currentPlayer = self.playerA
                self.winner = None
                break
            elif playAgain == "n":
                break
            else:
                print("Invalid input!")
        if playAgain == "y":
            self.startGame()

    def updateScore(self):
        if self.winner == self.playerA:
            self.score["playerA"] += 1
        elif self.winner == self.playerAI:
            self.score["playerAI"] += 1
        else:
            self.score["tie"] += 1

    





if __name__ == "__main__":
    game = TicTacToe()
    game.startGame()