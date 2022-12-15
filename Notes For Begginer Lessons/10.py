text = "This is cool"

print(len(text))  # gets the length of the string

print(text[2])  # gets 2nd index value

print(text[4:])  # you can also slice strings

# iterate through letters in string
for letter in text:
    print(letter)

# puts the text after on a new line, basically a line break and also create a tab space with \t
print("create a \t Tab")
print("Create a \n new line")

name = "Joe"
age = 55
# %s is used for strings and %d is used for data types using tuple
print("My name is %s and I am %d" % (name, age))
print("My name is {} and I am {}".format(name, age))

# case manipulation functions
example = "This is my text. I like my text"
example = example.upper()  # transforms the whole to text to lowercase
example = example.lower()  # transforms text to be all lower
example = example.title()  # capitalizes every word
example = example.swapcase()  # it swaps the case of the letter meaning from upper case to lower for each letter
example = example.count("my")  # counts how many times a substring is a in a string, so my and text occur two times
example = example.find("text")  # finds the starting position of a string, index

seperator = ":"
print(seperator.join(example))
print(example.split('a'))  # splits the text where a is in it
print(example.replace("like", "love"))  # replaces the string with another string specified
