#hellohellohellohellohelloHiHiHihelloHi








from random import randint
import random
import time

def dot_spam(text):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(text), end='\r')

dot_spam("The murderer has killed everyone except you.")