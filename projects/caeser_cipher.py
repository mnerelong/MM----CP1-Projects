# MM, Period 1 Programming I, Caeser Cipher

letters= []
for i in range(97, 123): # for loop adding the letters to the list.
    letters.append(chr(i)) # I don't want to write it out myself.

# - - - - - - - - !
neo_letters = ""
for letter in letters:
    neo_letters += letter
print(neo_letters)
# - - - - - - - - !

def encode(raw, shift, key=letters):
    """This function will encode the given information."""
    encoded = []
    for char in raw:
        low_char = char.lower()

        if low_char in key:
            new_char = key[key.index(low_char) + shift]
            encoded.append(new_char)
    return encoded

def decode():
    """This function will decode the given information."""
    return

def joining(string):
    """This function will join lists into individual strings, which doesn't make sense because strings /are/ lists, right???"""
    new_string = ""
    for char in string:
        new_string += char
    print(new_string)
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
        user_shift = input("How much would you like to shift by?\n") # <------- SHOULD BE AN INTEGER, MAKE WHILE TRUE TRY & EXCEPT
        print(joining(encode(user_raw, 1, letters)))
