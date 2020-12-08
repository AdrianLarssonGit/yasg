class Snake:
    def __init__(self, symbol):
        self.symbol = symbol
        self.position = [0, 0]

    def print(self):
        return self.symbol

    def snake_position_height(self):
        return(self.position[0])

    def snake_position_width(self):
        return(self.position[1])
