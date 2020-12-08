class Snake:
    def __init__(self, symbol):
        self.symbol = symbol
        self.position = [0, 0]
        self.size = 1

    def print(self):
        print(self.symbol, end='')

    def snake_position_height(self):
        return(self.position[0])

    def snake_position_width(self):
        return(self.position[1])

    def update_position(self, move):
        self.position[0] = self.position[0]+1
        print(self.position[0])
        print(self.position[1])
