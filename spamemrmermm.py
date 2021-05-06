import pyautogui as pg
import time


time.sleep(3)
strr = 'youre a piece of shit you fucking shit ass dick'
for i in range(0,10):
    for msg in strr.split(" "): 
        pg.typewrite(msg + '\n')