import pyautogui
import time

def jump():
    pyautogui.press('space')

def detect_obstacle():
    screenshot = pyautogui.screenshot(region=(500, 350, 50, 50))
    for pixel in screenshot.getdata():
        if pixel == (83, 83, 83):  # Color of the obstacle
            return True
    return False

time.sleep(2)  # Time to switch to the game window

while True:
    if detect_obstacle():
        jump()
