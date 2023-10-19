#!/bin/bash

def main():
    car_info = { 
    colour : str(input("What colour is your car?: "))
    }

    if is_dark(x):
        print("Insurance will be higher.")
    else:
        print("Insurance will be lower.")

def is_dark(d):
    dark_colours = ["black", "dark"]
    return any(dark_colour in d.lower() for dark_colour in dark_colours)