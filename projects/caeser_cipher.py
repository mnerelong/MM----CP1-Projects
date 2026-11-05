# MM, Period 1 Programming I, Caeser Cipher

e_or_d = 0
user_raw = "nanometers"
user_shift = 0

def encode(raw, shift=1):
    """This function will encode the given information."""
    encoded = []
    for char in raw: 
        if not char.isalpha():
            encoded.append(str(char))
            continue
        new_char = chr(ord(char) + shift) # BIG PROBLEM!! BIG PROBLEM!!! DOESN'T WRAP D: <----------------------------------------------- !!EMERGENCY!!! BREAKING NEWS!!! !!!!!!!!!!
        encoded.append(new_char)

    return encoded

def decode(raw, shift):
    """This function will decode the given information."""
    decoded = []
    if not shift:
        for i in range(1, 25):
            new_decoded = for_decode(raw, i, decoded)
            print(*new_decoded)
            new_decoded = []
    else:
        for_decode(raw, shift, decoded)
    return new_decoded

def for_decode(raw, shift, new_list):
    for char in raw:
        if not char.isalpha():
            new_list.append(str(char))
            continue
        new_char = chr(ord(char) - shift)
        new_list.append(new_char)
    return new_list

def joining(string):
    """This function will join lists into individual strings, which doesn't make sense because strings /are/ lists, right???"""
    new_string = ""
    for char in string:
        new_string += char

    return new_string



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
    if e_or_d == 1:
        user_raw = input("Type what you would like to encode.\n")
        while True: # loop 3 <-----
            try:
                user_shift = int(input("How much would you like to shift by?\n"))
            except:
                print("A number, please.")
            else:
                break # loop 3
#                 2       1                                            separate functions marked
        print(joining(encode(user_raw, user_shift)))
    elif e_or_d == 2:
        user_raw = input("Type what you would like to decode.\n")
        while True: # loop 4 <-----
            try:
                user_shift = int(input("Do you know what the shift is?\n(If not, enter 0)"))
            except:
                print("A number, PLEAAASE!!")
            else:
                break # loop 4
#                 2       1                                            separate functions marked
        print(joining(decode(user_raw, user_shift)))
