# MM, 1st period Programming I, Order Up!

def food_picker(menu, chosen, type):
    while True:
        picking = input(f"What would you like from our {type}?\n").title().strip()
        if picking not in menu[type]:
            print("That isn't available.")
            continue
        else:
            chosen.append(picking)
            break

def clean_up(string="Triple Affirmative"):
    fresh_string = ""
    for character in string:
        if string.index(character) >= 5 and character == 's' and not string == "Main Courses":
            break
        elif string == "Main Courses":
            fresh_string = "Main Course"
            break
        fresh_string += character
    return fresh_string

menu = {
    "Main Courses": {
        "Foliage Meal": 15,
        "Flesh Chunk": 10,
        "Dog Food": 17,
        "Paprikash": 17,
        "Pemmican": 18
    },
    "Sides": {
        "Geo Fruit": 4,
        "Cactus Chunk": 3,
        "Candy Bar": 7,
        "Ketchup Bottle": 5,
        "Aspic": 9
    },
    "Desserts": {
        "Cereal": 16,
        "Mysterious Can": 2,
        "Pancakes": 17,
        "Cake": 15
    },
    "Drinks": {
        "Water": 7,
        "Soda": 9,
        "Biochem Fluid": 3,
        "L.R.D. Serum": 10
    }
}

user_chosen = []
total = 0
single_menu = []
for type in menu:
    fresh_type = str(clean_up(type))
    single_menu.append(fresh_type)
    

for sub_menu, item in menu.items():
    print(f"{sub_menu}--> {item}")  
print()

i = 0
for type in menu:
    food_picker(menu, user_chosen, type)
    if type == "Sides":
        print("\nAgain.")
        food_picker(menu, user_chosen, type)
        i+=1
    total += menu[type][user_chosen[i]]
    i+=1
    print()

i = 0
print("Your order is thus:\n")
for item in single_menu:
    print(f"{item}: {user_chosen[i]}")
    i+=1
    if item == "Sides":
        print(f"\t{user_chosen[i]}")
        i+=1
print(f"\n\tTotal: ${total}.00")