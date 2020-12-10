from game import Game
import time
import _thread

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

    def input_thread(a_list):
        input()
        a_list.append(True)

    def game_session(move):
        a_list = []
        _thread.start_new_thread(input_thread, (a_list,))
        while not a_list:
            time.sleep(1)
            game.update_snake_position(move)
            game.render()


    move = input()
    game_session(move)

    break
