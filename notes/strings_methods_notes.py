# Meika Milton, 1st period Programming I, Strings Methods Notes

sentence_1 = "Triple AFFIRMATIVE!! Confirmed!!!"

# ----- function?? Premade function?
print(len(sentence_1)) #<- object
#^ action

# ----- methods (DOT NOTATION)
print(sentence_1.lower()) # <- action
# ^ object
print(sentence_1.upper()) # all uppercase
print(sentence_1.title()) # all first letters capitalized
print(sentence_1.capitalize()) # only first letter capitalized
# all about output...
#                                           v strip removes white space before and after a string (ex: "                        lalala                        ")
name_1 = input("What's your name?").title().strip() # you can also do title in the print statement
print("Have you found the solution yet, " + name_1 + "?")

# --- be specific

# name_2 = input("Okay one more time, what is your NAAME?").title().strip().split()
# print(name_2)
# fixed_name_2 = "".join(name_2)
# print(f"You think you're slick, {fixed_name_2}?")

# ---

first_name = input("What is your first name?\n").strip().split()
first_fixed = "".join(first_name).title()
last_name = input("What is your last name?\n").strip().split()
last_fixed = "".join(last_name).title()
full_name = first_fixed + " " + last_fixed

print(f"Nice try, {full_name}.")

# ----- REPLACING WORDS IN SENTENCES OH MY GOD
changed_1 = sentence_1.replace("Confirmed", 'Denied').title()
print(changed_1)

sentence_2 = "Five Pebbles lost his five pearls."
pearl_old_amt = input("How many pearls are there?\n").strip().capitalize()
pearl_new_amt = input("How many pearls are there NOW?\n").strip().capitalize()

changed_2 = sentence_2.replace(pearl_old_amt, pearl_new_amt)
print(changed_2)

# ----- finding substrings & SPLITTING STRINGS
print(changed_1.find("Denied")) #.find() returns an index

print(sentence_2.split()) # <- PUTS EVERY WORD IN A LIST!!!!!!!!!!!!!!!!!!!! SEPARATED BASED ON SPACES
print(sentence_2.split("five")) # <- REMOVES WHATEVER YOU SPLIT ON!!!

# ----- CHECKING TO MAKE SURE EVEYTHING IS LIKE VALID or whataverr!!
char = input("give me something (just one something)\n")
print(char.isalpha()) # is it ALL letters?
print(char.isnumeric()) # is it ALL numbers?
print(char.isupper()) # is it ALL uppercase?
print(char.islower()) # is it ALL lower?
print(char.istitle()) # is it a title?