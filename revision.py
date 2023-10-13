#!/bin/python3

def main():
    name = input( "What is your name? " ).title().strip()
    print("Hello " + name, end=". ")
    print("How's the weather today?")

main()