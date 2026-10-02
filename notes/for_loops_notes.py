# Meika Milton, 1st period Programming I, For Loops

import time # LIBRARY!

# ------- FOR ------- LOOPS -------

iterators = ["Five Pebbles", "Looks to the Moon", "No Significant Harassment", "Seven Red Suns", "Unparalleled Innocence", "Sliver of Straw", "Gray Winds"]
#     v- iterator variable (literally)
for iterator in iterators: # usually use just i or x or singular version of whatever you named your list
    print(f"{iterator} has ascended.")

waluigis_plus = {"Mirai", "Leo", "Cohen", "Elijah", "Isaac C.", "Santi", "Isaac B.", "Dirk"} # set is unordered and will print randomly
#v- keyword "for"
for waluigi in waluigis_plus: # <- waluigi only exists in the for loop and cannot be used outside of it
    print(f"{waluigi} is cool...")


pebbles = (1, 5, 6, 7, 18, 17)
avg = 0
for pebble in pebbles:
    avg += pebble
    print(f"{pebble} was added to the avg, which is now {avg}.")
avg /= len(pebbles) #                                                v- curious to know what that means? rounds it, I know.
print(f"The average amount of pebbles in a superstructure is: {avg:.2f}")
#                                                                    ^- is a float automatically because of the division on line 21

# ------- ------- -------
for i in range(4,11):
    print(f"{i} red suns...")
print("11. WHOLE. SUNS!!!@1!1!@")
print()
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT

#    start amt -v   v- end # (not included)
for i in range(1, 40, 2):#<- what it counts by (step, iterator, iteration)
    print(f"I found a slugcat and stole their pearls! I have {i} pearls now.")
print()
#                       v- counts down!!
for i in range(12, 0, -1):
    print(f"OHNO! I DROPPED MY SLUGPUP! I ONLY HAVE {i} LEFT!")
print()
# ------- ------- -------
# BOOLEAN? ACTUALLY A BOOLEAN?
for i in range(6, 0, -1): # keeps checkign for when the loop should stop. keeps going (as true) until its false
    print(f"{i} SECONDS UNTIL THE TRIPLE AFFIRMATIVE.")
    time.sleep(1) # TIMER!
print("TRIPLE AFFIRMATIVE!")

for waluigi in waluigis_plus:
    if waluigi == "Leo":
        print("*CHUD!")
        break
    else:
        print(f"Hi, {waluigi}!")

# ------- ------- -------
print("This is", end="")
print(" all", end="")
print(" like four", end="")
print(" different print statements.", end="")
# ------- ------- -------