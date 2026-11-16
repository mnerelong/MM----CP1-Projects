# MM, 1st period Programming I, Combat Program
import random as r

# -------

def player_attack(weapon, inventory, enemy_stats):
    return

def player_turn(stats, enemy_stats, inventory):
    while True:
        try:
            choice_action = int(input("It's your move. What will you do?\n[1] Attack\n[2] Item\n[3] Defend (Resilience +5 for this turn)\n[4] Flee.\nChoose:"))
        except:
            print("That's... not an option.")
        else:
            break

        if choice_action == 1:
            while True:
                try:
                    user_weapon = int(input("What weapon would you like to use?\n[1] Bare Claws: infinite uses.\n[2] Shotgun: Ammo at 6, can be refilled in Item.\n[3] Flimsy Knife: 50 uses.\n[4] I've changed my mind: ends turn, you don't have time for doubt.\n\nChoose:"))
                except:
                    print("That's... not an option.")
                else:
                    break
            
# -------

sawian_info = ["Expie", [10, 8, 7], "Milky", [8, 12, 6], "Dune", [11, 6, 9]]

inventory = ["Shotgun", 6, "Ammo", 16, "Flimsy knife", 50, "Bandages", 4, "Tourniquet", 1, "Blood Bag", 3]

thornback_info = [20, 16, 10]

while True:
    user_sawian = input('Choose your sawian:\n\n\t"Expie"\nHealth: 10, Resilience: 8, Strength: 7\n\n\t"Milky"\nHealth: 8, Resilience: 12, Strength: 6\n\n\t"Dune\n"Health: 11, Resilience: 6, Strength: 9\n\nChoose: ').capitalize()

    if user_sawian not in sawian_info:
        print("That's... not an option.")
        continue
    else:
        break

user_saw_info = sawian_info[sawian_info.index(user_sawian) + 1]

if r.randint(1, 5) % 2 == 0:
    turn = ["The monster ambushes you.", 0]
else:
    turn = ["Make the first move.", 1]

print("\nYou are being attacked by an Elder Thornback. Run for your life or chase it down.")
print(turn[0])