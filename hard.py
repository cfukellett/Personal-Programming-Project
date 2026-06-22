from random import randint
import random
import time
import pygame
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb
from playsound3 import playsound
import sys
import os
pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1)

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
    # red("Would you like to read the rules? (y/n):\n")
    # read_rules = input()
    # read_rules = read_rules.lower()
    # while read_rules not in ['y', 'yes', 'n', 'no']:
    #     wronginsert()
    #     red("Would you like to read the rules? (y/n):\n")
    #     read_rules = input()
    #     read_rules = read_rules.lower()
    # if read_rules in ['y', 'yes']:
    #     red("rules here")
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
    #print(namelist2)
    if day == 1:
        if murd != 0:
            namelist2.pop(murd)
        namelist2.pop(0)
        for name in namelist2:
            botenergylist.append(0)
    energyboost = 0
    person = 0
    #print(namelist2)
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
        #print(botenergylist)
        #print(person)
        botenergylist[person] += energyboost
        #else:
        #    botenergylist.append(energyboost)
        person += 1
    #print(botenergylist)
    #print(namelist2)
    return botenergylist

def vote(namelist, suspts, energylv, murd, playername, day, dayrandomvar, murdname):
    murddead = False
    #print(f"This is the murd value: {murd}")
    #print(f"This is the murderer's name: {namelist[murd]}")
    yellow('There is a murderer among you and the others.\n')
    time.sleep(2)
    #print(namelist)
    intenamelist = namelist
    intenamelist.pop(0)
    defoptions = ["Plead", "Argue", "Denial", "Confess", "Silence"]
    atkoptions = ["Object", "Argue", "Accuse", "Warn", "Silence"]
    random.shuffle(atkoptions)
    random.shuffle(defoptions)
    purple(f"You must interrogate every person.\nYou will be given three options.\nChoose the correct option for better odds of deducing who the murderer is.")
    if day <= 2:
        green("Input anything to begin the interrogation!")
        ReallyRandomInputThatWillNeverBeUsed = input()
        ReallyRandomInputThatWillNeverBeUsed = '1'
    else:
        green("1. Start Interrogation\n2. I'm getting bored of this interrogation slop. SKIP!!!\n")
        ReallyRandomInputThatWillNeverBeUsed = input()
        while ReallyRandomInputThatWillNeverBeUsed not in ['1', '2']:
            wronginsert()
            green("1. Start Interrogation\n2. I'm getting bored of this interrogation slop. SKIP!!!\n")
            ReallyRandomInputThatWillNeverBeUsed = input()
    if ReallyRandomInputThatWillNeverBeUsed == '1':
        for person in intenamelist:
            blue(f"{person} is being interrogated.")
            blue("Choose your interrogation option.")
            random.shuffle(atkoptions)
            blue(f"1. {atkoptions[0]}\n2. {atkoptions[1]}\n3. {atkoptions[2]}\n4. Skip")
            #the interrogated has these options: plead, argue, denial, confess, silence, reroll
            #the interrogater has these options: object, argue, accuse, warn, silence, skip, reroll
            #plead beats object, argue beats accuse, denial beats argue, confess beats warn, silence is a tie, reroll allows them to reroll their options
            #object beats argue, argue beats denial, accuse beats confess, warn beats silence, silence beats plead, reroll allows them to reroll their options
            #i have come from the future (2 weeks) i am here to say that the notes above are all false 
            atkchoice = input()
            atkchoice2 = ''
            while atkchoice not in ['1', '2', '3', '4']:
                wronginsert()
                blue("Choose your interrogation option.")
                blue(f"1. {atkoptions[0]}\n2. {atkoptions[1]}\n3. {atkoptions[2]}\n4. Skip")
                atkchoice = input()
            #if atkchoice == 5:
            #    atkchoice = intespec(atkoptions, atkchoice, 'reroll')
            if int(atkchoice) == 4:
                red("You chose to skip this interrogation...\n")
                atkchoice2 == "none"
            else:
                atkchoice2 = atkoptions[int(atkchoice)-1].lower()
            defbotchoice = defoptions[0]
            winlose = ''
            defbotchoice2 = defbotchoice.lower()
            if atkchoice2 == 'object':
                green(f"{playername}(you): Objection!")
                if defbotchoice2 == 'plead':
                    winlose = 'l'
                elif defbotchoice2 == 'argue':
                    winlose = 'w'
                elif defbotchoice2 == 'denial':
                    winlose = 'l'
                elif defbotchoice2 == 'confess':
                    winlose = 'l'
                elif defbotchoice2 == 'silence':
                    winlose = 'w'
            elif atkchoice2 == 'argue':
                green(f"{playername}(you): Redditors, lend me your power!")
                if defbotchoice2 == 'plead':
                    winlose = 'w'
                elif defbotchoice2 == 'argue':
                    winlose = 'l'
                elif defbotchoice2 == 'denial':
                    winlose = 'l'
                elif defbotchoice2 == 'confess':
                    winlose = 'w'
                elif defbotchoice2 == 'silence':
                    winlose = 'l'
            elif atkchoice2 == 'accuse':
                green(f"{playername}(you): I call cap.")
                if defbotchoice2 == 'plead':
                    winlose = 'l'
                elif defbotchoice2 == 'argue':
                    winlose = 'l'
                elif defbotchoice2 == 'denial':
                    winlose = 'l'
                elif defbotchoice2 == 'confess':
                    winlose = 'w'
                elif defbotchoice2 == 'silence':
                    winlose = 'w'
            elif atkchoice2 == 'warn':
                green(f"{playername} (you): Don't do that again...")
                if defbotchoice2 == 'plead':
                    winlose = 'l'
                elif defbotchoice2 == 'argue':
                    winlose = 'l'
                elif defbotchoice2 == 'denial':
                    winlose = 'l'
                elif defbotchoice2 == 'confess':
                    winlose = 'w'
                elif defbotchoice2 == 'silence':
                    winlose = 'w'
            elif atkchoice2 == 'silence':
                green(f"{playername} (you): ...")
                if defbotchoice2 == 'plead':
                    winlose = 'w'
                elif defbotchoice2 == 'argue':
                    winlose = 'l'
                elif defbotchoice2 == 'denial':
                    winlose = 'l'
                elif defbotchoice2 == 'confess':
                    winlose = 'w'
                elif defbotchoice2 == 'silence':
                    winlose = 'l'
            if atkchoice != '4':
                green(f"You chose: {atkchoice2}")
                red(f"{person} chose: {defbotchoice2}")
                if winlose == 'w':
                    red(f"{person}: Oh no.")
                    playsound("ohno.mp3")
                    green("You won the interrogation!")
                    if namelist[murd-1] == person:
                        red(f"{person} is quite suspicious...\n")
                elif winlose == 'l':
                    red(f"{person}: Are you sure?")
                    playsound("areyousure.mp3")
                    blue("You lost the interrogation...\n")
                elif winlose == 't':
                    green(f"{playername}(you): ...")
                    red(f"{person}: ...")
                    playsound("crow.mp3")
                    blue("You...both lost the interrogation?\n")
            time.sleep(1.5)
    red("It is now your turn to be interrogated.")
    time.sleep(2)
    red("Choose the correct option to clear their suspicion towards you!\n")
    time.sleep(2)
    random.shuffle(atkoptions)
    random.shuffle(defoptions)
    blue(f"1. {defoptions[0]}\n2. {defoptions[1]}\n3. {defoptions[2]}")
    defchoice = input()
    while defchoice not in ['1', '2', '3']:
        wronginsert()
        blue("Choose your interrogation option.")
        blue(f"1. {defoptions[0]}\n2. {defoptions[1]}\n3. {defoptions[2]}\n")
        defchoice = input()
    atkbotchoice = atkoptions[0]
    winlose = ''
    defchoice2 = defoptions[int(defchoice)-1].lower()
    atkbotchoice = atkbotchoice.lower()
    if defchoice2 == 'plead':
        green(f"{playername}(you): S-sir, please!!")
        if atkbotchoice == 'object':
            winlose = 'l'
        elif atkbotchoice == 'argue':
            winlose = 'w'
        elif atkbotchoice == 'accuse':
            winlose = 'l'
        elif atkbotchoice == 'warn':
            winlose = 'l'
        elif atkbotchoice == 'silence':
            winlose = 'w'
    elif defchoice2 == 'argue':
        green(f"{playername}(you): Redditors, lend me your power!")
        if atkbotchoice == 'object':
            winlose = 'w'
        elif atkbotchoice == 'argue':
            winlose = 't'
        elif atkbotchoice == 'accuse':
            winlose = 'l'
        elif atkbotchoice == 'warn':
            winlose = 'l'
        elif atkbotchoice == 'silence':
            winlose = 'w'
    elif defchoice2 == 'denial':
        green(f"{playername}(you): I didn't do it bro!! trust")
        if atkbotchoice == 'object':
            winlose = 'w'
        elif atkbotchoice == 'argue':
            winlose = 'l'
        elif atkbotchoice == 'accuse':
            winlose = 'l'
        elif atkbotchoice == 'warn':
            winlose = 'w'
        elif atkbotchoice == 'silence':
            winlose = 't'
    elif defchoice2 == 'confess':
        green(f"{playername}(you): Yeah. I did that.")
        if atkbotchoice == 'object':
            winlose = 't'
        elif atkbotchoice == 'argue':
            winlose = 'w'
        elif atkbotchoice == 'accuse':
            winlose = 'l'
        elif atkbotchoice == 'warn':
            winlose = 'w'
        elif atkbotchoice == 'silence':
            winlose = 'l'
    elif defchoice2 == 'silence':
        green(f"{playername}(you): ...")
        if atkbotchoice == 'object':
            winlose = 'w'
        elif atkbotchoice == 'argue':
            winlose = 'l'
        elif atkbotchoice == 'accuse':
            winlose = 'l'
        elif atkbotchoice == 'warn':
            winlose = 'w'
        elif atkbotchoice == 'silence':
            winlose = 't'
    green(f"You chose: {defchoice2}")
    person = namelist[randint(1,len(namelist)-1)]
    red(f"{person} chose: {atkbotchoice}")
    if winlose == 'w':
        green(f"{playername}(you): I'm outta here!")
        playsound("byebye.mp3")
        yellow("You went through with the interrogation without seeming suspicious!\n")
        suspts -= 20
    elif winlose == 'l':
        red(f"{person}: Are you sure?")
        playsound("areyousure.mp3")
        blue("You lost the interrogation...\n")
        red("Everyone is now more suspicious of you.\n")
        suspts += 50
    elif winlose == 't':
        green(f"{playername}(you): ...")
        red(f"{person}: ...")
        playsound("crow.mp3")
        blue("You...both lost the interrogation?\n")

    time.sleep(2)
    purple("It's time to vote.\nIf you think someone is suspicious, vote them out!\nAlternatively, you can also skip your vote.\n")
    nameindex = 1
    for name in namelist:
        if playername != namelist[0]:
            blue(f"{nameindex}. {name}")
            nameindex += 1
    blue(f"{nameindex}. Skip")
    playervote = input(f"Type in the number of the person who you would like to vote out,\nor type '{nameindex}' to skip your vote.\n")
    while 1 > int(playervote) or int(playervote) > nameindex or playervote.isalpha():
        wronginsert()
        playervote = input(f"Type in the number of the person who you would like to vote out,\nor type '{nameindex}' to skip your vote.\n")
    if playervote == str(nameindex):
        red("You skipped your vote...")
    else:
        purple(f"You voted for {namelist[int(playervote)-1]}.")
    if suspts >= 200:
        playervotedchance = 1
    elif suspts >= 150:
        playervotedchance = randint(1,3)
    elif suspts >= 100:
        playervotedchance = randint(1,7)
    elif suspts >= 50:
        playervotedchance = randint(1,12)
    elif suspts >= 25:
        playervotedchance = randint(1,30)
    else:
        playervotedchance = 0
    if playervotedchance == 1:
        playergetsvoted = True
    else:
        playergetsvoted = False

    botplayervote = 1
    botselfvote = 0
    if playergetsvoted == True:
        red(f"The majority decided to vote for you...")
        dead = True
        return dead
    else:
        for name in namelist:
            if day > 5:
                dayrandomvar = 25
            else:
                dayrandomvar = 100-(15*day)
            votewithplayer = randint(1,dayrandomvar)
            if votewithplayer <= 20:
                if name != murdname:
                    votewithplayer = True
                else:
                    votewithplayer = False
            else:
                votewithplayer = False
            if votewithplayer == True:
                if int(playervote) == nameindex:
                    blue(f"{name} trusts your vote and has skipped their vote.")
                    botplayervote += 1
                else:
                    blue(f"{name} trusts your vote and has voted for {namelist[int(playervote)-1]}.")
                    botplayervote += 1
            else:
                blue(f"{name} has kept their vote hidden from you...")
                botselfvote += 1
            time.sleep(1.5)
    
        if botselfvote > botplayervote:
            largestvote = 'bot'
        elif botselfvote < botplayervote:
            largestvote = 'player'
        else:
            largestvote = 'tie'
        skiportie = ''
        if largestvote == 'bot':
            chosenvoted = randint(1,len(namelist)-1)
            #print("largest vote is bot")
        elif largestvote == 'player':
            #print("largest vote is player")
            if playervote != '5':
                chosenvoted = int(playervote)-1
            else:
                chosenvoted = 'skip'
                skiportie = 'skip'
        elif largestvote == 'tie':
            chosenvoted = 'skip'
            skiportie = 'tie'
        blue(f"The majority of the votes are in...")
        time.sleep(2)
        #print(chosenvoted)
        if chosenvoted != 'skip':
            chosenvotedname = namelist[chosenvoted]
            yellow(f"{chosenvotedname} received the most votes...")
            #print(f"This is the murd value: {murd}")
            time.sleep(1.5)
            red(f"{chosenvotedname} has been eliminated.")
            #(murdname)
            if chosenvotedname == murdname:
                #print("Murd has been eliminated!")
                murddead = True
            namelist = namelist.pop(chosenvoted)
        elif chosenvoted == 'skip':
            if skiportie == 'tie':
                yellow(f"There was a tie in the votes!\nThe votes will be skipped.")
            else:
                yellow("The majority agreed to skip the vote.")
    return murddead

