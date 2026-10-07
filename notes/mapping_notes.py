# Meika Milton, 1st period Programming I, Mapping Notes

import math

# ----------------------------------------------------------------
# mapping is the process of running the same function on each item in a list.
# ----------------------------------------------------------------

def add(num):
    return num + 2
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv why doesnt it work :(
numbers = range(1, 18) # way easier than [1, 2, 3, 4, 5, 6, 7, 8, etc etc]
pebbles = [1, 3, 5, 7, 17, 18]

# ----------------------------------------------------------------

#                     v- has to be a function
suns_peb_mult = map(add, pebbles)# leaves the original data alone and is just really simple
print(suns_peb_mult)
# prints <map object at 0x000001429B779E10> <- called a pointer. tells you where its at but not really what it is !!!!1!1!!111!!1!1!1!!1!1!!!!111!!1!!11

for sun in suns_peb_mult:
    print(f"{sun} red suns")

# ----------------------------------------------------------------

num_add = map(add, numbers)
print(*list(num_add)) # won't print something ugly. prints right!!
#     ^- AND you can unpack here!!

# a for loop would be infinitely more work. for loop changes the list itself so if you want a new list then you'd have to make a new list ALONG WITH the loop and its just chud stuff



# ----------- ACCUMULATOR PATTERN!!!!!----------------------------
# when you just add a bunch of one thing to a list?
# ----------------------------------------------------------------

iterators = ["Pebbles", "Pulse", "Moon", "Harassment", "Suns", "Straw"]
length = list(map(len, iterators))
print(length)

def product(num):
    return num**2

length_product = list(map(product, length))
print(length_product)

# ----------------------------------------------------------------
print(math.factorial(5)) # ugh