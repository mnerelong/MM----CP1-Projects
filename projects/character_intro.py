# Meika Milton, Character Introduction

name = input("What's your name?\n").title()
age = int(input("How old are you?\n"))
job = input("What's your job?\n").lower()
origin = input("Where did you come from?\n").title()


if age >= 70:
    print(f"Oookay. Let me get this right. You are {age} years old... with the name... {name}- from {origin} nonetheless- and your job is {job}??? The concepts...")
    print(f"Are you turning {age + 1}? Or did you turn {age} just this year?")

elif age >= 40:
    print(f"Alright, {name}. You're really old. {age}? Going on {age + 1} I'm assuming? And I mean, you said you're from {origin}? Old. You're so old. They should call you Uncle {name}.")
    print(f"Oh, you also said your job was {job}? Heh, okay Uncle {name}.")

elif age >= 18:
    print(f"Hello {name}! Nice to meet you. You're {age}? I am too! I'm also from {origin}, kinda close to the South end. I thought my job would end up being {job}, but I ended up being a computer instead.\nI hope we meet again, {name}.")

elif age >= 11:
    print(f"Uhm... {name}... You seem to be pretty young to be working the job {job}... only {age}? I don't trust you. I don't trust {age} year olds. GO BACK TO {origin.upper()}!!!")

elif age <= 10 and age > 1:
    print(f"You're {age}? get out of here I don't have time to babysit you. I don't believe that you have a job as a {job}. Go back to {origin.upper()}!!!!!!!!!!!!!!")

else:
    print(f"{name} are you even real. how are you {age} genuinely bro wdym you're a {job}... what is wrong with people from {origin}...")