def intespec(atkoptions, atkchoice, status):
    if status == 'reroll':
        rerolls = 3
        while atkchoice == 5:
            if rerolls > 0:
                rerolls -= 1
                purple("You have chosen to reroll.")
                red(f"Rerolls remaining: {rerolls}")
                random.shuffle(atkoptions)
                blue(f"1. {atkoptions[0]}\n2. {atkoptions[1]}\n3. {atkoptions[2]}\n4. Skip\n 5. Reroll")
                while 1 < atkchoice < 5:
                    wronginsert()
                    blue("Choose your interrogation option.")
                    blue(f"1. {atkoptions[0]}\n2. {atkoptions[1]}\n3. {atkoptions[2]}\n4. Skip\n 5. Reroll")
                    atkchoice = input().lower()
    return atkchoice

def day(day, suspts, energylv, name_list, murd, player_role, chosen, player_name, dayrandomvar, murddead, murdname):
    #print(name_list)
    #botenergys = botenergylv(name_list, murd, day, botenergylist)
    yellow(f"☀️--Day {day}--☀️")
    purple("It's the start of a brand new day.")
    purple(f"Here are your day {day} stats:")
    if player_role == 'surv':
        blue(f"Your role: 😨survivor")
    else:
        red(f"Your role: 🔪 murderer")
    blue(f"🤔 Suspicion Points: {suspts}")
    yellow(f"⚡Energy Level: {energylv}")
    deadlist = ["was found with his eyes gouged out and his neck hanging on a branch… Terrifying! 😱", "had been impaled and had died from blood loss...", "was electrocuted, leaving their body completely unrecognisable...", "was having a midnight snack and suddenly suffered from a heart attack...Yes, this was caused by the murderer.", "somehow found an active volcano and jumped into it, burning themselves into ashes in the process.", "was found without skin in a toolshed."]
    rand_death = randint(0,(len(deadlist)-1))
    if dayrandomvar > 10:
        dayrandomvar -= 10
    #print(f"This is the value for rand_death", rand_death)
    if player_role == 'surv':
        if day == 1:
            green("There is no danger here. You can freely rest.")
        else:
            dot_spam("", True)
            time.sleep(0.2)
            if murddead == False:
                if len(name_list) > 3:
                    red("Oh, what's this? A murder had occurred overnight.")
                    time.sleep(2)
                    #print(name_list)
                    #print(f"This is the murd value before the chosen value has been assigned: {murd}")
                    #print(f"This is the chosen value", chosen)
                    if chosen > (len(name_list)-1):
                        chosen -= 1
                    if chosen == murd:
                        chosen -= 1
                    if chosen == 0:
                        #print(f"Chosen value was 0, now changing")
                        chosen = randint(1,len(name_list)-1)
                        #print(f"This is the new chosen value", chosen)
                    red(f"{name_list[chosen]} {deadlist[rand_death]}")
                    time.sleep(2)
                    name_list.pop(chosen)
                    if murd > (len(name_list)-1):
                        murd -= 1
                    #print(f"This is the murd value: {murd}")
                    murddead = vote(name_list, suspts, energylv, murd, player_name, day, dayrandomvar, murdname)
                    person = 0
                    #for name in name_list:
                    #    print(name, botenergylist[person-1])
                    #    person += 1
                else: 
                    print("(normally there would be a special gamemode between the last survivor and the killer here)")
                    print("(pretend you won i guess!!)")
                    lms(energylv, murdname, player_name)
                    sys.exit()
            else:
                yellow("No murder had occurred overnight.")
                dot_spam("which means", False)
                green(f"The murderer has been eliminated! Hooray!\n(end of game)")
                pygame.mixer.music.stop()
                pygame.mixer.music.load("win.mp3")
                pygame.mixer.music.play(-1)
                playsound("cheer.mp3")
                sys.exit()
                
            
    if player_name != name_list[0]:
        name_list.insert(0,player_name)
    #print(name_list)
    #for name in name_list:
    time.sleep(2)
    return dead, murddead, murd

