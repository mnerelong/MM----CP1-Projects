# Meika Milton, 1st period Programming I, Madlib

word_types = ["a creature", "a place", "another place", "an adjective", "a noun", "an emotion or feeling", "a verb ending in -ed/past tense", "a game", "a verb", "an adjective", "another adjective", "a place", "a food or drink", "a verb ending in -ing" ]
word_response = []
for i in word_types:
    word_response.append(input(f"Give me... {i}.\n"))

#--------------- If the assignment didn't say to save these in variables then I'd just put the responses directly into the print statement
# But I don't know if saving them as variables does have some benefits
# Maybe that it's easier to adjust specific responses without having to dig through the print statement?
creature = word_response[0].lower()
place_1 = word_response[1].title()
place_2 = word_response[2].title()
adjective_1 = word_response[3].lower()
noun_1 = word_response[4].lower()
emotion = word_response[5].lower() # Making it lowercase first so that if I ever wanted to use it regularly I could just put it in without worrying about it being uppercase. Lowercase is the base.
verb_1 = word_response[6].lower()
game = word_response[7].title()
verb_2 = word_response[8].lower()
adjective_2 = word_response[9].lower()
adjective_3 = word_response[10].lower()
place_3 = word_response[11].title()
food_drink = word_response[12].lower()
verb_3 = word_response[13].lower()

print(f"\n\nOne time I saw a {creature} run straight through {place_1}.\nI don't know where the {creature} was going. Maybe {place_2}? It looked kind of {adjective_1}.\nOH MY GOD!! IT CAME BACK!!! WITH A {noun_1.upper()}?! I'M SO {emotion.upper()}!!!!\n\t*sound effects*\nokay so anyways I {verb_1} it and it's gone now.\nThat kind of reminded me of {game}.\nTake note. When a {creature} runs through {place_1} and comes back with a {noun_1}, the only thing that will get rid of it is to {verb_2} it.\nWait, I didn't {verb_2} it? My bad. My memory is pretty {adjective_2}. Anyways it's uh... pretty {adjective_3} outside today here in {place_3} don't you think?\nNo? Well I don't like people who consume {food_drink}. I HATE {food_drink.upper()}!! Let's fight. No {verb_3}.")