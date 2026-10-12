# Meika Milton, 1st period Programming I, Escape Room

import random

room = "comb"
comb_room = ["The platform seems to radiate an energy when the room turns the strongest color of your hair, Madeline Celeste.", "You see several crystals not attached to the cave itself. You can't make out what kind of crystals they are, but their colors are as follows: 1) Red, 2) Green, 3) Yellow, 4) Pink, 5) Blue", "It seems like the birds fly in a set pattern (which is really weird?). They're the same colors as the crystals scattering the caves. The sequence is thus: 3, 4, 1, 1, 5."] # Print out the respective statement.
items = ["Red crystal", "Green crystal", "Yellow crystal", "Pink crystal", "Blue crystal",] 
inventory = []
hints = ["Your hair somehow and for some reason changes color when you jump. When you don't jump it rests pink, and you're full of energy. One jump turns it red, and jump once more and you'll find that your hair turns a nice blue, but you're too tired to jump again."]

print("You find yourself in a shining crystal cave. The thin spikes lining the cave seem to share a heartbeat, with iridescent colors being pushed through their veins to create a gentle loop of changing colors", end=" ")
print("Directly infront of you is a small platform just over a looming pit. There is a key hole in the platform and you suppose that you could stick something in it to make the platform cross the abyss.", end=" ")
print("Blocking your view into the next part of the cave is a huge crystal wall directly over the pit, you notice a small opening in it but you can't tell where it goes.", end=" ")
print("You feel a soft breeze in your hair coming from above you. Looking up, there is a small skylight and you can make out the small forms of birds.")
print("There is nothing that you can see in the room other than crystals of various colors and the platform, however, you can hear the faint singing of birds.\n")

while True: # While Loop 0
    if room == "comb":
        while True: # While loop 1
            try:
                choice = int(input("1) Inspect the platform, 2) Look through the crystals, 3) Watch the birds, 4) Try something.\n"))
            except:
                print("...1, 2, 3, or 4??")
            else:
                if choice < 1 or choice > 4:
                    print("...1, 2, 3, or 4??")
                    continue
                if choice == 4: # if the user decides to do something.
                    while True: # While loop 2
                        try:
                            crystal = int(input("Grab a crystal (1-5)."))
                        except:
                            print("A number between 1 and 5.")
                        else:
                            if crystal > 5 or crystal < 1: # triple nested conditionals...
                                print("A number between 1 and 5.")
                                continue
                            break # Breaks while loop 2 <-
                    if crystal == 4: # Here is win!
                        print("The crystal works perfectly, and the platform shudders to life. It pulls itself over the pit with you on it.")
                        room = "hive"
                        break  # Breaks while loop 1 <-
                    else:
                        print("It fits, but the platform doesn't do anything.")
                        print(f"HINT: {hints[random.randint()]}") # HERE HERE HERE WORK HERE HERE HERE
                        continue
                print(comb_room[choice - 1]) # if the user does not choose to do something, they go here.
    elif room == "hive": # every room part of the same if statement so that if the room variable fails then I can catch it with an else.
        while True: