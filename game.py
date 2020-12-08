class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []
        # Create 10 row board
        i = 0
        while i < 10:
            widthOfBoard = 0
            while widthOfBoard < 10:
                self.board.append()
    def render(self):
        print(self.height, self.width)

