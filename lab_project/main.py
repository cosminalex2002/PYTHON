import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.playerA = "X"
        self.playerAI = "O"
        self.currentPlayer = self.playerA
        self.winner = None
        self.gameOver = False
        self.difficulty = None
        self.alternate = 0
        self.score = {"playerA": 0, "playerAI": 0, "tie": 0}




    def changePlayer(self):
        if self.currentPlayer == self.playerA:
            self.currentPlayer = self.playerAI
        else:
            self.currentPlayer = self.playerA



    def moveAiRandom(self):
        while True:
            move = random.randint(0,8)
            if self.board[move] == " ":
                self.board[move] = self.currentPlayer
                break

    def moveAiBestMove(self):
        maxDepth = 9 - self.board.count("X") - self.board.count("O")
        bestScore = float('-inf')
        bestMove = None

        #iterate through each position on the board
        for i in range(9):
            if self.board[i] == " ":
                board_copy = self.board[:]
                #simulate AI move on the copied board
                board_copy[i] = self.playerAI

                #calculate the score for the AI's move using minimax algorithm
                score = self.minimax(board_copy, 0, False, maxDepth)

                #update the best move if a higher score is found
                if score > bestScore:
                    bestScore = score
                    bestMove = i

        #place the AI symbol in the best possible position on the actual board
        self.board[bestMove] = self.playerAI

    def minimax(self, board, depth, maximizingPlayer, maxDepth):
        #check if the game has ended or the maximum depth has been reached
        if depth >= maxDepth or self.checkGameOver(board):
            self.gameOver = False
            # Evaluate the score for the current state of the board
            if self.hasWon(board, self.playerAI):
                return 1 * (10 - depth)
            elif self.hasWon(board, self.playerA):
                return -1 * (10 - depth)
            else:
                return 0

        #if its the turn of the maximizing player (AI)
        if maximizingPlayer:
            bestScore = float('-inf')
            #iterate through each position on the board
            for i in range(9):
                if board[i] == " ":
                    #make a move for the AI
                    board[i] = self.playerAI
                    #recursively calculate the score for the next move
                    score = self.minimax(board, depth + 1, False, maxDepth)
                    #undo the move
                    board[i] = " "
                    #update the best possible score for the AI
                    bestScore = max(score, bestScore)
            return bestScore
        else:
            #if itd the turn of the minimizing player (human)
            bestScore = float('inf')
            #iterate through each position on the board
            for i in range(9):
                if board[i] == " ":
                    #make a move for the human player
                    board[i] = self.playerA
                    #recursively calculate the score for the next move
                    score = self.minimax(board, depth + 1, True, maxDepth)
                    #undo the move
                    board[i] = " "
                    #update the best possible score for the human player
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
        if self.hasWon(board, self.playerA):
            self.winner = self.playerA
            self.gameOver = True
            return True
        elif self.hasWon(board, self.playerAI):
            self.winner = self.playerAI
            self.gameOver = True
            return True
        elif board.count(" ") == 0:
            self.winner = None
            self.gameOver = True
            return True
        else:
            return False

    def askDifficulty(self):
        while True:
            self.difficulty = input("Choose the difficulty : \n 1. AI move random \n 2. AI move one move random, one the best move \n 3. AI the best move always \n")
            if self.difficulty == "1":
                break
            elif self.difficulty == "2":
                break
            elif self.difficulty == "3":
                break
            else:
                print("Invalid input!")

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
        winCombination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))
        for combination in winCombination:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                self.winner = self.currentPlayer
                self.gameOver = True
                break

    def moveAiMedium(self):
        if self.alternate == 0:
            self.moveAiRandom()
            self.alternate = 1
        else:
            self.moveAiBestMove()
            self.alternate = 0


    def startGame(self):
        self.askDifficulty()

        while not self.gameOver:
            self.printBoard()
            self.printStatus()

            if self.currentPlayer == self.playerAI:
                if self.difficulty == "1":
                    self.moveAiRandom()
                elif self.difficulty == "2":
                    self.moveAiMedium()
                elif self.difficulty == "3":
                    self.moveAiBestMove()
            else:
                self.move()
            self.checkGameOver(self.board)
            self.changePlayer()
        self.printBoard()
        self.printResult()
        self.updateScore()
        self.printScore()
        self.playAgain()

    def playAgain(self):
        while True:
            playAgain = input("Play again? (y/n): ")
            if playAgain == "y":
                self.board = [" " for _ in range(9)]
                self.gameOver = False
                self.currentPlayer = self.playerA
                self.winner = None
                self.difficulty = None
                self.alternate = 0
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

if __name__ == "__main__":
    game = TicTacToe()
    game.startGame()
