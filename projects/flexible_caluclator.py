# MM, period 1 Programming I, Flexible Calculator

def sum_of(*nums):
    total = 0
    for num in nums[0]:
        total += num
    return total

def average_of(*nums):
    total = 0
    for num in nums[0]:
        total += nums
    avg = total/len(nums)
    return avg

def max_of(*nums):
    maximum = nums[0][0]
    for num in nums:
        if num > maximum:
            maximum = num
        else:
            continue
    return maximum

def min_of(*nums):
    minimum = nums[0][0]
    for num in nums[0]:
        if num < minimum:
            minimum = num
        else:
            continue
    return minimum

def product_of(*nums):
    product = num[0][0]
    i = 0
    for num in nums[0]:
        if not i:
            i+=1
            continue
        product = product * num

def number_picking(**kwargs): # using kwargs here so that it doesn't break if i were to put something in
    user_numbers = []
    print("\nEnter the numbers that you want (individually, separated by you pressing enter). When you're finished simply keep the input blank.")
    while True:
        try:
            number = 0
            number = int(input("Number here: "))
        except:
            if not number and len(user_numbers) == 0:
                print("You haven't given enough information!")
                continue
            if not number:
                break
            print("Not an option.")
            continue
        else:
            user_numbers.append(number)
    print("Your numbers:", *user_numbers) 
    return user_numbers

# --------------------

user_numbers = []

while True: # loop 1
    while True: # loop 2
        try:
            to_do = int(input("Hello! Would you like to:\n[1] Find the sum of-\n[2] Find the average of-\n[3] Find the max of-\n[4] Find the min of-\n[5] Find the product of-\nWhat will it be: "))
        except:
            print("That isn't something that I can do for you.")
        else:
            break # breaks loop 2

    if to_do == 1:
        to_use = number_picking()
        print(sum_of(to_use))

    elif to_do == 2:
        to_use = number_picking()
        print(average_of(to_use))

    elif to_do == 3:
        to_use = number_picking()
        print(max_of(to_do))

    elif to_do == 4:
        to_use = number_picking()
        print(min_of(to_use))

    elif to_do == 5:
        to_use = number_picking()
        print(product_of(to_use))

    else:
        print("Try again.")


    again = ""
    again = input("Would you like to go again? (y/n) :")
    if again == "y":
        print()
        continue
    else:
        break
