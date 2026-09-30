# Meika Milton, 1st period Programming I, Letter Grade Assignment

while True:
    try:
        class_amt = int(input("Hey John, how many classes are you currently taking: "))
    except:
        print("...Try again, John.")
    else:
        break

grades = []
letter_grad = []

for i in range(1, class_amt):
    while True:
        try:
            grades.append(int(input(f"What's your grade in your {i} period, John?: ")))
        except:
            print("Try again, John.")
        else:
            break

        #grades based on Mrs. Cannon's SM2 class.
    if grades[i - 1] > 100:
        letter_grad.append("A+") # How exactly would I use logical operators for determining + or -?
    elif grades[i - 1] >= 92:
        letter_grad.append("A")
    elif grades[i - 1] >= 90:
        letter_grad.append("A-")
    elif grades[i - 1] >= 89:
        letter_grad.append("B+")
    elif grades[i - 1] >= 86:
        letter_grad.append("B")
    elif grades[i - 1] >= 81:
        letter_grad.append("B-")
    elif grades[i - 1] >= 79:
        letter_grad.append("C+")
    elif grades[i - 1] >= 76:
        letter_grad.append("C")
    elif grades[i - 1] >= 71:
        letter_grad.append("C-")
    elif grades[i - 1] >= 69:
        letter_grad.append("D+")
    elif grades[i - 1] >= 66:
        letter_grad.append("D")
    elif grades[i - 1] >= 62:
        letter_grad.append("D-")
    else:
        letter_grad.append("F")

avg_perc = 0

for grade in grades:
    avg_perc += grade

for i in range(class_amt):
    print(f"Your grade in class #{i} is {grades[i-1]}, which is a {letter_grad[i-1]}.")

avg_perc /= len(grades)
print(f"Your grade average is {round(avg_perc, 2)}")