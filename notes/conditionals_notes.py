# Meika Milton, 1st period Programming I, Conditionals Notes

# CONDITIONAL STATEMENT ------- makes decisions based on a boolean value.
pebbles = 5
#v begins with if
if pebbles == 5: # <- bolean statement after the if
    print("FIIIIIVE PEEEBBBBLEEESSS!!!\n\n" * 17)
elif pebbles < 5: # elif only runs if the above statement is false
    print("You... You... My pebbles..?")
else: # ALSO YOU DON'T NEED else YOU CAN JUST END IT...
    print(f"these... are my pebbles... my {pebbles} pebbles...")
# ^ indent. white space is important in python...

affirmative = input("Have you found the triple affirmative?\n")
if not bool(affirmative):
    print("??")
elif affirmative == "yes":
    print("OHH MY GODSSDDDH!!!!!")
else:
    print("m.")

raining = False
if raining:
    print("SLUGCATS RUNN!!!!!!")
else:
    print("I sure hope it doesn't RAIN in this WORLD because then I'd be TWO soggy to walk.")