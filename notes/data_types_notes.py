# Meika Milton, Data Types Notes
#integers. whole numbers.
integer = 1
#         ^ this is an integer. just write the number.
not_integer = 1.00
#              ^ this is a float, because of the decimal.

# Arithmetic Operators (+ (add), - (subtract), * (multiply), / (division), ** (exponents), // (int. division), % (modulo))
print(5 / 2) # Regular division always gives us a float.
print(5 // 2) # No decimal/ Gives us an integer.

print(9 % 4) # Modulo returns the leftover of division. *the remainder of a division problem
# Modulo/Mod | % is called a modulus

print(231/2+4-1%3**5)
# Order of operations "PEMMDAS" (left -> right)
#   Parenthesis, exponents, multiplication uh or modulo or both, division, addition, subtraction.

# Assignment Operator -> =
variable = 23 # sets the variable.
variable += 21 # adds 21 to variable.
variable //= 11 # divides the variable by 11.
# all arithmetic operators work.
variable %= 3
#         ^ an expression

#----------------- HOW TO TURN STUFF INTO OTHER STUFF -----------------
#             v turn input into a float immediately.
data_type = float(input("Pick a number, any number.\n"))
print(f"{data_type + 1}, huh? Wait, not {data_type + 1}? Oh. {data_type}.\n")

print("OR\n")

data_type = input("Pick a number, any number.\n")
print(f"{float(data_type) + 1}, huh? Wait, not {float(data_type) + 1}? Oh. {data_type}.")
#           ^ turn input into a float upon usage.

# converting to int
integer_2 = int(3.14) # DOES NOT ROUND.
print(integer_2)

tob_rounded = 2.69556
print(f"before: {tob_rounded}\nafter: {round(tob_rounded, 3)}\nfully rounded: {round(tob_rounded)}")
#                                                         ^ how many decimal places.            ^ can leave blank to round something to a whole number.
