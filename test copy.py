#hellohellohellohellohelloHiHiHihelloHi








from random import randint
import random
import time

def dot_spam(text, remove):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    if remove == True:
        print(" " * len(text), end='\r')

dot_spam("The murderer has killed everyone except you.", False)