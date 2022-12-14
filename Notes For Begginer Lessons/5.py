x = 0

# create a while loop until it reaches 10

while x <= 10:
    x += 10
    print(x)

# for loop iterates 11 times
for i in range(0, 10):
    print(i)
for i in range(30):
    print("another way to write it.")

# if you want to break out of the loop
while x < 10:
    if x == 5:
        break
    x += 1
    print(x)

# to skip printing out the num 5 but print the rest
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

# lets you fill your code with a blank line
if x == 65:
    pass
# Endless while loop
while True:
    print("Endless loop")