def lms(energylv, murdname, playername):
    purple(f"LAST SURVIVOR STANDING:\n{playername} VS {murdname}")
    purple("To survive, you must participate in a brutal fight to the death against the murderer...")
    yellow("Would you like to read the rules for this special gamemode? (y/n)\n")
    readrules = input()
    readrules = readrules.lower()
    while readrules not in ['y', 'yes', 'n', 'no']:
        wronginsert()
        red("Would you like to read the rules? (y/n):\n")
        readrules = input()
        readrules = readrules.lower()
    if readrules in ['y', 'yes']:
        yellow("Your initial HP will be determined on your energy level.\nThe more your energy level, the higher your initial HP will be.")
        yellow("The survivor starts off without a weapon, while the murderer starts off with a knife.")
        yellow("If you do not have a weapon, you are able to choose 1 out of 4 options.")
        yellow("1. Punch (deals 15 HP on successful hit)\n2. Block (heals 10 HP on successful hit)\n3. Kick (deals 5 HP and heals 5 HP on successful hit)\n4.Steal (steals the opposing's knife)")
        yellow("If you have a weapon, you are able to choose 1 out of 4 options.")
        yellow("1. Stab (deals 25 HP on successful hit)\n2. Block (heals 10 HP on successful hit)\n3. Kick (deals 5 HP and heals 5 HP on successful hit)\n4. Throw (deals 35 HP on successful hit)")
        yellow("Punch/Stab beats Kick\nBlock beats Punch/Stab\nKick beats Block")
        yellow("Steal beats Stab/Punch and Throw but loses to everything else")
        yellow("Throw beats everything except Steal and has a 50/50 chance to miss (lose)")
        purple("This is all very straightforward and definitely not confusing in anyway, right?\nGood!")
    atkoptions = ["Punch", "Block", "Kick"]

    pass

