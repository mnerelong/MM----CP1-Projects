# Meika Milton, 1st period Programming I, Idiot Proof Assignment
def name(intake):

    while True:
            intake = input(f"What is your last name?\n").title().strip()
            if intake.isalpha():
                break
            else:
                print("Please try again.")
    return intake

def phone(intake):

    while True:
        try:
            intake = int(input(f"What is your phone number?\n"))
        except:
            print("Please try again.")
        else:
            intake = str(intake)
            if len(intake) == 10:
                intake = list(intake) # I admit that I searched this up, but I'm glad that I did! I feel like I learned something (because I did)
                intake.insert(3, " ") # sorry I looked up insert too.
                intake.insert(7, " ")
                intake = "".join(intake)
                break
            else:
                print("Try again.")
    return intake

def grade(intake):

    while True:
        try:
            intake = float(input(f"What is your GPA?\n"))
        except:
            print("No... Try again.")
        else:
            if intake > 12 or intake < 0:
                print("Sure. Sure buddy. Try again.")
            else:
                break
    return intake

user_name = name(0)
phone_num = phone(0)
gpa = grade(0)

print(f"Let me get this straight. Your LAST name is {user_name}; your phone number is {phone_num}; and you have a {gpa} GPA?\nWhatever. I didn't even ask.")