# zero division error
print(2/0)

# allows program to continue and prints what is in except if error is found and also does finally something if everything fails
x = 2
y = 0
# this is usally good for streams
try:
    print(x/y)
except:
    print("can't do that")
finally:
    print("Done")
# can also do specific error
except ValueError:
    print("please enter a correct value")
except ZeroDivisionError:
    print("cannot divide by zero")

# How to raise your own Exception
def someFunc():
    if True:
        raise Exception("Some error occured")
        raise ValueError("Some value is wrong")
someFunc()

# how to force an untrue statement to true, demand it
x = 30
y = 20

assert(x < y)
