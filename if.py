x = int(input("What is x? "))
y = int(input("What is y? "))


if x > y :
    print(f"x ({x}) is greater than y ({y}).")
elif x == y :
    print(f"x ({x}) is equal to y ({y})")
elif x < y and x > 0 :
    print(f"x ({x}) is between 0 and y ({y}).")
else:
    print(f"x ({x}) is less than or equal to 0.")