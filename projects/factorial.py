# Meika Milton, 1st period Programming I, Factorial Calculator

while True:
    try:
        num = int(input("Give me a number, any number!!\n"))
    except:
        print("...Try again dude.")
    else:
        if num < 0:
            print("Ha ha nice try.")
        else:
            break

equation_num = range(num, 1, -1)

for number in equation_num:
    print(number)

print(equation_num)