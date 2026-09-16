# Meika Milton, 1st period Programming I, fixing the Ravager Snack Bar

import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits (:D?ok)
while True:
    try:
        quantity = float(input("How many would you like? ")) # while true loop my beloved!
    except:
        print("Arrr?? That's not a number???")
    else:
        break

total = price * int(quantity) # quantity was a string. Switched it to be an integer. run time error.

discounted_total = total - 2 * 0.10

tax_rate = 0.08 
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) # fixed incorrect variable name. run time error.
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total)) # logic error, total before tax should be the total. used to just be the price.
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # added missing parenthesis. syntax error.

# WHERE IS THE SECOND LOGIC ERROR!!???!?!?!?!?!?!?!
# THERE IS NONE!!!!!!!!