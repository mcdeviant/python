#!/usr/bin/python3

#I wasn't happy with my function understanding, and wanted to revise it, so made this to practice. 
#It's like an insurance filter. If you enter a colour with "dark" or "black", or a fancy make of car from the list,
# it will warn of higher interest. 


def main(): 
    
    car_info = {
        "colour": str(input("What colour is your car?: ")), #Store key "colour" and value (user input) in dictionary "car_info".
        "make": str(input("What make is your car?: ")), #Store key "make" and value (user input) in dictionary "car_info".
        }
    car_info["model"] = str(input(f"What model is your {car_info['make']}?: ")) #References the 'make', so I had to complete/close the previous dictionary assignments.

    if is_dark(car_info["colour"]) or is_rich(car_info["make"]): #pass the variable to is_dark function
        print(f"Insurance will be higher for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")
    else:
        print(f"Insurance will be lower for your {car_info['colour']}, {car_info['make']}, {car_info['model']}.")

def is_dark(colour): # set is_dark function with (colour) parameter
    dark_colours = ["black", "dark"] #set criteria for the bool function to be True
    return any(dark_colour in colour.lower() for dark_colour in dark_colours) #convert user input to lower case to ensure match with criteria above

def is_rich(make): # set is_rich function with (make) parameter
    rich_models = ["mercedes", "bmw", "lexus", "aston martin", "ferrari", "porsche", "lamborghini", "tesla"] #set car models for bool function to be True
    return any(rich_model in make.lower() for rich_model in rich_models) #convert the user input to lower case to ensure match

main()