def greet(name):
    print(f"Hello, {name}!")
    print(f"How are you today, {name}?")
    print(f"Have a good day, {name}!")

greet(input("Name: "))

def greet_with(name, location):
    print(f"Hello, {name}, are you going to {location}?")

greet_with(input("Name: "), input("Location: "))