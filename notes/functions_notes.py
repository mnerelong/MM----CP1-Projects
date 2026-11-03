# MM, 1st period Programming I, Functions Notes


def thousand_wind_wine():
    print("Fill up the barrels and store them away,")
    print("and wait, wait for a windier day.")
    print("Wax the bottles, seal them tight.")
    print("With the south wind that soothes, with the north wind that bites.")
    print("How does this fine wine taste to the tongue?")
    print("Like the Mondstadt to the ear of the sweet dream of freedom.")
    print("And what of the fruit that went into the brew?")
    print("An explorers courage, a love tender and true.")
    print("A defenders will, strong as yesteryear,")
    print("joining the thousand winds in a song of good cheer.")
    print("Turning sour into sweet, bitter notes fade away,")
    print("as we wait, wait for a windier day.")


#             v-- parameters are like variables that exist SOLELY in the function
def banning(name, loud_mouth="Albert Rich"):# <- sets a default parameter incase one isn't provided
    print(f"\n{name} is BANNED from the family func.")
    print(f"Will {name} ever be allowed back at the family func? NO. {name.upper()} WILL NOT BE COMING BACK TO THE FAMILY FUNC.")
    print(f"Shut up {loud_mouth} you SUCK at gambling.")
    print("")
    # get it? family FUNCTION?


# --------------- BUILT IN FUNCTIONS vvvvvvvvvvv
# v- command
print("five?")# <- parameters


# print() is an example of a built in function.


# --------------- NOT BUILT IN FUNCTIONS?? vvvvvvvvvvv
thousand_wind_wine()# <---
# calling the function


banning("Five Pebbles")# <- parameters have a local scope.
banning("Mirai Hsiao")# <- they have to be set in the things
#notice how loud_mouth isn't set, so it'll say "Shut up Albert Rich."


mass_ban = "y"


while mass_ban == "y":
    banned = input("Who are you banning?\n")
    banning(banned)


    mass_ban = input("Would you like to ban somebody else from the family func? y/n\n").lower()


# --------------- PARAMETERS vvvvvvvvvvv
# don't define your functions down here kids


#                 v----------v---------- order MATTERS when you're setting them
def position(positional, arguments):
    print(f"I'm {positional}...\nI'm {arguments}!!")


position(2, 1)
print("NOOOOOO!!! THATS WRONG!!")
position(1, 2)
print(":3c")


# --------------- FUNCTIONS
# are like variables, but they hold actions.


# four main purposes
# -> assist in readability
# -> modularity. breaking a big problem into smaller pieces.
# -> abstraction. you can use a function without knowing how the insides work.
