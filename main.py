from random import randint
import time

def intro():
    print("--Welcome--")
    time.sleep(1.2)
    player_name = input("Please enter your name:\n")
    print(f"Hello, {player_name}, welcome to the game.")
    time.sleep(1)
    read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    while read_rules not in ['y', 'yes', 'n', 'no']:
        print("Sorry. I did not quite catch that.")
        read_rules = input("Would you like to read the rules? (y/n):\n").lower()
    if read_rules in ['y', 'yes']:
        print("rules here")
    print("The game will now begin.")
    roles()

def roles():
    comp1_role = ""
    comp2_role = ""
    comp3_role = ""
    comp4_role = ""
    comp5_role = ""
    comp6_role = ""
    comps = [comp1_role, comp2_role, comp3_role, comp4_role, comp5_role, comp6_role]
    player_role = randint(0,1)
    if player_role == 0:
        player_role = "surv"
    else:
        player_role = "murd"
    if player_role == "murd":
        comp1_role = "surv"
        comp2_role = "surv"
        comp3_role = "surv"
        comp4_role = "surv"
        comp5_role = "surv"
        comp6_role = "surv"
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
    if player_role == "murd":
        print("🔪 murderer.")
    else:
        print("😨survivor.")

intro()
