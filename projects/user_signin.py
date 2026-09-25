# Meika Milton, 1st period Programming I, User Signin

#user_list = [["xXerratic_PUSLEXx", "IHATE_FAM1LY"], ["sis_M00n", "b1tt3rA3rie"], ["_X-SIGNIFICANT-HARASSMENT6969-X_", "BOII1I"], ["7red_son-s", "R0TP3BBLES"]]
user_list = ["xXerratic_PUSLEXx", "sis_M00n", "_X-SIGNIFICANT-HARASSMENT6969-X_", "7red_son-s", "4-ease"]
password_list = ["IHATE_FAM1LY", "b1tt3rA3rie", "BOII1I", "R0TP3BBLES", "4"]
signup = "0"
count = 0

while True: # username loop,
    if count > 16: # forces the user to go to the password section for... little to no reason other than that I think it's annoying of them to never get the username right yet refuse to make a new.
        user = "4-ease"
        print("\tOkay, I give up.\nThe password is 4.\n\tDon't mess it up.\n")
        break
    user = input("What is your username?\n")
    count += 1 # counts up to skipping to the password section.
    if user in user_list:
        break
    elif not user: # so that the user cannot enter nothing as a username.
        print("??? Just why.")
    else:
        print("Try again.")
        if (count % 2) == 0: # I don't want the code to keep repeating this EVERY SINGLE TIME the username is wrong. it kinda bothers me I dunno.
            print("Uhhhh... okay I have no idea who you are. Do you want to create an account? (y/n)")
            signup = input().lower()
            if signup == "y":
                user = input("What's your username of choice?\n")
                user_list.append(user)
                password = input("Whats the paassssword??\n")
                password_list.append(password)

        else:
            continue

while True:
    password = input("Whats the PASSWORD?\n")
    if password in password_list and password_list.index(password) == user_list.index(user):
        print(f"\nWelcome, {user}!")
        break
    else:
        print("No... try again.")

    #user = input("What is your username?")