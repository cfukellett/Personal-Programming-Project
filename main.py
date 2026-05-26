from random import randint
import random
import time
import pygame
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

def intro():
    print("--Welcome--")
    time.sleep(1.2)
    yellow("Please enter your name:\n")
    name = input()
    yellow(f"Hello, {name}, welcome to the game.")
    time.sleep(1)
    red("Would you like to read the rules? (y/n):\n")
    read_rules = input().lower()
    while read_rules not in ['y', 'yes', 'n', 'no']:
        wronginsert()
        yellow("Would you like to read the rules? (y/n):\n")
        read_rules = input.lower()
    if read_rules in ['y', 'yes']:
        red("rules here")
    red("The game will now begin.")
    return name

def roles():
    players = ["surv", "surv", "surv", "surv", "surv", "surv", "surv"]
    player = randint(0,0)
    if player == 0:
        players[0] = "surv"
    else:
        players[0] = "murd"
    if players[0] == "surv":
        random_murd = randint(1, 6)
        players[random_murd] = "murd"
    print("Your selected role is...") 
    select = "selecting"
    dot_spam(select, True)
    player = players[0]
    if player == "murd":
        red("🔪 murderer.\n")
    else:
        blue("😨survivor.\n")
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

def botenergylv(name_list, murd, day, botenergylist):
    namelist2 = []
    namelist2= name_list.copy()
    print(namelist2)
    if day == 1:
        if murd != 0:
            namelist2.pop(murd)
        namelist2.pop(0)
        for name in namelist2:
            botenergylist.append(0)
    energyboost = 0
    person = 0
    print(namelist2)
    for name in range(len(namelist2)-1):
        energyboost = 0
        status = randint(1,5)
        if status == 1:
            energyboost += 20
        elif status == 2:
            energyboost += 30
        elif status == 3:
            energyboost += 40
        elif status == 4:
            energyboost -= 20
        elif status == 5:
            energyboost -= 30
        #if not rep:
        print(botenergylist)
        print(person)
        botenergylist[person] += energyboost
        #else:
        #    botenergylist.append(energyboost)
        person += 1
    print(botenergylist)
    print(namelist2)
    return botenergylist

def vote(name_list, suspts, energylv, murd):
    
    pass

def day(day, suspts, energylv, name_list, murd, player_role, chosen, player_name):
    print(name_list)
    #botenergys = botenergylv(name_list, murd, day, botenergylist)
    yellow(f"☀️--Day {day}--☀️")
    purple("It's the start of a brand new day.")
    purple(f"Here are your day {day} stats:")
    green(f"Your role: {player_role}")
    blue(f"🤔 Suspicion Points: {suspts}")
    yellow(f"⚡Energy Level: {energylv}")
    deadlist = ["was found with his eyes gouged out and his neck hanging on a branch… Terrifying! 😱", "had been impaled and had died from blood loss...", "was electrocuted, leaving their body completely unrecognisable...", "was having a midnight snack and suddenly suffered from a heart attack...Yes, this was caused by the murderer.", "somehow found an active volcano and jumped into it, burning themselves into ashes in the process.", "was found without skin in a toolshed."]
    rand_death = randint(0,(len(deadlist)-1))
    chosen-=1
    print(f"This is the value for rand_death", rand_death)
    if player_role == 'surv':
        if day == 1:
            green("There is no danger here. You can freely rest.")
        else:
            dot_spam("", True)
            time.sleep(0.2)
            red("Oh, what's this? A murder had occured overnight.")
            print(name_list)
            print(f"This is the chosen value", chosen)
            red(f"{name_list[chosen]} {deadlist[rand_death]}")
            name_list.pop(chosen)
            yellow('There is a murderer among you and the others. Vote to eliminate the murderer!\n')
            purple("Let's take a look at the others.")
            vote(name_list, suspts, energylv, murd)
            person = 0
            #for name in name_list:
            #    print(name, botenergylist[person-1])
            #    person += 1
            if len(name_list) < 2:
                dot_spam("The murderer has killed everyone except you.", False)
    print(name_list)
    #for name in name_list:
        


        
    time.sleep(2)
    return dead

