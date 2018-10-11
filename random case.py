import pyautogui
import pyglet
from pynput.keyboard import Key, Controller, Listener
import time
import click
from pyglet.window import key

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A:
        print("A was pressed")

pyglet.app.run()
