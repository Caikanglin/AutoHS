import get_screen
import click
import time
import random
import FSM_action
import keyboard
import sys

if __name__ == "__main__":
    keyboard.add_hotkey("ctrl+q", sys.exit)
    FSM_action.AutoHS_automata()
