#Define your function. after "to", optional default argument of "world"
def hello(to = "world"):
    #Define what your function does
    print("hello,", to)
#Hello function with no argument, will use the default in line 1
hello()
#Ask user their name. Remove whitespace from string. Capitalise users name
name = input("What's your name?: ")
#use the function
hello(name)