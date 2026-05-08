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