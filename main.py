
import pyautogui as p

RUNNING = True
TIME = 0

# R G B | 0 - 255
color = (0, 0, 0)

fishy = 0

while RUNNING:
    x, y = p.position()
    height = 100
    yoff = y - height / 2
    for i in range(height):
        if p.pixelMatchesColor(x, int(yoff + i), color):
            fishy += 1 
            print("found fish: ", fishy)
            p.dragTo(x, y, 1)


