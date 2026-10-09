# Meika Milton, 1st period Programming I, While Loops Notes

import random
import time

vulture = random.randint(1, 11)
bird = 1
# While loops run until a boolean is not true?
while vulture != bird:
    print("bird...")
    time.sleep(0.1)
    bird += 1

print("VULTURE!!")

# ------------------------- ANATOMY OF A LOOP - - - - -

sales = random.randint(1,10)
profits = 1 # <- start point
# ^iterator :)  v- tells us the end statement. When it becomes FALSE then the loop finished.
while sales != profits:
    print(f"iterator... {profits}")
    time.sleep(0.05)
    profits += 1 # incrimentor. USED TO CHANGE YOUR ITERATOR!!! LIKE FIVE PEBBLES!! LIKE FIVE PEBBLES!! LIKE FIVE PEBBLES!!!
#           an iterator is what keeps track of the current iteration
#      *an iteration is one instance of a loop.
print("UNSIGNIFICANT FIIIVEEE TO THE RED STRAWWWW!!!")

# ------------------------- - - - - -

iterator = 14

while iterator >= 7:
    print(f"{iterator} red suns")
    time.sleep(0.2)
    iterator -= 1

# ------------------------ GUESSING GAME?? - - - - - -

pearls = random.randint(1, 50)
print("If you can properly guess how many pearls I currently own, then I'll give you this here electric spear for FREE!")

end = random.randint(1, 4)

while True:
    while True:
        try:
            guess = int(input("How many pearls do I have? Between 1 and 50?\n"))
        except:
            print("That... that isn't a number?")
        else:
            if guess < 0 or guess > 50:
                print("Did you even listen to me..?")
                continue # starts the next iteration
            else:
                break # EXITS the loop
    if guess == pearls:
        if end == 1:
            print("GAHH! You win this time...\nor.. NOT!! *throws the spear at you and kills you*")
            break
        elif end == 2:
            print(f"rrraaAAAAAAAGHHh!! You win! Fine! You win!\n*Throws all {pearls} pearls at you for some reason*")
            break
        elif end == 3:
            print("Good Job! Here's your spear.\n*Kindly hands you an electric spear*")
            break
        else:
            print("*spontaneously throws bomb at you*\nYOU WIN!!")
            break
    elif guess < pearls:
        print("I have more than that. Who do you think I am? A scavenger with AVERAGE wealth?")
    elif guess > pearls:
        print("WHOA whoa... Ain't nobody got THAT many pearls.")
    else:
        print("???")


# ------------------------ SCARY  - - - - - -

vulture = 20
bird = 1
# While loops run until a boolean is not true?
while vulture != bird:
    print("bird...")
    time.sleep(0.1)
    bird += 1
    if bird == 10:
        print("WA WA game over.")
        break # <- CAUSES THE ELSE TO NOT HAPPEN
else: # HAPPENS WHEN THE LOOP *NATURALLY* ENDS
    print("VULTURE!!")
# ^ no the else is not part of the if, its part of the while loop.