from game import Game
import time
while True:
    print("Welcome to Yet Another Snake Game!")
    print("I assume you know the rules for this classic game?")
    print("If you do not please free to do a quick web search and \nand then return.")
    print("Controls are as follows:")
    print("Arrow keys or WSDA to move.\n")
    print("If you are \"one of those people\" VIM keys also work!")
    game = Game(10, 10, " ", ">")
    print("The snake start at 0,0 (Upper left corner)")
    print("Good luck!")

    game.render()


    def game_session(move):
        game.update_snake_position(move)
        while True:
            time.sleep(1)
            game.update_snake_position(move)
            game.render()
            if input():
                move = input()
                game_session(move)
                break


    move = input()
    game_session(move)

    break
