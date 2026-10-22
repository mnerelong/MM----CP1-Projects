# MM, 1st period Programming I, Factorial Calculator

import math

def factorialize(number): # I wanted to make my own function if that's okay. I understand how to use math though.
    new_num = number
    for i in range(number - 1 , 0, -1):
        new_num *= i
    return new_num

while True:
    try:
        num = int(input("Give me a number, any number!!\n"))
    except:
        print("...Try again dude.")
    else:
        if num < 0:
            print("Ha ha nice try.")
        else:
            break

equation_num = range(num, 0, -1)
factorials = list(map(factorialize, equation_num)) # or list(map(math.factor, equation_num)) for using math

print()
for number in equation_num:
    print(f"{number}! = {factorials[equation_num.index(number)]}") # finds the index of the number and then finds the item at the same index.

