from snake import Snake
from apple import Apple
import subprocess

class Game:
    def __init__(self, height, width, board_symbol, snake_symbol):
        self.height = height
        self.width = width
        self.board = []
        self.snake = Snake(snake_symbol)
        self.apple = Apple(width, height)
        self.score = 0

        # Generate board
        i = 0
        while i < 10:
            l = [board_symbol] * 10
            self.board.append(l)
            i += 1

    def render(self):
        subprocess.call("clear")
        i = 0
        print(" -" * (len(self.board) - 3))
        while i < len(self.board):
            print("| ", end='')

            if self.snake.snake_position_height() == i:
                snakeOnThisLine = True
            else:
                snakeOnThisLine = False

            if self.apple.apple_position_height() == i:
                appleOnThisLine = True
            else:
                appleOnThisLine = False

            # Inner list
            subCounter = 0
            for subList in self.board[i]:
                for char in subList:
                    if snakeOnThisLine:
                        if self.snake.snake_position_width() == subCounter:
                            self.snake.print()
                            snakeOnThisLine = False
                            continue
                    if appleOnThisLine:
                        if self.apple.apple_position_width() == subCounter:
                            self.apple.print()
                            snakeOnThisLine = False
                            continue
                    print(char, end='')

                subCounter += 1

            print(" |")
            i += 1
        print(" -" * (len(self.board) - 3))

        if self.apple.position[0] == self.snake.position[0] and self.apple.position[1] == self.snake.position[1]:
            self.apple.update_apple_position()
            self.score += 1
            print("SCORE: " + str(self.score))


    def update_snake_position(self, move):
        self.snake.update_position(move)

