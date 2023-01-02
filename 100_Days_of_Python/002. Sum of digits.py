# Write a program that adds the digits in a 2 digit number

# Method 1
number = int(input("Your number = "))
print("Sum of digits = ", int(number % 10 + number / 10))

# Method 2
number = input("Your number = ")
print("Sum of digits = ", int(number[0]) + int(number[1]))