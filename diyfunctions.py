#Define the main part of the code
def main():
    #Ask user their name. Remove whitespace from string. Capitalise users name
    name = input("What's your name?: ")
    #use the function
    hello(name)



#Define your function. after "to" parameter, optional default value of "world"
def hello(to = "world"):
    #Define what your function does
    print("hello,", to)

#Call main at the end of the file
main()