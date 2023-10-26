#!/usr/bin/python

def main():
    car_info = { 
      str(input("What colour is your car?: "))
      } #store user input in variable car_info

    if is_dark(car_info): #pass the variable to is_dark function
        print("Insurance will be higher.")
    else:
        print("Insurance will be lower.")

def is_dark(colour): # set is_dark funnction with (d) parameter
    dark_colours = ["black", "dark"] #set criteria for the function to be True
    return any(dark_colour in colour.lower() for dark_colour in dark_colours) #conver user input to lower case

main()