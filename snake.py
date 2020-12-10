import time
class Snake:
    def __init__(self, symbol, boarddimesionarray):
        self.symbol = symbol
        self.position = [0, 0]
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
        elif move == "d" and self.position[1]+2 >= self.boarddimesionarray[1]:
            print("Game over! D")
            time.sleep(3)
        elif move == "s" and self.position[0]+2 <= self.boarddimesionarray[0]:
            self.position[0] = self.position[0] + 1
        elif move == "s" and self.position[0]+2 >= self.boarddimesionarray[0]:
            print("Game over! S")
        elif move == "a" and self.position[1] > 0:
            self.position[1] = self.position[1] - 1
        elif move == "a" and self.position[1] <= 0:
            print("Game over! A")
            time.sleep(3)
        elif move == "w" and self.position[0] > 0:
            self.position[0] = self.position[0] - 1
        elif move == "w" and self.position[0] <= 0:
            print("Game over! W")
            time.sleep(3)
        else:
            print("Game over!")
        # else:
        #     print("Game ever! D")
        #     print(self.position)
        #     print(self.boarddimesionarray)
        #     time.sleep(10)
        #
        # if move == "s" and self.position[0]+2 <= self.boarddimesionarray[0]:
        #     self.position[0] = self.position[0]+1
        # else:
        #     print("Game over! S")
        #     time.sleep(10)
        #
        # if move == "a" and self.position[1] > 0:
        #     self.position[1] = self.position[1]-1
        # else:
        #     print("Game over! A")
        #
        # if move == "w" and self.position[0] > 0:
        #     self.position[0] = self.position[0]-1
        # else:
        #     print("Game over! W")

    def size(self):
        return self.size()

    def update_size(self):
        self.size += 1

    def get_position(self):
        return self.position
