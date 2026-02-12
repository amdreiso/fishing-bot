
import pyautogui as p

RUNNING = True
TIME = 0

color = (0, 0, 0)

while RUNNING:
    x, y = p.position()
    print(x, y)
    width = 1
    height = 100
    xoff = x - width / 2
    yoff = y - height / 2
    for i in range(width):
        for j in range(height):
            if p.pixelMatchesColor(int(xoff + i), int(yoff + j), color):
                print("found fish")
                p.dragTo(x, y, 1)


