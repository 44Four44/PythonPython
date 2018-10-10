import pyautogui
import random
import time

moves = ['up', 'down', 'left', 'right']

time.sleep(2)

while True:
    key = random.choice(moves)
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)
