# MM, 1st period Programming I, Nesting Notes

import time as t

# ---- CONDITIONALS ---- #

green_bag = False
eyebrow_r = green_bag

if not green_bag:
    if not eyebrow_r:
        print("I can see a cat, I can see a hat, I can see a man with a baseball bat!")
    else:
        print("Green is not a creative color!")
else:
    print("Theres fish everywhere... fish everywhere.")

# ---- ------- ---- #
"""Break a move!"""
# ---- WHILE LOOPS ---- #
alive = True
dying = 1
breathing = 10
pain = 0

expie = [alive, dying, breathing, pain]

while expie[0]:
    while expie[1]:
        t.sleep(0.3)
        breathing -= 1
        print(breathing)
        if not breathing:
            alive = False
            break
    else:
        print("I love humour!")
        break
    break

print()
while True:
    for i in range(6):
        print(f"{i} pebbles")
    again = input("Did you get that?\n")
    if again.lower() == "n":
        print()
        pass
    else:
        break

# ---- ------- ---- #
"""Steak a move!"""
# ---- FOR LOOPS ---- #

