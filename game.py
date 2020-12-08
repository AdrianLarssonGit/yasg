from snake import Snake
class Game():
    def __init__(self, height, width, board_symbol, snake_symbol):
        self.height = height
        self.width = width
        self.board = []
        self.snake = Snake(snake_symbol)
        # Create 10 row board
        i = 0
        while i < 10:
            l = [board_symbol] * 10
            self.board.append(l)
            i += 1

    def render(self):
        i = 0
        print(" -"*(len(self.board)-3))
        snakeOnThisLine = False
        while i < len(self.board):
            print("| ", end='')
            if self.snake.snake_position_height() == i:
                snakeOnThisLine = True
            else:
                snakeOnThisLine = False

            for subList in self.board[i]:
                subCounter = 0
                if snakeOnThisLine:
                    if self.snake.snake_position_width() == subCounter:
                        print(self.snake.print, end='')
                        snakeOnThisLine = False
                    else:
                        print(sublist[subCounter], end='')
                    subCounter += 1

            print(" |")
            i += 1
        print(" -"*(len(self.board)-3))

        print(self.snake.print())



