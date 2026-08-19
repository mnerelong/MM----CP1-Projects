# Meika Milton, Variables Notes.


question = "what is a variable?" # a container.
# and they should be up here, at the top. thats how you organize them. these are called global variables.
# THE SCOPE <---------- where you can use the variable based on when you declare them
# for global variables, the scope is the FULL PAGE

def firstFunc(loc):
    loc = "this is a local variable. it can only be used in a function"
    loc = "it can actually only be used in the function it is declared in"
    loc = "global variables can't be used here..!"



#  -------------------- WHAT CAN THEY DO?  --------------------

declare = "initialize" # declaration & initialization? sets up the variable and lets it be used. first mention of variable.
snake_teeth = "cat thumbs" # name should be easy to understand and accurate to what the variable contains.
# also short and specific
cup = "rootbeer" # much better!

# CREATE VARIABLE
var1 = "variable two contents but they're bad." # you can change variable contents post declaration (& initialization)

# RESET VARIABLE
var1 = "actually i changed my mind they're good."



# -------------------- ANATOMY OF VARIABLE --------------------

# name of var            value of variable
# v                     v
var2 = "this one is bad again"
#    ^ 
#    assignment operator



# -------------------- VARIABLES IN USE --------------------

karma = int(input("uhh what karma are you at? MAKE IT AN INTEGER\n")) # declares and initializes the variable. | int() makes the input an integer. 
print("Oh, you're at karma", karma, "?" ) # uses the variable
karma -= 1 # changes/resets the variable
print("wait you died it's at", karma, "now") # uses the reset variable.



# -------------------- NAMING VARIABLES --------------------

snake_case = "all letters lowercase, spaces replaces with underscores" # use for naming variables
# ex:
cat_thumbs = "snake_teeth_are_weird_and_they_make_me_uncomfortable"


camelCase = "capitalize all first letters of words (after the first one) and remove all spaces." # Ms. Larose uses this to name functions.
# ex:
beerCup = "full"


PascalCase = "capitalize all first letters, remove spaces."
# ex: 
KarmaGate = "Too High"


# NAMES MUST BEGIN WITH A LETTER OR _ & NO SPECIAL CHARACTERS!!!!!!!!!!!!!!!!!!!!!!! 
# names can have numbers (not start with) though but they're not cool
# DO NOT NAME YOUR VARIABLES AFTER KEY WORDS (ex: input, print, def, etc)