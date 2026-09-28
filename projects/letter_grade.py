# Meika Milton, 1st period Programming I, Letter Grade Assignment

class_amt = input("Hey John, how many classes are you currently taking: ")
grades = []

for i in range(1, class_amt):
    while True:
        try:
            grades.append(int(input(f"What's your grade in your {i} period?")))
        except:
            print("Try again, John.")
        else:
            break
    if grades.index(i) > 100:
        letter_grad = "A+"

avg_perc = 0

for grade in grades:
    avg_perc += grade

avg_perc /= len(grades)
print(f"Your grade average is {avg_perc}")