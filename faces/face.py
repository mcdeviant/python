#!/bin/python

def main():

    #convert input to string, store in variable
    STRING = str(input())
    #call convert on the above variable
    RESULT = convert(STRING)

#Converts emoticons to emojis
def convert(STRING):
    SMILE = STRING.replace(":)","\\U0001F642")
    FROWN = STRING.replace(":(","\\1F641")
    return STRING
convert()

main()