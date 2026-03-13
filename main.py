from random import randint
import time

def intro():
    print("--Welcome--")
    time.sleep(1.2)
    name = input("Please enter your name:\n")
    print(f"Hello, {name}, welcome to the game.")
    time.sleep(1)
    read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    while read_rules not in ['y', 'yes', 'n', 'no']:
        print("Sorry. I did not quite catch that.")
        read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    if read_rules in ['y', 'yes']:
        print("rules here")
    print("The game will now begin.")
    return name

def roles():
    comp1 = ""
    comp2 = ""
    comp3 = ""
    comp4 = ""
    comp5 = ""
    comp6 = ""
    comps = [comp1, comp2, comp3, comp4, comp5, comp6]
    player = randint(0,1)
    if player == 0:
        player = "surv"
    else:
        player = "murd"
    if player == "murd":
        comp1 = comp2 = comp3 = comp4 = comp5 = comp6 = "surv"
    else:
        random_murd = randint(1, 6)
        for i in range(len(comps)):
            if i + 1 == random_murd:
                comps[i] = "murd"
            else:
                comps[i] = "surv"

    print("Your selected role is...") 
    select = "selecting"
    for i in range(5):
        select += "."
        print(select, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(select), end='\r')
    if player == "murd":
        print("🔪 murderer.")
    else:
        print("😨survivor.")

    return player, comp1, comp2, comp3, comp4, comp5, comp6

def energy(pts):
    if pts >= 200:
        lv = "hyper"
    elif pts >= 150:
        lv = "energetic"
    elif pts >= 100:
        lv = "neutral"
    elif pts >= 50:
        lv = "tired"
    else:
        lv = "exhausted"
    return lv


intro()
sus_points = 0
energy_points = randint(500,540)
energy_lv = energy(energy_points)
print(energy_points)
print(energy_lv)