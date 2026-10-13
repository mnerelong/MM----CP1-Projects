# Meika Milton, 1st period Programming I, Escape Room

import random

#alt + z highly reccomended. it's the only reason I could sort of comfortably work on this.
room = "comb"
comb_room = ["The platform seems to radiate an energy when the room turns the strongest color of your hair, Madeline Celeste.", "You see several crystals not attached to the cave itself. You can't make out what kind of crystals they are, but their colors are as follows: 1) Red, 2) Green, 3) Yellow, 4) Pink, 5) Blue", "It seems like the birds fly in a set pattern (which is really weird?). They're the same colors as the crystals scattering the caves. The sequence is thus: 3, 4, 1, 1, 5."] # Print out the respective statement.
#items = ["Red crystal", "Green crystal", "Yellow crystal", "Pink crystal", "Blue crystal",] 
#inventory = []
hints = ["Your hair somehow and for some reason changes color when you jump. When you don't jump it rests pink, and you're full of energy. One jump turns it red, and jump once more and you'll find that your hair turns a nice blue, but you're too tired to jump again.", "You suspect that a crystal will fit in the key hole of the platform.", "The birds don't seem to be related to the platform, but maybe they'll be of use later...", "It seems like the birds go in specific directions... the red ones go up; the green ones go left; the yellow ones go up; the pink ones go right; and the blue ones go down.", "How were those colored crystals numbered again...? Oh well, I forgot.", "Birds... crystals... birds... maze... hmm... Makes no sense."]

print("You find yourself in a shining crystal cave. The thin spikes lining the cave seem to share a heartbeat, with iridescent colors being pushed through their veins to create a gentle loop of changing colors.", end=" ")
print("Directly infront of you is a small platform just over a looming pit. There is a key hole in the platform and you suppose that you could stick something in it to make the platform cross the abyss.", end=" ")
print("Blocking your view into the next part of the cave is a huge crystal wall directly over the pit, you notice a small opening in it but you can't tell where it goes.", end=" ")
print("You feel a soft breeze in your hair coming from above you. Looking up, there is a small skylight and you can make out the small forms of birds.")
print("There is nothing that you can see in the room other than crystals of various colors and the platform, however, you can hear the faint singing of birds.\n")

direction_ans = "14112"

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
                            crystal = int(input("Grab a crystal (1-5).\n"))
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
                        print(f"HINT: {hints[random.randint(0, 2)]}") # prints out a random hint
                        continue
                print(comb_room[choice - 1]) # if the user does not choose to do something, they go here.
    elif room == "hive": # every room part of the same if statement so that if the room variable fails then I can catch it with an else.
        print("The platform carries you into the crystal wall, and you realize that you've gotten yourself stuck in a maze. You notice that the platform you're on has simple arrow buttons going Up, Down, Left, and Right.")
        while True: # While loop 3
            try: # the while loop should contain the entire section rather than JUST the try & except so that it can be repeated indefinitely without five billion loops.
                choice = int(input("1) Try something, 2) Remember.\n"))
            except:
                print("...1 or 2?")
                continue
            else:
                if choice < 1 or choice > 2:
                    print("...1 or 2??")
                    continue
                if choice == 1:
                    directions = input("What directions will you go? (Up = 1, Down = 2, Left = 3, Right = 4. EX: 13242)\n")
                    if directions == direction_ans:
                        print("You navigate smoothly out of the maze! You make it to the other side and feel steady ground under your feet again.")
                        room = "sky"
                        break # breaks while loop 3 <-
                    else:
                        print("Unfortunately, you crash into the walls of the maze. The platform seems to reset back to its original position with you on it.")
                        print(f"HINT: {hints[random.randint(3,5)]}")
                        continue
                else:
                    print("Crystals: 1) Red, 2) Green, 3) Yellow, 4) Pink, 5) Blue\nBirds: 3, 4, 1, 1, 5")
    elif room == "sky":
        print("You walk out of the cave and you lose your balance to a strong wind. After regaining your composition, you look over the edge of the overhang and see your freedom down below you. The birds swirl around you and their size is much greater than you initially thought from the skylight. <A<A<A<AHEREHEREHEHERHEHEHREHEHHEREHEREHEREHEREHEREHEREHEREHERE <- HERE")
        while True:
            try:    
                choice = int(input("1) Catch a bird."))