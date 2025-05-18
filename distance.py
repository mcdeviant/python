#!/usr/bin/python3

def main():
    miles = miles_input(input("Enter number of miles to convert: "))
    kms = kms_out(miles * 1.6)
    print(f"{miles:.2f} miles = {kms:.2f} kilometers")

def miles_input(m):
    return int(float(m))

def kms_out(k):
    return (float(k))

main()