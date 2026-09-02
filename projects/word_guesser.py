# Meika Milton 1st period Programming I

word = "pebbles"
print(f"The word has {len(word)} letters.")

def guessing(user_guess):
    while True:
        user_guess = input("Guess one letter.\n").lower()
        if len(user_guess) > 1:
            print("I said one letter, genius.")
        else:
            break
    return(user_guess)

print(guessing(0))