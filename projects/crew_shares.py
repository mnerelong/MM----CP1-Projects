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
        pirate_total = int(input("How many pirates are there (including Yondu and Peter)?"))
    except:
        print("?? Weird crew size, huh?")
    else:
        if pirate_total <= 2:
            print("Sorry... yeah... there's more than that actually.")
        else:
            break

full_print = 0 # 0 for false.

if pirate_total <= 25:
    pirate_names = []
    full_print = 1 # 1 for true.

    for pirate in range(1, (pirate_total - 1)): # only -1 because it's already not including the last number
        pirate_names.append(input(f"Whats the name of pirate # {pirate}?\n").strip().title())

initial_plunder = random.randint(500, 5000) # i did 5001 because i thought that the 2nd number wasnt included and i wanted to include 5000 im sorry
plunder = initial_plunder

crew_shares = 3
yondu_share = 3
peter_share = 3
plunder -= crew_shares * pirate_total

yondu_share = udonta_quill(plunder, yondu_share, 13)
plunder = round(plunder - yondu_share, 2)
peter_share = udonta_quill(plunder, peter_share, 11)
plunder = round(plunder - peter_share, 2)

equal_share = round(plunder / pirate_total, 2)

yondu_share = round(equal_share + yondu_share, 2)
peter_share = round(equal_share + peter_share, 2)
crew_shares = round(equal_share, 2)


print(f"\nThe crew's total unit plunder was {initial_plunder}!\n")
print(f"Yondu has {yondu_share} units!\nPeter has {peter_share} units!")

if full_print == 1:
    for member in pirate_names:
        print(f"{member} has {crew_shares} units!")
else:
    print(f"The rest of the crew has {crew_shares} units!")