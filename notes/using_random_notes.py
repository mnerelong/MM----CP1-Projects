# Meika Milton, 1st period Programming I, Random Numbers
import random
#         ^ module/library
# contains a bunch of pre-built functions.

#                     lowest
#                        v
pebbles = random.randint(0,5)# < highest
print(f"Pebbles... {pebbles} pebbles?!")
# RETURN: the info that is given back.




# ------- SO MUCH FUN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T YOU JUST LOVE IT??
iterators = ["Five Pebbles", "Big Sis Moon", "No Significant Harrassnent", "Sliver of Straw", "Seven Red Suns", "Gray Winds", "Unparalleled Innocence"]
print(f"{iterators[random.randint(0,6)]} has ascended.")


#    |   |   
#----|---|----
#    |   |
#----|---|----
#    |   |

#    |   |   
#----|---|----
#    | x |
#----|---|----
#    |   |

# o  |   |   
#----|---|----
#    | x |
#----|---|----
#    |   |

# o  |   |   
#----|---|----
#    | x |
#----|---|----
#  x |   |

# o  |   |   
#----|---|----
#    | x |
#----|---|----
#  x | o |

# o  |   |  x
#----|---|----
#    | x |
#----|---|----
#  x | o |

#_______
#|    |  help me
#|    o   ^       (----                 (----)
#|   /|\          |   _            _    |    |     _   __
#|   /\           |____| []\ |\/| (-'   |____| \/ (-' |
#_______                           ``              ``

# ------- RANDOM RANGE!! 
#                  start___    stop (not included)
#                          v   v                                          2s                 3s
crayons = random.randrange(2, 48, 3)# < counts by 3rd number. (ex: [1, 3, 5, 7, 9] [1, 4, 7, 10, 13, 16, 19])
print(f"\nHow the HELL did you eat all {crayons} of my crayons?!?!")

#                 v float between 0 - 1 (so like... percentages!!)
completion = random.random()
print(f"The triple affirmative is {completion:.2} done.")
completion_perc = round(completion * 100, 1)
print(f"SORRY sorry I meant {completion_perc}%...")

# floats are really difficult for python (Ms. Larose's words, not mine.)