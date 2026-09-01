# Meika Milton, 1st period Programming I, Average Grade

# -------------asking how many classes
while True:
    try:#                v int because people aren't going to have 7.623 classes
        classes_num = int(input("Hey! How many classes are you currnetly taking?\n"))
    except:# irrelevant but I love the hollow knight soundtrack please play it more
        print("A number, genius.")
    else:
        break

# -------------asking grades
grades = [] # I DON'T KNOW WHAT I'M DOING
n = 1
while n <= classes_num:
    while True:
        try:
            query = float(input(f"What is your grade in your {n} period?"))
        except:
            print("AS A NUMBER... ")
        else:
            break
    grades += [query] # its works so DONT TOUCH IT :(
    n += 1

sum_grades = 0
for grade in grades:
    sum_grades += grade

grade_avg = sum_grades / classes_num
print(f"Your grade average is {grade_avg}! You have {len(grades)} classes.")

#for grade in grades:
#    print(f"{grade}")