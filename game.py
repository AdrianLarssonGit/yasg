from snake import Snake


class Game:
    def __init__(self, height, width, board_symbol, snake_symbol):
        self.height = height
        self.width = width
        self.board = []
        self.snake = Snake(snake_symbol)

        # Generate board
        i = 0
        while i < 10:
            l = [board_symbol] * 10
            self.board.append(l)
            i += 1

    def render(self):
        i = 0
        print(" -" * (len(self.board) - 3))
        while i < len(self.board):
            print("| ", end='')
            if self.snake.snake_position_height() == i:
                snakeOnThisLine = True
            else:
                snakeOnThisLine = False

            # Inner list
            subCounter = 0
            for subList in self.board[i]:
                for char in subList:
                    if snakeOnThisLine:
                        if self.snake.snake_position_width() == subCounter:
                            self.snake.print()
                            snakeOnThisLine = False
                            continue
                    print(char, end='')

                subCounter += 1

            print(" |")
            i += 1
        print(" -" * (len(self.board) - 3))

    def update_snake_position(self, move):
        self.snake.update_position(move)

