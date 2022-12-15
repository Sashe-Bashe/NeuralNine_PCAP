# imports os module
from os import *
# file operators
# w for write, r for read, a for appending
file = open("myfile.txt", "w")  # writing to a file that doesn't exist make a new file

# closing the file stream and flushes/closes it
file.close()
file.flush()  # flushes the stream but the file is still open
# if you don't wnat to manually close a file

with open('myfile.txt', "r") as f:  # reading a file that doesn't exist fails
    content = f.read()
    f.write("Hello world")
print(content)
mkdir("test") # makes a directory named test aka folder
chdir("Test") # inside of folder
rename("da.txt")
remove("ja.txt")
