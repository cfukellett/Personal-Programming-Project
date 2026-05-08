#hellohellohellohellohelloHiHiHihelloHi







from random import randint

name_list = ["Tom", "James", "Bob"]
murd = 0
botenergylist = []
if murd != 0:
    name_list = name_list.pop(murd)
    print("done")
name_list.pop(0)
print(name_list)
for i in range (3):
    person = 0
    energyboost = 0
    for name in name_list:
        person += 1
        energyboost = 0
        status = randint(1,1)
        if status == 1:
            energyboost += 5
            print(botenergylist)
            if len(botenergylist) != 0:
                botenergylist[person-1] += energyboost
            else:
                botenergylist.append(energyboost)
    print(botenergylist)