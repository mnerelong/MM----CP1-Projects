
        user_range = int(input("How big dya want your multiplication table?\n"))
    except:
        print("...Sorry... it has to be a number. It's multiplication?")
    else:
      #  if user_range >= 38:
           # print("Uhm... Actually... That number is too big... :(")
        #else:
            break

for i in range(1, user_range + 1): # +1 so that it includes the chosen number
    for x in range(1,user_range + 1):
        print(x * i, end="\t")
    print("\n\n")
    