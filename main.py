from game import Game
import subprocess
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
    while True:
        move = input()
        game.update_snake_position(move)
        game.render()




    break