def wronginsert():
    print("Please answer with an acceptable input.\n")

def night(player_role, chosen, murd, name_list, energy_pts):
    dead = False
    player_lh = ""
    if player_role == "surv":
        blue("Will you sleep? (y/n)\n")
        player_sleep = input().lower()
        while player_sleep not in ['y', 'yes', 'n', 'no']:
            wronginsert()
            blue("Will you sleep? (y/n)\n")
            player_sleep = input().lower()
        if player_sleep in ['y', 'yes']:
            player_sleep = True
            if chosen == 0:
                dead = True
        elif player_sleep in ['n', 'no']:
            player_sleep = False
        if player_sleep == False:
            while player_lh != "1" and player_lh != "2" and player_lh != "3":
                purple("Will you take a peek outside or go into hiding? (Enter 1, 2 or 3)")
                red("1. (Take a peek outside)")
                green("2. (Hide in your house)")
                blue("3. Nevermind. I'm feeling sleepy.")
                player_lh = input()
                if player_lh == "1":
                    player_lh = "look"
                    red("You decided to take a peek outside...")
                    dead = peek(murd, name_list)
                    break
                elif player_lh == "2":
                    player_lh = "hide"
                    blue("You decided to hide for the night.")
                    hide(chosen)
                    break
                elif player_lh == "3":
                    player_lh = "none"
                    player_sleep = True
                    break
                else:
                    wronginsert()
            if player_lh != "3":
                energy_pts -= 30
            else:
                energy_pts += 20
        else:
            energy_pts += 20
    return dead, energy_pts

def peek(murd, names):
    dead = False
    obs_rate = randint(1,4)
    murd_rate = randint(1,2)
    print(names)
    print(murd)
    if murd_rate != 3:
        chosen_one = names[murd]
    else:
        chosen_one = names[randint(0,3)]
    dot_spam("You peeked out the window", False)
    peektext = [f"...and saw {chosen_one} walking on the streets with their hands in their pockets...", f"...and saw {chosen_one} quietly sitting on a bench outside...", f"...and saw {chosen_one} breakdancing in an alleyway...?", f"...and saw {chosen_one} doing the Enma Palm Sign...", f"...and saw {chosen_one} floating in the air with a grin...Oh, you were hallucinating. {chosen_one} is really just standing there doing nothing.", f"...and saw {chosen_one} stretching out in the open..."]
    murdtext = [f"...and saw {chosen_one} holding a knife...", f"...and saw {chosen_one} with bloods splattered all over their hands...", f"...and saw {chosen_one} carrying a Hush Puppy..."]
    murdtextrate = randint(1,2)
    allpeektext = peektext
    if chosen_one == names[murd]:
        if murdtextrate == 1:
            allpeektext += murdtext
    allpeektextindex = len(allpeektext)-1
    if obs_rate != 1:
        if murdtextrate == 1:
            red(f"{allpeektext[allpeektextindex]}")
        else:
            purple(f"{allpeektext[allpeektextindex]}")
        spotted = randint(1,10)
        if spotted == 1:
            time.sleep(1)
            dot_spam(f"...Suddenly, {chosen_one} stopped...", False)
            time.sleep(1)
            red(f"Shivers go up your spine...{chosen_one} has found you.")
            time.sleep(1)
            red(f"You are now what people call 'dead'.")
            dead = True
    else:
        green("...and saw nothing.")
    return dead



