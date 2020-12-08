class Snake:
    def __init__(self, symbol):
        self.symbol = symbol
        self.position = [0, 0]

    def print(self):
        print(self.symbol, end='')

    def snake_position_height(self):
        return(self.position[0])

    def snake_position_width(self):
        return(self.position[1])
