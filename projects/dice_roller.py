# Meika Milton, 1st period Programming I, Dice Roller
import random

def roll(list):
    total = 0
    for max in list:
        local_result = random.randint(1, max)
        total += local_result
        print(f"The D{max} rolled {local_result}.")
    return total

pick_dice = ["D4", "D6", "D8", "D10", "D12", "D20", "D100"] # meet potential dice
chosen_dice = []

print("Hey kiddo. Want some money? Too bad! I only have die!\nDie as in dice... Here's my stock.")
for die in pick_dice:
    print(die)
print("Pick.")

while True:
    user_dice = input().upper()
    if user_dice in pick_dice:
        chosen_dice.append(user_dice)
        print(f"Your dice: {chosen_dice}")
        loop = input("Great! Do you want another one? You should have another one. (yes/no)\n").lower()
        if loop == "yes": # are nested conditionals okay?
            print("What die do you want?")
        else:
            break
    else:
        print("???? I don't have that one?? Try again.")
print("Ready?")

roll_max = [] # highest number the dice can roll total.
results = 0 # the result
results_per = 0 # the result per dice
loop = "bluh" # if the code should loop
loop_num = 0 # how many loops the user has gone through

for die in chosen_dice:
    remove = die.split("D") # remove the D to get just the number.
    remove = "".join(remove)
    remove = int(remove)
    roll_max.append(remove)

while True: #  okay.... are nested loops alright?
    loop = input(f"You've rolled {loop_num} times. Roll? (yes/no)\n").lower()
    if loop == "yes":
        print("\n") # skips
        results = roll(roll_max)
        print(f"Your total is {results}!!")
        loop_num += 1
    elif loop != "yes" and loop_num == 0:
        print("You haven't even rolled? Are you sure?\n(You have no other choice)")
    else:
        print(f"Thanks for using my dice. You're going to have to pay for that.\nIt's gonna cost you about ${results}.")
        break