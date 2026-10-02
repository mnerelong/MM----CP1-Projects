# Meika Milton, 1st period Programming I, Shopping List Manager

def add (shopping):
    shopping.append(input("What would you like to add?\n"))
    return

def done (shopping):
    print("Your shopping list:")
    for item in shopping:
        print(f"{shopping.index(item)} {item}")
    while True:
        try:
            pick = int(input("Which item would you like to mark off?\n"))
        except:
            print("The number...")
        else:
            if pick > len(shopping):
                print("No. No. No. Try again.")
            else:
                break
    done_item = shopping[pick]
    shopping.pop(pick)
    shopping.insert(pick, f"\033[9m{done_item}\033[0m")

shopping = []

for item in shopping: # making sure that nothing is in the list before use
    shopping.remove()

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
        if choice == 2 and not len(shopping) or choice == 3 and not len(shopping): # not instead of ==0? barely faster but was a fun experiment
            print("Uh actually you can't do that... You don't have a list yet!")
        elif choice == 1:
            add(shopping)
        elif choice == 2:
            done(shopping)
        elif choice == 3:
            break
        else:
            print("Not cool dude try again")
            continue

print("\nHere's your final list!")
for item in shopping:
    print(f"\t{item}")
print("Thanks for shopping!")