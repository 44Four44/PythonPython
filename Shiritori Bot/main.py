from pynput import keyboard
from pynput.keyboard import Key, Controller

run = True
board = Controller()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The dictionary
words = [[]]
# Counts words from each letter so words aren't resused
count = [0]

# Read words
with open('/Users/EthanWang/Python/Shiritori Bot/words.txt', 'r') as file:
    data = file.readlines()
    i = 0
    for line in data:
        if line == '\n':
            i += 1
            words.append([])
            count.append(0)
        else:
            words[i].append(line.rstrip())

def on_press(key):

    if key.char == '1':
        board.press(Key.cmd)
        board.press('a')
        board.release('a')
        board.release(Key.cmd)
    else:
        n = letters.index(key.char)

        if count[n] < len(words[n]):
            board.press(Key.backspace)
            board.release(Key.backspace)

            board.type(words[n][count[n]])

            count[n] += 1

            board.press(Key.enter)
            board.release(Key.enter)
        else:
            print("No more words left")

    return False

# Collect events until released
while run:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


