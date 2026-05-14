#hellohellohellohellohelloHiHiHihelloHi








from random import randint
import random
import time
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb

#ze colours
def red(string):
    rgb(string, 255,0,0)

def blue(string):
    rgb(string, 0,0,255)

def green(string):
    rgb(string, 0,255,0)

def yellow(string):
    rgb(string, 255,255,0)

def purple(string):
    rgb(string, 255,0,255)
str(purple)
def dot_spam(text, remove, colour):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(text), end='\r')
    if not remove:
        print(text)

dot_spam("The murderer has killed everyone except you", False, "red")