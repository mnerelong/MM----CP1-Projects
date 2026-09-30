# Meika Milton, 1st period Programming I,  Lists, Tuples, and Sets Notes

# ---------- LIST BREAKDOWN!! ----------
#bust a move! Lists are complex data types. Holds multiple values/multiple pieces of information at once.

#                     v items separated by commas
siblings = ["Caspian", "Costeau", "Ripley", "Reif", "Tideus"]
#          ^ brackets make it a list
# EVERY ITEM MUST BE A PROPER DATA TYPE

print(siblings)# UGLY!!
print(*siblings)# not ugly. called UNPACKING ITS THE UNPACKING OPERATOR UNPACKING

# ---------- ----------
#strings are lists
# ORDERED
# MUTABLE changeable ynknow
# DUPLICATES are ok so you can have multiple of the same things
# ---------- ----------

#             0          1          2          3            4          5           6            7
slugcats = ["Monk", "Survivor", "Hunter", "Artificer", "Gourmand", "Rivulet", "Spearmaster", "Saint"]
print(f"{slugcats[0]} fought {slugcats[5]} and won.")
print(f"THE {slugcats[-1].upper()} KILLED FIVE PEBBLES!!")
#                      ^ negative goes backwards. really helpful actually

# ---------- ----------
length = len(siblings) # gets the length !!!!!!!!!!!!!
# ---------- ----------
slugcats.append("Enot")# adds to the end of the list
print(*slugcats)
# ---------- ----------
siblings.insert(0, "The Yellow One")# adds it to whereever you want!!!!! !!!
print(*siblings)
# ---------- ----------
slugcats.extend(["Watcher", "Kale"])# uh... puts two lists together
print(*slugcats)
# ---------- ----------
siblings.remove("The Yellow One") # No index
print(*siblings)
# ---------- ----------
slugcats.pop(0)# removes the last one IF there is no >>>>> index given <<<<<
print(*slugcats)


# ---------- TUPLES BREAKDOWN!! ----------
#trust a move!

# when you don't want somebody to move stuff
ocs = ("\nDoris", "Croker", "Merten", "Benny", "Beppu", "Dalton", "Artipex")
#      ^ parenthesis NOT brackets

# ORDERED
# IMMUTABLE - not changeable
# DUPLICATES are ok so you can have multiple of the same things

print(*ocs) # unpacking works
print(f"{ocs[0]} is a bad person")
# no adding or removing



# ---------- SETS BREAKDOWN!! ----------
#must move!

waluigis_plus = {"Leo", "Cohen", "Mirai", "Elijah", "Isaac C.", "Isaac B." "Jay", "Santi"}
#               ^ CURLY

# UNORDERED
# MUTABLE
# NO DUPLICATES

print("\n", *waluigis_plus) # UUUUUUUUUUNNNNNNNNPPPPPPPAAAAAAACCCCCCCCKKKKKKKKKKIIIIIIIIIINNNNNNNNGGGGGGGGGGG
print(f"{len(waluigis_plus)} is how many people are in the waluigis plus") # length works but NOT INDEX STUFF

waluigis_plus.update({"Leo", "Cohen", "Mirai", "Elijah", "Isaac C.", "Jay", "Santi", "Dirk"})
print(*waluigis_plus)
waluigis_plus.remove("Dirk")
print(*waluigis_plus)
# ohno

# ---------- CONVERTING BREAKDOWN!! ----------
#lust on the move!
slugcats_set = set(slugcats) # ugh
waluigis_tuple = tuple(waluigis_plus) # ugh
ocs_list = list(ocs)# ugh
#        ^ You have to make new variables


# I'M PRETTY SURE YOU CAN PUT TUPLES AND STUFF IN LISTS IDK :(