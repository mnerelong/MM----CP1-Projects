# MM, period 1 Programming II

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        while True:
            try:#       v- code would not run if user inputs something that is not an number. runtime error.
                guess = int(input("Guess a number between 1 and 20: "))
            except:
                print("Please pick a number.")
            else:
                guesses = guesses + 1
                break

        if guess == secret_number: # <- missing colon. syntax error.
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---") #  v- you cannot concatonate lists. runtime error I believe? syntax error?
print("Your guesses per round: ", *scores) # <- also unpacking is important, y'know?

total = 0
for score in scores:
#    total = 0 setting total to 0 for every single iteration. this is bad. logic error.
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(average, 2)))# rounded so that it looks nicer. not really an error, it's just... unpleasant.

best_round = scores[0]
for i in range(1, rounds - 1):
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")