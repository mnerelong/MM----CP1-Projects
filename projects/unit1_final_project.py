# Meika Milton, Unit 1 Final Project introduction

name = input("Hey there, star! What's your name?\n").title() # name should have first letter capitalized only

while True: #age input
    try:
        age = int(input("Okay, how old are you?\n")) # no reason to be integer other than to limit the options of the user. so that they don't do some "im twelve years old"
    except:
        print("As a number... An integer...")
    else:
        break

old_school = input("What school do you go to? Not to be weird or anything...\nOh and if you don't go to school then just pretend that you do.\n").title()
new_school = input("Alright, now that we have that, what school is the school of your dreams?\n").title()
fav_drink = input("Most important question. What's your favorite drink?\n")

# ALT + Z IS NECESSARY
print(f"\nBehold… our newest star! {name}!!! At the ripe age of {age} years old… they've decided to reach for the sky and take their chances to enroll at {new_school}!\nYes, right now! They are done with {old_school}. Like {name} always says… “In with the new, and out with the old”! Yes!! They say that all of the time!!\nAnd at {new_school} they will enjoy a delicious {fav_drink}! … wait. {fav_drink}? That's your favorite? I'm trying to introduce you in an appealing manner and your favorite drink is {fav_drink}?! I HATE {fav_drink.upper()}!!!! Get OUT!! Introduction OVER!! {name} is a FALLEN STAR!!")