#function that takes arguments
def func1(arg1, arg2):
    print(arg1, " ", arg2)

#function that return a value
def cube(x):
    return x*x*x

#function with variable number of arguments
def power(num, x=1):
    result = 1
    for i in range(x):
        result*=num
    return result

#using the enumerate() function
def mydays():
    offdays=["Mon", "Wed"]
    for i,d in enumerate(offdays):
        print (i, " ", d)

print (power(2))
print (power(2,4))
print (power(x=3, num=2))   
print (mydays())