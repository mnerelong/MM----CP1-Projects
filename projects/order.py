# MM, 1st period Programming I, Order Up!

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
    "Dessert": {
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

for sub_menu, item in menu.items():
    print(f"{sub_menu}--> {item}")  
