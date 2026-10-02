# Meika Milton, 1st period Programming I, Multiplication Table
while True:
    try:
        user_range = int(input("How big dya want your multiplication table?\n"))
    except:
        print("...Sorry... it has to be a number. It's multiplication?")
    else:
        break

for i in range(1, user_range + 1): # +1 so that it includes the chosen number
    for x in range(1,user_range + 1):
        print(x * i, end="\t")
    print("\n\n")