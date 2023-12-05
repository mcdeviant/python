#!/usr/bin/python3
#Not a guided lesson, just practicing. 
def main(): 
    
    car_info = {
        "colour": str(input("What colour is your car?: ")), #Store key "colour" and value (user input) in dictionary "car_info".
        "make": str(input("What make is your car?: ")), #Store key "make" and value (user input) in dictionary "car_info". Doesn't do anything, just an example/test.
        }
    car_info["model"] = str(input(f"What model is your {car_info['make']}?: ")) #References the 'make', so I had to complete/close the previous dictionary assignments.

    if is_dark(car_info["colour"]): #pass the variable to is_dark function.
        print(f"Insurance will be higher for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")
    else:
        print(f"Insurance will be lower for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")

def is_dark(colour): # set is_dark funnction with (colour) parameter.
    dark_colours = ["black", "dark"] #set criteria for the function to be True.
    return any(dark_colour in colour.lower() for dark_colour in dark_colours) #convert user input to lower case.

main()

