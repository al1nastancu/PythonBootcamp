print("Welcome to Python Pizza Deliveries!")
size = input("What pizza size do you want? S, M, L\nAnswer = ")
add_peperoni = input("Do you want peperoni?  Y / N \nAnswer = ")
extra_cheese = input("Do you want extra cheese?  Y / N\nAnswer = ")

if size == 'S':
    cost = 15
elif size == 'M':
    cost = 20
else:
    cost = 25

if add_peperoni == 'Y':
    cost += 2
if extra_cheese == 'Y':
    cost += 3

cost += 1  # package

print(f'Your final bill is: {cost}')