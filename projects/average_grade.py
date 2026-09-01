# Meika Milton, 1st period Programming I, Average Grade

# -------------asking how many classes
def check(period_amt):
    while True:
        try:#                v int because people aren't going to have 7.623 classes
            period_amt = int(input("Hey! How many classes are you currnetly taking?\n"))
        except:# irrelevant but I love the hollow knight soundtrack please play it more
            print("A number, genius.")
        else:
            break
    return period_amt

# THANK YOU ISAAC FOR THE FUNCTION IDEA TO MAKE SURE PEOPLE DON'T DO 0 CLASSES!!!
#-------------makes sure that the amount of classes is acceptable
classes_num = check(0)
while True:
    if classes_num == 0:
        print("I'm sorry, why are you using a grade average calculator if you have zero classes..?\nTry again.")
        classes_num = check(0)
    elif classes_num < 0:
        print("Could we do a positive number please?\nTry again.")
        classes_num = check(0)
    else:
        break

# -------------asking grades in classes
grades = [] # I DON'T KNOW WHAT I'M DOING
n = 1
while n <= classes_num:
    while True:
        try:
            query = float(input(f"What is your grade in your {n} period?\n"))
        except:
            print("A number.")
        else:
            break
    grades += [query] # its works so DONT TOUCH IT :(
    n += 1

sum_grades = 0
for grade in grades:
    sum_grades += grade

grade_avg = sum_grades / classes_num
print(f"Your grade average is {round(grade_avg,2)}! You have {len(grades)} classes.")

#for grade in grades:
#    print(f"{grade}")