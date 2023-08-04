#Ask user their name. Remove whitespace from string. Capitalise users name
name = input("What's your name?: ").strip().title()
#Split users name into first/last names
first, last = name.split(" ")
#Print greeting
print(f"Hello, {first}")
