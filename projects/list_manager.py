# Meika Milton, 1st period Programming I, Shopping List Manager

def add (shopping):
    shopping.append(input("What would you like to add?\n"))
    return

def done (shopping):
    print("Your shopping list:")
    for item in shopping:
        print(f"{shopping.index(item)} {item}")
        

item = "my name is FIVE PEBBLES" # testing sorry m tesyting
print(f"\033[9m{item}\033[0m") # THANK YOU ISAAC B THANK YOU ISAAC B

shopping = []

for item in shopping:
    shopping.remove()

if len(shopping) == 0:
    print("This is your list and there's nothing here.")
else:
    for item in shopping:
        print({item})
    
while True:
    try:
        if len(shopping) == 0:
            print("This is your list and there's nothing here.")
        else:
            print("Your shopping list:")
            for item in shopping:
                print(f"\t{item}")
        choice = int(input("\nWould you like to, (1) add something to your list or (2) mark something as done, or (3) finish your list.\n"))
    except:
        print("Please pick one of the numbers bro")
    else:
        if choice == 1:
            add(shopping)
        elif choice == 2:
            done(shopping)
        else:
            print("Not cool dude try again")
            continue