class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []
        # Create 10 row board
        i = 0
        while i < 10:
            l = [None] * 10
            self.board.append(l)
            i += 1

    def render(self):
        for i in self.board:
            print(i)

