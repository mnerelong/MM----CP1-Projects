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
             break
    return intake

def grade(intake):

    while True:
            intake = input(f"What is your last name?\n").title()
            if intake.isalpha():
                break
            else:
                print("Please try again.")
    return intake

user_name = name(0)
phone_num = phone(0)
gpa = []

