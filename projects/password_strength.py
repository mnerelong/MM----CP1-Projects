# MM, 1st Period Programming I, Password Strength Checker

def upper(word):
    check = False
    for char in word:
        if char.isupper():
            check = True
            break
        else:
            continue

    return check

def lower(word):
    check = False
    for char in word:
        if char.islower():
            check = True
            break
        else:
            continue

    return check

def number(word):
    check = False
    for char in word:
        if char.isnumeric():
            check = True
            break
        else:
            continue

    return check

def special(word):
    check = False
    for char in word:
        if not char.isalpha() and not char.isnumeric():
            check = True
            break
        else:
            continue

    return check

password = input("Make a password: ") # remembered that strings are
score = 0

if len(password) >= 8:
    score += 1

if upper(password):
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
    print("dude did you even try.")

if score != 5:
    print("\nMake sure your password is over 8 characters long and contains at least one:\n-> uppercase letter\n-> lowercase letter\n-> number\n-> special character\nyeah lock in.")