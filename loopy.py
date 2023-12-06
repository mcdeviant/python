#!/usr/bin/python

print("meow\n" * 3, end="")

#or

while True:
    n = int(input("How many times did the cat meow? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#or

def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()