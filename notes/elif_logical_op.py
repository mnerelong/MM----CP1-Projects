# Meika Milton, 1st period Programming I, Elif & Logical Operators Notes
import random

suns = random.randint(0, 10)
pebbles = random.randint(0, 10)

# ------- CONDITIONALL!!!
if suns == 7: # all conditionals behgin with an if.
    print("Welcome home, seven red SONS!!")
elif suns >= 5: # as many elifs as you want!!
    print("Well, at least theres some suns left.")
else: # marks the end of the conditional.
    print("UNPURPOSED ORGANISMS!!! LEAVE!!")

# ------- LOGICAL OPERATORS... [AND] [OR] [NOT]
if suns == 7 and pebbles == 5: # BOTH have to be true
    print("TRIPLE AFFIRMATIVE!")
elif suns == 7 or pebbles == 5: # only ONE has to be true
    print("double affirmative..? single affirmative?")
elif not suns == 7 and not pebbles == 5: # THEY HAVE TO BE FALSE!
    print("void bath")
else:
    print("What could have possibly happened?")

iterator = False #  vvv yoo
if pebbles == 5 and not iterator:
    print("WHO ARE YOU?! ascend")
else:
    print("lalalala la la lalalalala")

# win check
rain = True if pebbles >= 5 else False
timer = 25

# if it's raining or the timer is out then the game is over
if rain or timer <= 1:
    print("Game o-o-o-over.")
    if timer > 0:
        pass # makes it do nothing... it's a placeholder.
    else:
        print("Pebbles... the rain is here.")
else:
    print("cycle cycle breaker cycle breaker cycle cycle breaker")