# MM, 1st Period Programming I, Password Strength Checker

# all functions work the same
def upper(word): # function that checks for uppercase letter
    check = False
    for char in word: # goes through each character in the given word and
        if char.isupper(): # checks to see if its uppercase.
            check = True # the second that the code notices any uppercase letter it sets the check to True and breaks the code.
            break
        else:
            continue

    return check

def lower(word): # function that checks for lowercase letter
    check = False
    for char in word:
        if char.islower():
            check = True
            break
        else:
            continue

    return check

def number(word): # function that checks for a number
    check = False
    for char in word:
        if char.isnumeric():
            check = True
            break
        else:
            continue

    return check

def special(word): # function that checks for a special character
    check = False
    for char in word:
        if not char.isalpha() and not char.isnumeric():
            check = True
            break
        else:
            continue

    return check

# I don't understand any(). we haven't learned that. I checked w3schools and it still doesn't make sense, sorry!
# I did think about making one big function but I don't know how to use code *within* a parameter or *within* a list, because thats the only other way I could think to do it.
# I probably didn't think hard enough huh :/

password = input("Make a password: ")
score = 0

if len(password) >= 8:
    score += 1

if upper(password): # if check returns True, then the score will go up.
    score += 1

if lower(password):
    score += 1

if number(password):
    score += 1

if special(password):
    score += 1

print()
if score == 1 or score == 2:
    print("You did so bad. You did sooo bad. That’s a terrible password. Weak.")
elif score == 3:
    print("You’re like… I don’t even know. This is fine. Moderate.")
elif score == 4:
    print("Okay… tuff… I like it… tuff… Strong password.")
elif score == 5:
    print("Oh… my… goodness… Could you write MY passwords for me? Strongest password ever!!")
else:
    print("dude did you even try.") # I don't think its possible to get a password with a different score, but it's good to have a catch anyways.

if score != 5: #                        vvvvvvvv- fixed
    print("\nMake sure your password is at least 8 characters long and contains at least one:\n-> uppercase letter\n-> lowercase letter\n-> number\n-> special character\nyeah lock in.")