def wronginsert():
    print("Please answer with an acceptable input.\n")

def night(player_role, chosen, murd, name_list, energypts, murddead):
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
                    energypts -= 30
                    dead = peek(murd, name_list, murddead)
                    break
                elif player_lh == "2":
                    player_lh = "hide"
                    blue("You decided to hide for the night.")
                    hide(chosen)
                    energypts -= 30
                    break
                elif player_lh == "3":
                    player_lh = "none"
                    player_sleep = True
                    energypts+=20
                    break
                else:
                    wronginsert()
    return dead, energypts

def peek(murd, names, murddead):
    dead = False
    obs_rate = randint(1,4)
    murd_rate = randint(1,3)
    #print(names)
    #print(murd)
    if murd_rate == 3 and murddead == False:
        chosen_one = names[murd]
    else:
        chosen_one = names[randint(0,3)]
    dot_spam("You peeked out the window", False)
    peektext = [f"...and saw {chosen_one} walking on the streets with their hands in their pockets...", f"...and saw {chosen_one} quietly sitting on a bench outside...", f"...and saw {chosen_one} breakdancing in an alleyway...?", f"...and saw {chosen_one} doing the Enma Palm Sign...", f"...and saw {chosen_one} floating in the air with a grin...Oh, you were hallucinating. {chosen_one} is really just standing there doing nothing.", f"...and saw {chosen_one} stretching out in the open..."]
    murdtext = [f"...and saw {chosen_one} holding a knife...", f"...and saw {chosen_one} with bloods splattered all over their hands...", f"...and saw {chosen_one} carrying a Hush Puppy..."]
    murdtextrate = randint(1,2)
    allpeektext = peektext
    if chosen_one == names[murd] and murddead == False:
        if murdtextrate == 1:
            allpeektext += murdtext
    allpeektextindex = len(allpeektext)-1
    if obs_rate != 1:
        if murdtextrate == 1 and murddead == False:
            red(f"{allpeektext[allpeektextindex]}")
        else:
            purple(f"{allpeektext[allpeektextindex]}")
        spotted = randint(1,10)
        if spotted == 1 and murddead == False:
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
    hidingrandom = randint(1,len(hideactions)-1)
    hidetext = "Hiding"
    tensiontexts = ["...nothing happened.", "...you heard nothing.", "...you stayed silent, but somehow, the world seemed even quieter.", "...nothing was happening."]
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
    time.sleep(1.5)

