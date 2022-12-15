# you can add any type of value to list
myList = [2, 5, 6, 6, "text", False, 3.33]

# access third value
print(myList[2])

# slice list values
print(myList[1:3])

# start from first value
print(myList[:3])

# access from right to left
print(myList[-2])

# replace value in list
myList[2] = "it is not a string"

# iterate through whole list
for i in myList:
    print(i)

L1 = [1, 2, 3]
L2 = [4, 5, 6]

# adding lists together
print(L1 + L2)

# making a list four times
print(L1 * 4)

# tells how long the list is
print(len(L1))

# output the max value in the list can only use for int/float
print(max(L1))

# output the minimum value in the list can only use for int
print(min(L1))

# appends one value to the end of the list
L1.append("yes")

# insert a new value to the list at a specific index
L1.insert(2, "new value")

# remove a value that is in the list
L1.remove("value")

# remove a value at a specific index
L1.pop(3)

# gives the index of a value
L1.index(1)

# a useful way to use the funcs
L1.pop(L1.index(1))

# it sorts a list
L1.sort()

# another way to write this without changing the list
print(sorted(list))

# outputs the bool of wheter something is in a list
print(2 in L1)
print((5 not in L1))

# can't modify values in tuple but can access them
x = (1, 2, 3)
print(x[2])

# can change values by making it a list
x = list(x)
x[1] = 5
x = tuple(x)

# dictionary
fruits = {'color': 'green', 'sweet': 'yes', 'tree': 'yes', 'age': 23, True: 45}
print(fruits['color'])
print(fruits[True])

# create a new key-value pair
fruits['height'] = 44

# returns a dict of all items
print(fruits.items())

# returns all the values
print(fruits.values())

# print the keys of a dict
print(fruits.keys())

# prints whether something is a type of value
y = 13
if y is int:
    print("yes")
else:
    print("no")