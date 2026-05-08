#hellohellohellohellohelloHiHiHihelloHi







from random import randint

name_list = ["Tom", "James", "Bob"]
murd = 0
botenergylist = []
print(name_list[0])
if murd != 0:
    name_list = name_list.pop(murd)
    print("done")
name_list.pop(0)
print(name_list)
rep = 0
for i in range (3):
    energyboost = 0
    person = 0
    for name in name_list:
        energyboost = 0
        status = randint(1,1)
        if status == 1:
            energyboost += 5
            if rep != 0:
                botenergylist[person] += energyboost
            else:
                botenergylist.append(energyboost)
        person += 1
    rep += 1
    print(botenergylist)