import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
#https://dino-chrome.com/
#100%
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(640, 680):
        for j in range(450, 480):
            if data[i, j] <100:
                hit("down")
                return

  #Draw the rectanle for cactus
    for i in range(640, 680):
        for j in range(490, 500):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print(" Hey.... DIno game is about to start in 3 Seconds")
    time.sleep(3)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
        #print(asarray(image))
''''''
