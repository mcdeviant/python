#!/usr/bin/python3

#Creates a function to convert emoticons to emojis
def convert(input_string):
    #Stores the replacement for :) into "smile" variable
    smile = (input_string.replace(":)","\U0001F642"))
    #Adds the :( conversion and stores it all in the "frown" variable
    frown = (smile.replace(":(","\U0001F641"))
    #When the function is called, this tells it to return the "frown" variable
    return frown
    
def main():
    #convert input to string, store in "input_string" variable
    input_string = str(input())
    #call convert on the above variable, store in "result" variable
    result = convert(input_string)
    print(result)

main()