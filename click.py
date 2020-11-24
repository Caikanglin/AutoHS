import win32gui
import win32api
import win32con
import time
from pynput.mouse import Button, Controller
import random

OPERATE_INTERVAL = 0.3


def left_click(x, y):
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    mouse = Controller()
    time.sleep(0.2)
    mouse.position = (x, y)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)


def right_click(x, y):
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    mouse = Controller()
    time.sleep(0.2)
    mouse.position = (x, y)
    time.sleep(0.2)
    mouse.press(Button.right)
    time.sleep(0.2)
    mouse.release(Button.right)


def math_opponent():
    left_click(1400, 900)
    left_click(1400, 900)


def flush_uncertain():
    left_click(50, 400)


def end_turn():
    left_click(1500, 500)


def choose_card():
    left_click(950, 500)
    left_click(960, 860)


def emoj():
    emoj_list = [(800, 780), (1140, 780), (800, 680), (1150, 680)]
    right_click(950, 830)
    time.sleep(OPERATE_INTERVAL)
    x, y = emoj_list[random.randint(0, 3)]
    left_click(x, y)
    time.sleep(OPERATE_INTERVAL)


def use_card():
    card_list = [(700, 1060), (800, 1060), (880, 1060), (950, 1060), (1050, 1060), (1150, 1060)]
    card_list.reverse()
    for coor_tuple in card_list:
        left_click(coor_tuple[0], coor_tuple[1])
        time.sleep(OPERATE_INTERVAL)
        left_click(950, 200)


def use_skill():
    left_click(1150, 850)


def minion_attack():
    for minion_location in range(530, 1450, 100):
        left_click(minion_location, 600)
        time.sleep(OPERATE_INTERVAL)
        left_click(950, 200)


def hero_atrack():
    left_click(950, 830)
    time.sleep(OPERATE_INTERVAL)
    left_click(950, 200)


if __name__ == "__main__":
    left_click(1400, 900)
