from game import Game
import time
import _thread
from pynput.keyboard import Controller, Key
import globals
while True:
    game = Game(10, 10, " ", ">")
    print("Welcome to Yet Another Snake Game!")
    print("I assume you know the rules for this classic game?")
    print("If you do not please free to do a quick web search and \nand then return.")
    print("Controls are as follows:")
    print("Arrow keys or WSDA to move.\n")
    print("If you are \"one of those people\" VIM keys also work!")
    print("The snake start at 0,0 (Upper left corner)")
    print("Good luck!")
    print("Press any key to start...")
    input()
    game.render()

    globals.move = ""

    def input_thread(a_list):
        globals.move
        globals.move = input()
        a_list.append(True)

    def game_session():
        a_list = []
        _thread.start_new_thread(input_thread, (a_list,))
        while not a_list:
            time.sleep(0.5)
            game.update_snake_position(globals.move)
            game.render()

        if a_list:
            game_session()
            input_thread().join()

    globals.move = input()
    game_session()

    break
