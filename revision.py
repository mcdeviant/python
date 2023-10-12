#!/bin/python3

def main():
    entry = input( "What is your name? " )
    name = entry.title()
    print("Hello " + name, end=". ")
    print("How's the weather today?")

main()