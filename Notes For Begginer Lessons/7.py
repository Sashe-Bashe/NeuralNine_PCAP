# a function
def helloWorld():
    print("hello world")


helloWorld()


# pass values to func
def adding(x=0, y=0):  # set to 0 if no parameter is passed
    print(x + y)
    return x + y


adding(4, 5)
result = adding(30, 5)


def sumOF(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result


print(sumOF(10, 50, 50, 60))
