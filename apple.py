from random import randrange

class Apple:
    def __init__(self, boardWidth, boardHeight):
        self.symbol = "A"
        self.applePosition = [5,5]
        self.baordWidth = boardWidth
        self.boardHeight = boardHeight

    def update_apple_position(self):
        #Gets called when snake eat apple
        randomNewHeight = randrange(0,self.boardHeight)
        randomNewWidth = randrange(0,self.baordWidth)

        self.applePosition = [randomNewHeight, randomNewWidth]

    def apple_position_height(self):
        return self.applePosition[0]

    def apple_position_width(self):
        return self.applePosition[1]

    def print(self):
        print(self.symbol, end='')