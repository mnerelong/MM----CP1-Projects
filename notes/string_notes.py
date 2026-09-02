# Meika Milton, 1st period Programming I, Stirng Notes

#------------------- STRINGS: are a collection of characters held together by quotation marks. "ex"
string = "I am a string"
numbers = "can be strings too."
example = "411"
you = "Can't do math with that number. Try adding it to something, I dare you."
#try to convert?
print(example + " + 2")
#             ^ concatonation or whatever
#------------------- DEF: adding one string directly to the end of another
#ex:
print("This print statement" + " has been concatonated.") # need to add spaces individually.

first_name = 'Five'
last_name = 'Pebbles' # You can do this I guess.
full_name = first_name + " " + last_name
print(f"ITS {full_name.upper()}!!!!!!!!!!!")

#------------------- ESCAPE CHARACTER
#tells the computer to ignore whatever the next character is.
print(f'And Sliver of Straw finally said\n\t"it\'s triple affirmative time."')
#                                            ^ escape char to make sure the apostraphe doesnt mess with the string
# \n skips yo next line. \t tabs over the line.

#------------------- PRINTING STRINGS MULTIPLE TIMES
print("THE RAIN IS COMING " * 3) #all on the same line. need \n
#                            ^ probably the only math thing you can do to strings other than add (concatonate?)


#------------------- I'M SCARED BUT REALLY IMPORTANT -------------------
sentence = "Unparalleled Innocence? More like unparalleled CHUD!!!"
sentence_2 = "TRIPLE AFFIRMATIVES"
print(sentence)
print(sentence.find("e"))
# starts at 0   ^ finds the # location of the first appearance of a specific character.
# is at INDEX 24

#------------------- CUTTING STRINGS
print(sentence[47:54])
#                ^ oh god oh god oh god
# way easier?                                                 v so that we can keep the S
print(sentence_2[sentence_2.find("A"):sentence_2.find("S") + 1])
#                    this is just horrible how do I even explain this
# finds everything inbetween (and including) A and S and prints it

word = "TRIPLE"
start = (sentence_2.find(word))
length = len(word)
print(sentence_2[start:start + length])
#ok you figure it out