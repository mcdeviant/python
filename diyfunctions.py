#!/usr/bin/python3

#Define the main part of the code/function
def main():
    #prompt for input
    name = input("What's your name?: ")
    #use the function
    hello(name)



#Define your function. after "to" parameter, optional default value of "world"
def hello(to = "world"):
    #Define what your function does
    print("hello,", to)

#Call main at the end of the file
main()