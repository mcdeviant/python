#!/usr/bin/python

def main():
    car_info = { 
      "colour": str(input("What colour is your car?: ")),
      } #store user input in variable car_info

    if is_dark(car_info["colour"]): #pass the variable to is_dark function
        print(f"Insurance will be higher for your {car_info['colour']} car.")
    else:
        print(f"Insurance will be lower for your {car_info['colour']} car.")

def is_dark(colour): # set is_dark funnction with (colour) parameter
    dark_colours = ["black", "dark"] #set criteria for the function to be True
    return any(dark_colour in colour.lower() for dark_colour in dark_colours) #convert user input to lower case

main()