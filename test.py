#hellohellohellohellohelloHiHiHihelloHi







from random import randint

name_list = ["Tom", "James", "Bob"]
murd = 0
botenergylist = []
if murd != 0:
    name_list = name_list.pop(murd)
    print("done")
name_list = name_list.pop(0)
person = 0
energyboost = 0
for name in name_list:
    energyboost = 0
    status = randint(1,1)
    if status == 1:
        energyboost += 5
        botenergylist.append(energyboost)
print(botenergylist)
            

thislist = ["John", "Sam", "Some guy"]
thislist.pop(0)
print(thislist)




deadlist = {"was found with his eyes gouged out and his neck hanging on a branch… Terrifying! 😱", "had been impaled and had died from blood loss...", "was electrocuted, leaving their body completely unrecognisable...", "was having a midnight snack and suddenly suffered from a heart attack...Yes, this was caused by the murderer.", "somehow found an active volcano and jumped into it, burning themselves into ashes in the process.", "was found without skin in a toolshed."}
rand_death = randint(1,len(deadlist))
print(rand_death)



peektext = [f"...and found", "...and test"]
peektext2 = ["...and saw here"]
peektext3 = peektext
peektext3 += peektext2
print(peektext3)
allpeektextindex = len(peektext3)-1
test = randint(1, allpeektextindex)
print(f"{peektext3[test]}")