def hide(target):
    hideactions = ["You hid in a cardboard box, hoping not to be found...", "You hid in the wardrobe, trying to stay as silent as possible...", "You hid under your bed whilst attempting to control your heavy breathing...", "You hid underneath the bathroom cabinet, surely they won't expect this...", "You hid in the attic, staying as still as possible...", "You hid under the dining table...Surely they can't see you down there...right? RIGHT???", "You dug 3000 kilometers below the surface into the mantle to greet Satan and treated yourself with a nice Subway sandwich. Then, you went into the deep sea to greet your good old friend 'Angus the Deep Sea Anglerfish' and had a great time catching up. Then, you returned to your house and found a knife...but it was a toy knife. So, you decided to climb on the ceiling and hope for the best.", "You hid in the kitchen cabinet, holding your breath."]
    hidingrandom = randint(1,len(hideactions))
    hidetext = "Hiding"
    tensiontexts = ["...nothing happened.", "...you heard nothing.", "...you stayed silent, but somehow, the world seemed even quieter", "...nothing was happening."]
    dot_spam(hidetext, True)
    purple(f"{hideactions[hidingrandom]}")
    randomtension = randint(2,4)
    for i in range(randomtension):
        dot_spam(".", True)
        random.shuffle(tensiontexts)
        print(tensiontexts[0])
        time.sleep(1)
    dot_spam(".", True)
    if target == 0:
        print("...?")
        purple("You heard what seemed like footsteps paddling around in your house.")
        purple("After 5 minutes of tension, the footsteps faded away.")
    green("You felt safe.")


def dot_spam(text, remove):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(text), end='\r')
    if not remove:
        print(text)


def playerchosenbias():
    print('Biased function is running. Gambling if player is chosen or not.')
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

def aicode(playerrole, c1role, c2role, c3role, c4role, c5role, c6role, namelist):
    role_list = [playerrole, c1role, c2role, c3role, c4role, c5role, c6role]
    chosen = randint(1,len(namelist))
    chosen -= 1
    print(f"This is the chosen value", chosen)
    if chosen == 0:
        chosen = playerchosenbias()
    while role_list[chosen] == 'murd':
        chosen = randint(1,len(namelist))
        chosen -= 1
        if chosen == 0:
            chosen = playerchosenbias()
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
        count += 1
        if player == "murd":
            break
    return count

def overview(daynum, name, role, energy_lv, sus_points, murd, dead, names):
    if dead == True:
        red("You have perished...This is quite tragic indeed.")
    yellow(f"{name}:")
    green(f"Your role was {role}.")
    yellow(f"Final Energy Level: {energy_lv}")
    blue(f"Final Suspicion Points: {sus_points}")
    if role == 'surv':
        dot_spam("You survived for", False)
        purple(f"{daynum} days.")
        dot_spam("The murderer was", False)
        red(f"{names[murd]}.")

def murdthing(player_role, role_list, namelist):
    if player_role == 'surv':
        chosen = aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role, namelist)
        murd = murdwho(role_list)
    else:
        murd = 0
    return murd, chosen

#compnames()
#player_lh = int(input())
player_name = intro()
player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role = roles()
comp1name, comp2name, comp3name, comp4name, comp5name, comp6name = compnames()
name_list = [player_name, comp1name, comp2name, comp3name, comp4name, comp5name, comp6name]
sus_points = 0
energy_points = randint(100,140)
day_num = 0
print(player_role)
role_list = [player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role]
murd, chosen = murdthing(player_role, role_list, name_list)
dead = False
print(name_list)
while dead == False:
    day_num += 1
    energy_lv = energy(energy_points)
    #if day_num == 1:
        #botenergylist = []
    dead = day(day_num, sus_points, energy_lv, name_list, murd, player_role, chosen, player_name)
    aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role, name_list)
    if dead == False:
        dead, energy_points = night(player_role, chosen, murd, name_list, energy_points)
    if dead == True:
        overview(day_num, player_name, player_role, energy_lv, sus_points, murd, dead, name_list)
    print(chosen)
    #if chosen == 0:
        #if dead == True:
          #  name_list.pop(chosen)
   # else:
        #name_list.pop(chosen)
    print(name_list)
