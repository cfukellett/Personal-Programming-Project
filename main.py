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
    player = randint(0,0)
    if player == 0:
        player = "surv"
    else:
        player = "murd"
    if player == "murd":
        comp1 = comp2 = comp3 = comp4 = comp5 = comp6 = "surv"
    else:
        random_murd = randint(6, 6)
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
        print("🔪 murderer.\n")
    else:
        print("😨survivor.\n")
    time.sleep(2)
    return player, comp1, comp2, comp3, comp4, comp5, comp6

def energy(pts):
    if pts >= 200:
        lv = "Hyper 🤩"
    elif pts >= 150:
        lv = "Energetic 😁"
    elif pts >= 100:
        lv = "Neutral 😐"
    elif pts >= 50:
        lv = "Tired 😫"
    else:
        lv = "Exhausted 🫩"
    return lv


def day(day, suspts, energylv):
    day += 1
    print(f"☀️--Day {day}--☀️")
    print("It's the start of a brand new day.")
    print("Here are your day 1 stats:")
    print(f"🤔 Suspicion Points: {suspts}")
    print(f"⚡Energy Level: {energylv}")
    if day == 1:
        print("There is no danger here. You can freely rest.")
    return day

def night(player_role):
    if player_role == "surv":
        player_sleep = input("Will you sleep? (y/n)\n").lower()
        while player_sleep not in ['y', 'yes', 'n', 'no']:
            print("Sorry. I did not quite catch that.")
            player_sleep = input("Will you sleep? (y/n)\n").lower()
    if player_sleep in ['y', 'yes']:
        player_sleep = True

def playerchosenbias():
    chosen = randint(1,5)
    chosen2 = ""
    if chosen == 1:
        chosen2 = "bias"
    else:
        chosen2 = "unbias"
    if chosen2 == "bias":
        chosen = randint(1,6)
    else:
        chosen = 0
    return chosen

def aicode(playerrole, c1role, c2role, c3role, c4role, c5role, c6role):
    role_list = [playerrole, c1role, c2role, c3role, c4role, c5role, c6role]
    chosen = randint(5,6)
    if chosen == 0:
        chosen = playerchosenbias()
    while role_list[chosen] == 'murd':
        print("test")
        chosen = randint(5,6)
        if chosen == 0:
            chosen = playerchosenbias()
    print(chosen)
    return chosen
    



player_name = intro()
player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role = roles()
sus_points = 0
energy_points = randint(100,140)
energy_lv = energy(energy_points)
day_num = 0
day_num = day(day_num, sus_points, energy_lv)
print(comp6_role)
if player_role == 'surv':
    chosen = aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role)
night(player_role)