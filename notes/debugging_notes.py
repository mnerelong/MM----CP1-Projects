# Meika Milton, Debugging Notes

#----------------------------------------

# Syntax Error
# - You wrote it wrong... code will not run.
# ex: print("whats going on?) or print("Hey guys"


    # Indentation Error (form of syntax error)
#    ex:
#    if true:
#    print(this is true) #<- should be indented under the if

#    if true:
#       print(this is true) #<- should be indented under the if

#----------------------------------------

# Logic Error
# - Haven't written anything wrong, but you did the wrong steps. It doesn't work how you want it to or at all (but it runs...).
#ex:
blue_fruit = 20
people = 3
#                 v make it a /
print(blue_fruit * people) # Tells me how many blue fruit everybody can have!!!
# No it doesn't...

#----------------------------------------

# Run-time errors
# - Happen while the code in running,  code doesn't finish. Can often be the user's fault.

#ex: fav_year = input("Favorite year?\n")
#    print(1 + fav_year) # ^ string

# You can't add a string to an integer and vice versa...

# To fix: ( and loop )
while True: # makes a loop that wont stop
    try:
        fav_year = int(input("Favorite year?\n"))
    except:
        print("That's not a year! Or a number! At all")
    else:
        break # breaks loop once user inputs a number and lets the program move on.
print(f"Cool. Mine is {1 + fav_year}.")