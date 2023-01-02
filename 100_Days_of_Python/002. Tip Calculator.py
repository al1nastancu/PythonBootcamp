print("Welcome to the tip calculator.")

print("What was the total bill?")
bill = float(input("Your bill = "))

discount = int(input("What percentage tip would you like to give? 10, 12, 15: "))
people = int(input("How many people to split the bill: "))
tip = ((bill * (discount/100)) + bill) / people
print(f'Each person should pay $ {tip}') 