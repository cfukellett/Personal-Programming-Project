from random import randint
import random
import time

def intro():
    print("--Welcome--")
    time.sleep(1.2)
    name = input("Please enter your name:\n")
    print(f"Hello, {name}, welcome to the game.")
    time.sleep(1)
    read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    while read_rules not in ['y', 'yes', 'n', 'no']:
        wronginsert()
        read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    if read_rules in ['y', 'yes']:
        print("rules here")
    print("The game will now begin.")
    return name

def roles():
    players = ["surv", "surv", "surv", "surv", "surv", "surv", "surv"]
    player = randint(0,1)
    murd = 0
    if player == 0:
        players[0] = "surv"
    else:
        players[0] = "murd"
    if players[0] == "surv":
        random_murd = randint(1, 6)
        players[random_murd] = "murd"
    print("Your selected role is...") 
    select = "selecting"
    dot_spam(select)
    if player == "murd":
        print("🔪 murderer.\n")
    else:
        print("😨survivor.\n")
    time.sleep(2)

    return players


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
    time.sleep(2)
    return day

def wronginsert():
    print("Please answer with an acceptable input.\n")

def night(player_role, chosen):
    dead = False
    player_lh = ""
    if player_role == "surv":
        player_sleep = input("Will you sleep? (y/n)\n").lower()
        while player_sleep not in ['y', 'yes', 'n', 'no']:
            wronginsert()
            player_sleep = input("Will you sleep? (y/n)\n").lower()
        if player_sleep in ['y', 'yes']:
            player_sleep = True
            if chosen == 0:
                dead = True
        elif player_sleep in ['n', 'no']:
            player_sleep = False
        if player_sleep == False:
            while player_lh != "1" and player_lh != "2" and player_lh != "3":
                print("Will you take a peek outside or go into hiding? (Enter 1, 2 or 3)")
                print("1. (Take a peek outside)")
                print("2. (Hide in your house)")
                print("3. Nevermind. I'm feeling sleepy.")
                player_lh = input()
                if player_lh == "1":
                    player_lh = "look"
                    print("You decided to take a peak outside...")
                    #peak()
                elif player_lh == "2":
                    player_lh = "hide"
                    print("You decided to hide for the night.")
                    hide(chosen)
                elif player_lh == "3":
                    player_lh = "none"
                    player_sleep = True
                else:
                    wronginsert()
    return dead

#def peak():
    #obs_rate = randint(1,5)
    #if obs_rate == 1:



def hide(target):
    hidingrandom = randint(1,8)
    hideactions = ["You hid in a cardboard box, hoping not to be found...", "You hid in the wardrobe, trying to stay as silent as possible...", "You hid under your bed whilst attempting to control your heavy breathing...", "You hid underneath the bathroom cabinet, surely they won't expect this...", "You hid in the attic, staying as still as possible...", "You hid under the dining table...Surely they can't see you down there...right? RIGHT???", "You dug 3000 kilometers below the surface into the mantle to greet Satan and treated yourself with a nice Subway sandwich. Then, you went into the deep sea to greet your good old friend 'Angus the Deep Sea Anglerfish' and had a great time catching up. Then, you returned to your house and found a knife...but it was a toy knife. So, you decided to climb on the ceiling and hope for the best.", "You hid in the kitchen cabinet, holding your breath."]
    hidetext = "Hiding"
    tensiontexts = ["...nothing happened.", "...you heard nothing.", "...you stayed silent, but somehow, the world seemed even quieter", "...nothing was happening."]
    dot_spam(hidetext)
    print(f"{hideactions[hidingrandom]}")
    randomtension = randint(2,4)
    for i in range(randomtension):
        dot_spam(".")
        random.shuffle(tensiontexts)
        print(tensiontexts[0])
        time.sleep(1)
    dot_spam(".")
    if target == 0:
        print("...?")
        print("You heard what seemed like footsteps paddling around in your house.")
        print("After 5 minutes of tension, the footsteps faded away.")
    print("You felt safe.")


def dot_spam(text):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(text), end='\r')


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
    chosen = randint(0,6)
    if chosen == 0:
        chosen = playerchosenbias()
    while role_list[chosen] == 'murd':
        chosen = randint(0,6)
        if chosen == 0:
            chosen = playerchosenbias()
    print(chosen)
    return chosen
    
def compnames():
    finalcomp_names = []
    comp_names = ["Tim", "Gerald", "Jack", "Sammy", "Maria", "Jeremy", "Kaitlyn", "Andrew", "Tate", "Matthew", "Nick", "Eric", "Martin", "Hugo", "Harry", "Richard", "Michael", "Gabriel", "Josephine", "Joe", "Patrick", "Ronald", "Jerry", "Oliver", "Mark", "Elizabeth", "Billy", "Greg", "Violet", "Martha", "Jeffery", "Jerome", "Debbie", "Callum", "Grant", "Sarah", "Veronica", "Rachel", "Colin", "Josh", "Aaron", "Frank", "Cynthia", "Steven", "Jennifer", "Sophie", "Muhammed", "Emily", "Claire", "Kylie", "Joel", "Alicia", "Darrell"]
    random.shuffle(comp_names)
    for i in range(6):
        finalcomp_names.append(comp_names[0])
        comp_names.pop(0)
    return finalcomp_names

def murdwho(people):
    count = -1
    for player in people:
        if player != "murd":
            count += 1
        else:
            break
    return count

#compnames()
#player_lh = int(input())
player_name = intro()
player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role = roles()
comp1name, comp2name, comp3name, comp4name, comp5name, comp6name = compnames()
sus_points = 0
energy_points = randint(100,140)
energy_lv = energy(energy_points)
day_num = 0
day_num = day(day_num, sus_points, energy_lv)
#print(player_role)
if player_role == 'surv':
    chosen = aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role)
    murd = murdwho([player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role])
print(murd)
night(player_role, chosen)