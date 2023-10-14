x = int(input("What is x? "))
y = int(input("What is y? "))

if ( x < y ) and ( x > 0 ):
    print(f"x is between 0 and {y} - y.")
elif ( x > y ) or ( x < 0 ):
    print(f"x is greater than {y} - y, or less than 0.")
else:
    print( "x is equal to y or 0.")