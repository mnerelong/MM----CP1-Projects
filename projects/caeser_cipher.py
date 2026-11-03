# MM, Period 1 Programming I, Caeser Cipher

while True: # loop 1 <-----
    while True: # loop 2 <-----
        try:
            e_or_d = int(input("encode (1) decode (2)\n"))
        except:
            print("invalid input!")
        else:
            if e_or_d == 1 or e_or_d == 2:
                break # loop 2
            else:
                print("invalid input.")
                continue # loop 2