import random

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

    def changePlayer(self):
        self.currentPlayer = self.playerAI if self.currentPlayer == self.playerA else self.playerA

    def moveAiRandom(self):
        while True:
            move = random.randint(0, 8)
            if self.board[move] == " ":
                self.board[move] = self.playerAI
                break

    def moveAiBestMove(self):
        bestScore = float('-inf')
        bestMove = None

        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.playerAI
                score = self.minimax(self.board, False)
                self.board[i] = " "

                if score > bestScore:
                    bestScore = score
                    bestMove = i

        self.board[bestMove] = self.playerAI

    def minimax(self, board, maximizingPlayer):
        if self.checkGameOver(board):
            if self.hasWon(board, self.playerAI):
                return 1
            elif self.hasWon(board, self.playerA):
                return -1
            else:
                return 0

        if maximizingPlayer:
            bestScore = float('-inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.playerAI
                    score = self.minimax(board, False)
                    board[i] = " "
                    bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.playerA
                    score = self.minimax(board, True)
                    board[i] = " "
                    bestScore = min(score, bestScore)
            return bestScore

    def hasWon(self, board, player):
        winCombination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))
        for combination in winCombination:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
                return True
        return False

    def checkGameOver(self, board):
        if " " in board:
            return False
        else:
            if self.hasWon(board, self.playerAI):
                self.winner = self.playerAI
            elif self.hasWon(board, self.playerA):
                self.winner = self.playerA
            else:
                self.winner = "tie"
            return True

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

    def startGame(self):
        while not self.gameOver:
            self.printBoard()
            self.printStatus()

            if self.currentPlayer == self.playerAI:
                self.moveAiBestMove()
            else:
                self.move()
            self.gameOver = self.checkGameOver(self.board)
            self.changePlayer()

        self.printBoard()
        self.printResult()
        self.updateScore()
        self.printScore()
        self.playAgain()

if __name__ == "__main__":
    game = TicTacToe()
    game.startGame()
