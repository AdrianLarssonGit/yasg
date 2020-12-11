from pynput import keyboard
from pynput.keyboard import Key
import globals


def on_press(key):
    if key == Key.up:
        key = "w"
        globals.move = key

    if key == Key.down:
        key = "s"
        globals.move = key

    if key == Key.left:
        key = "a"
        globals.move = key

    if key == Key.right:
        key = "d"
        globals.move = key

    try:
        globals.move = key.char
    except AttributeError:
        pass


def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
