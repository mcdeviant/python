#!/usr/bin/python3

def main(): 
    
    car_info = {
        "colour": str(input("What colour is your car?: ")), #store  colour input in variable car_info
        "make": str(input("What make is your car?: ")), #Store make input in variable car_info["colour"]- and now car_info is a tuple
        }
    car_info["model"] = str(input(f"What model is your {car_info['make']}?: "))

    if is_dark(car_info["colour"]): #pass the variable to is_dark function
        print(f"Insurance will be higher for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")
    else:
        print(f"Insurance will be lower for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")

def is_dark(colour): # set is_dark funnction with (colour) parameter
    dark_colours = ["black", "dark"] #set criteria for the function to be True
    return any(dark_colour in colour.lower() for dark_colour in dark_colours) #convert user input to lower case

main()