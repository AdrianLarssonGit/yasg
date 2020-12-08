from snake import Snake
class Game():
    def __init__(self, height, width, snake_symbol):
        self.height = height
        self.width = width
        self.board = []
        self.snake = Snake(snake_symbol)
        # Create 10 row board
        i = 0
        while i < 10:
            l = ["x"] * 10
            self.board.append(l)
            i += 1

    def render(self):

        i = 0
        print(" -"*(len(self.board)-3))
        while i < len(self.board):
            print("| ", end='')
            for list in self.board[i]:
                print(list, end='')
            print(" |")
            i += 1
        print(" -"*(len(self.board)-3))

        print(self.snake.print())