def dot_spam(text, remove):
    for i in range(5):
        text += "."
        print(text, end='\r')
        time.sleep(0.3)
    time.sleep(1)
    print(" " * len(text), end='\r')
    if not remove:
        print(text)


def playerchosenbias(namelist, murd):
    #print('playerchosenbias function is running. gambling time!')
    chosen = randint(1,5)
    chosen2 = ""
    if chosen == 1:
        chosen2 = "unbias"
    else:
        chosen2 = "bias"
    if chosen2 == "bias":
        while chosen == namelist[murd]:
            chosen = randint(1,len(namelist)-1)
    else:
        chosen = 0
    return chosen

def aicode(playerrole, c1role, c2role, c3role, c4role, c5role, c6role, namelist, day, murd):
    role_list = [playerrole, c1role, c2role, c3role, c4role, c5role, c6role]
    if day == 1:
        chosen = randint(1,len(namelist)-1)
    else:
        chosen = randint(0,len(namelist)-1)
    #print(f"This is the chosen value from aicode", chosen)
    if chosen == 0:
        chosen = playerchosenbias(namelist, murd)
    while role_list[chosen] == 'murd':
        chosen = randint(0,len(namelist)-1)
        if chosen == 0:
            chosen = playerchosenbias(namelist, murd)
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
        if daynum == 1:
            purple(f"...1 day?\nWow. You must be really bad at this game.")
        else:
            purple(f"{daynum} days.")
        dot_spam("The murderer was", False)
        red(f"{names[murd]}.")

