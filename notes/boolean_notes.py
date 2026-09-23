# Meika Milton, 1st period Programming I, Boolean Notes


# BOOLEANS ----------------
# primitive data type with only 2 values.
better_than = False
five_pebbles = True # 1st letter has to be capitalized.
print("I am five pebbles and I am better than you. True or false?")
if better_than: # --- booleans are very simple!!
    print("He is!")
else:
    print("He is not, but to him, he is.")

# COMPARISON OPERATORS ----------------

age = 35
if 17 < age: # boolean equation. will always result in true or false
    print("You are really old.")


" list : "
"[<] less than "
"[>] greater than "
"[<=] less than or equal to"
"[>=] greater than or equal to"
"[==] equal to"
"[!=] not equal to"

# ANYTHING!!!! ANYTHING CAN BE A BOOLEAN!!!! ----------------
print("\n",bool(age)) # age is true...
age = 14
print(f"Age... age is... {bool(age)}.")
age = 0
print(f"But NOW... now age is {bool(age)}.")
age = -14
print(f"Now its {bool(age)} again.")

#STRINGS ARE ALWAYS TRUE!! unless they re empty.
sentence = "Unparalleled Innocence is a CHUD!!"
print(sentence)
print(f"It's {bool(sentence)}.")
sentence = ""
print(f"But unparalleled innocence says its {bool(sentence)}. hm.")

iterators = ["five pebbles", "looks to the moon"]
if "five pebbles" in iterators: # in ---------------->
    print("Five Pebbles is an iterator!!")

if 2 is 2: # is ---------------->
    print("2 is 2 I guess?")
