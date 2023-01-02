# 1 year = 365, 1 year 52 weeks, 1 year = 12 months
age = int(input("What is your current age?\nMy age = "))

days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12
print(f"You have {days} days, {weeks} weeks, {months} months left until 90 years old.")