def murdthing(player_role, role_list, namelist, daynum, murd):
    if player_role == 'surv':
        chosen = aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role, namelist, daynum, murd)
        murd = murdwho(role_list)
    else:
        murd = 0
    return murd, chosen

#compnames()
#player_lh = int(input())
os.system('cls' if os.name == 'nt' else 'clear')
print("\n")
player_name = intro()
player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role = roles()
comp1name, comp2name, comp3name, comp4name, comp5name, comp6name = compnames()
name_list = [player_name, comp1name, comp2name, comp3name, comp4name, comp5name, comp6name]
sus_points = 0
energy_points = randint(100,140)
day_num = 0
#print(player_role)
role_list = [player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role]
murd = 0
murd, chosen = murdthing(player_role, role_list, name_list, day_num, murd)
dead = False
#print(name_list)
murdname = name_list[murd]
#print(f"Murd name before game starts: {murdname}")
dayrandomvar = 100
murddead = False
while dead == False:
    if murddead == False:
        murd = name_list.index(murdname)
    day_num += 1
    energy_lv = energy(energy_points)
    #if day_num == 1:
        #botenergylist = []
    dead, murddead, murd = day(day_num, sus_points, energy_lv, name_list, murd, player_role, chosen, player_name, dayrandomvar, murddead, murdname)
    if murddead == False:
        aicode(player_role, comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role, name_list, day_num, murd)
    if dead == False:
        dead, energy_points = night(player_role, chosen, murd, name_list, energy_points, murddead)
    if dead == True:
        overview(day_num, player_name, player_role, energy_lv, sus_points, murd, dead, name_list)
    #print(chosen)
    #if chosen == 0:
        #if dead == True:
          #  name_list.pop(chosen)
   # else:
        #name_list.pop(chosen)
    if player_name != name_list[0]:
        name_list.insert(0,player_name)
    #print(name_list)
