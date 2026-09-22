# Meika Milton, 1st period Programming I, Crew Shares

import random

def udonta_quill(start_amt, person, amount):
    person = round((amount/100) * start_amt, 2)
    return person

yondu_share = 0
peter_share = 0
crew_shares = 0

while True:
    try:
        pirate_total = int(input("How many pirates are there?\nINCLUDING Yondu and Peter.\nAlso you have to name all of them.\n"))
    except:
        print("?? Weird crew size, huh?")
    else:
        if pirate_total <= 2:
            print("Sorry... yeah... there's more than that actually.")
        else:
            break

pirate_names = []

for pirate in range(1, (pirate_total - 1)):
    pirate_names.append(input(f"Whats the name of pirate # {pirate}?\n").strip().title())

initial_plunder = random.randint(500, 5000) # i did 5001 because i thought that the 2nd number isnt included and i wanted to include 5000 im sorry
plunder = initial_plunder

crew_shares = 3
yondu_share = 3
peter_share = 3
plunder -= crew_shares * pirate_total

yondu_share = udonta_quill(plunder, yondu_share, 13)
plunder -= yondu_share
peter_share = udonta_quill(plunder, peter_share, 11)
plunder -= peter_share

equal_share = round(plunder / pirate_total, 2)

yondu_share = round(equal_share + yondu_share, 2)
peter_share = round(equal_share + peter_share, 2)
crew_shares = round(equal_share + crew_shares, 2)


print(f"\nThe crew's total unit plunder was {initial_plunder}!\n")
print(f"Yondu has {yondu_share} units!\nPeter has {peter_share} units!")

for member in pirate_names:
    print(f"{member} has {crew_shares} units!")