from pynput import keyboard
from pynput.keyboard import Key, Controller


board = Controller()


board.type("ASDsadas")
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))



# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
