from random import randint
peektext = [f"...and saw here walking on the streets with their hands in their pockets...", "and test"]
peektext2 = ["...and saw here"]
peektext3 = peektext
peektext3 += peektext2
print(peektext3)
allpeektextindex = len(peektext3)-1
test = randint(1, allpeektextindex)
print(f"{peektext3[test]}")