import random
import tkinter as tk
from tkinter import messagebox


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

                #calculate the score for the AIs move using minimax
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
            #evaluate the score for the current state of the board
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
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.board = [" " for _ in range(9)]
            self.gameOver = False
            self.currentPlayer = self.playerA
            self.winner = None
            self.difficulty = None
            self.alternate = 0
            self.startGame()
        else:
            print("Thank you for playing!")


    def updateScore(self):
        if self.winner == self.playerA:
            self.score["playerA"] += 1
        elif self.winner == self.playerAI:
            self.score["playerAI"] += 1
        else:
            self.score["tie"] += 1




    def printBoard(self):
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(self.board[i * 3 + j] + "|", end="")
            print()

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











class TicTacToeGUI(TicTacToe):
    def __init__(self):
        super().__init__()

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 20), width=5, height=2,
                                command=lambda position=i * 3 + j: self.make_move(position))
                btn.grid(row=i, column=j)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.difficulty_chosen = False

        label = tk.Label(self.root, text="Choose difficulty:")
        label.grid(row=3, columnspan=3)

        easy_button = tk.Button(self.root, text="Easy", command=self.set_easy)
        easy_button.grid(row=4, column=0)

        medium_button = tk.Button(self.root, text="Medium", command=self.set_medium)
        medium_button.grid(row=4, column=1)

        hard_button = tk.Button(self.root, text="Hard", command=self.set_hard)
        hard_button.grid(row=4, column=2)

        self.score_label = tk.Label(self.root, text="")
        self.score_label.grid(row=5, columnspan=3)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=6, columnspan=3)






    def show_play_again_dialog(self):
        play_again = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
        return play_again

    def start_game(self):
        self.update_GUI()
        if self.gameOver:
            self.show_play_again_dialog()
        else:
            self.root.mainloop()












    def set_easy(self):
        self.difficulty = "1"
        self.difficulty_chosen = True
        self.update_difficulty_buttons()
        self.enable_game_buttons()
        self.start_game_if_ready()

    def set_medium(self):
        self.difficulty = "2"
        self.difficulty_chosen = True
        self.update_difficulty_buttons()
        self.enable_game_buttons()
        self.start_game_if_ready()

    def set_hard(self):
        self.difficulty = "3"
        self.difficulty_chosen = True
        self.update_difficulty_buttons()
        self.enable_game_buttons()
        self.start_game_if_ready()


    def start_game_if_ready(self):
        if self.difficulty_chosen:
            self.start_game()

    def update_difficulty_buttons(self):
        for widget in self.root.winfo_children():
            if widget.winfo_class() == "Button" and widget.cget("text") != "Choose difficulty:":
                widget.config(state="disabled")

    def enable_game_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="normal")


    def make_move(self, position):
        if not self.gameOver and self.difficulty_chosen:
            if self.currentPlayer == self.playerA:
                if self.board[position] == " ":
                    self.board[position] = self.currentPlayer
                    self.buttons[position // 3][position % 3].config(text=self.currentPlayer)
                    self.update_GUI()
                    self.update_game()

    def update_game(self):
        if not self.gameOver:
            self.changePlayer()
            if self.currentPlayer == self.playerAI:
                if self.difficulty == "1":
                    self.moveAiRandom()
                elif self.difficulty == "2":
                    self.moveAiMedium()
                elif self.difficulty == "3":
                    self.moveAiBestMove()

                self.update_GUI()
                self.checkGameOver(self.board)
                if self.gameOver:
                    self.printResult()
                    self.updateScore()
                    self.printScore()
                    self.update_GUI()
                else:
                    self.changePlayer()


    def start_game(self):
        self.update_GUI()
        self.root.mainloop()

    def update_GUI(self):
        for i in range(3):
            for j in range(3):
                position = i * 3 + j
                self.buttons[i][j].config(text=self.board[position],
                                          command=lambda pos=position: self.make_move(pos))

        self.score_label.config(
            text=f"Player A: {self.score['playerA']}   Player AI: {self.score['playerAI']}   Tie: {self.score['tie']}")

        if self.gameOver:
            result_text = ""
            if self.winner == self.playerA:
                result_text = "Player A won!"
            elif self.winner == self.playerAI:
                result_text = "Player AI won!"
            else:
                result_text = "Tie!"

            self.result_label.config(text=result_text)

            play_again = self.show_play_again_dialog()
            if play_again:
                self.board = [" " for _ in range(9)]
                self.gameOver = False
                self.currentPlayer = self.playerA
                self.winner = None
                self.difficulty = None
                self.alternate = 0

                self.difficulty_chosen = False
                self.update_difficulty_buttons()
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].config(text=" ", state="normal")

                self.enable_difficulty_buttons()

                self.result_label.config(text="")
                self.start_game_if_ready()  
            else:
                self.root.destroy()




    def playAgain(self):

        play_again = tk.messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.board = [" " for _ in range(9)]
            self.gameOver = False
            self.currentPlayer = self.playerA
            self.winner = None
            self.difficulty = None
            self.alternate = 0

            # Reset GUI elements
            self.difficulty_chosen = False
            self.update_difficulty_buttons()
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(text=" ", state="normal")

            self.enable_difficulty_buttons()

            self.result_label.config(text="")
            self.start_game_if_ready()
        else:
            self.root.destroy()



    def enable_difficulty_buttons(self):
        for widget in self.root.winfo_children():
            if widget.winfo_class() == "Button" and widget.cget("text") != "Choose difficulty:":
                widget.config(state="normal")


if __name__ == "__main__":
    game = TicTacToeGUI()
    game.start_game()