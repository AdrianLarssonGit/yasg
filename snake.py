import time
class Snake:
    def __init__(self, symbol, boarddimesionarray):
        self.symbol = symbol
        self.position = [0, 0]
        self.positionUpdated = [[0,0]]
        self.size = 1
        self.boarddimesionarray = boarddimesionarray

    def print(self):
        print(self.symbol, end='')

    def snake_position_height(self):
        return(self.position[0])

    def snake_position_width(self):
        return(self.position[1])

    def update_position(self, move):
        if move == "d" and self.position[1]+2 <= self.boarddimesionarray[1]:
            self.position[1] = self.position[1]+1
            self.symbol = ">"
        elif move == "d" and self.position[1]+2 >= self.boarddimesionarray[1]:
            print("Game over! D")
            time.sleep(3)
        elif move == "s" and self.position[0]+2 <= self.boarddimesionarray[0]:
            self.position[0] = self.position[0] + 1
            self.positionUpdated[0][0] = self.positionUpdated[0][0] + 1
            self.symbol = "v"
        elif move == "s" and self.position[0]+2 >= self.boarddimesionarray[0]:
            print("Game over! S")
        elif move == "a" and self.position[1] > 0:
            self.position[1] = self.position[1] - 1
            self.symbol = "<"
        elif move == "a" and self.position[1] <= 0:
            print("Game over! A")
            time.sleep(3)
        elif move == "w" and self.position[0] > 0:
            self.position[0] = self.position[0] - 1
            self.symbol = "^"
        elif move == "w" and self.position[0] <= 0:
            print("Game over! W")
            time.sleep(3)
        else:
            print("Game over!")


    def size(self):
        return self.size()

    def update_size(self):
        self.size += 1

    def get_position(self):
        return self.position
