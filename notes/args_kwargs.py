# MM, 1st period Programming I, *args & *kwargs notes

# ------------------- *ARGS
# Use *args when you don't know how many arguments there will be. HAS to be the last parameter.
def arg_usage(name, *star): # <------ the important part is the star!! can be named anything
    print(args) # <-- args makes a tuple. not changeabele.
    for item in args:
        print(f"Hello {item}! Have you seen {name}?")

arg_usage("Cohen", "Five Pebbles", "Leo", "Mirai", "Moon", "Milky", "Orsoniks", "Joar", "Caspian")
arg_usage("Deltarune", "Kris")
arg_usage("the Triple Affirmative", "Five Pebbles", "No Significant Harassment", "Looks to th Moon", "Sliver of Straw")


# ------------------- **KWARGS
# ----> stands for keyword arguments
def clean(decimals = 0, **kwargs): # kwargs makes a dictionary.
    if not kwargs.get("data"):
        return "There is no data."
    if kwargs.get("type") == "str":
        return kwargs.get("data").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs.get("data"))
    elif kwargs.get("type") == "float":
        return round(float(kwargs.get("data")), decimals)
    elif kwargs.get("type") ==  "list":
        return str(f"{x}," for x in kwargs.get("data"))
    elif kwargs.get("type") == "bool":
        return f"{kwargs.get("data")}"
#             v------------v--------------> you can specify which one is which
print(clean(type="int", data="411"))
print(clean(data="        oasijdsJAHHH  ", type="str"))
#            ^                              ^
#           /                                \  
#          /-let you just use kwargs ---------\