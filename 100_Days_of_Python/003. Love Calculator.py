print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

new_name = name1 + name2
new_name = new_name.lower()

p1 = new_name.count('t') + new_name.count('r') + new_name.count('u') + new_name.count('e')
p2 = new_name.count('l') + new_name.count('o') + new_name.count('v') + new_name.count('e')

print(f"You are a match of {p1}{p2}%. Cool! (I guess!)")
