# Leap Year / An bisect
# divisible by 4
# not divisible by 100
# divisible by 400

year = int(input("Year = "))
cond = True  # condition = I supposed the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 1:
            cond = False

if year % 4 == 1:
    cond = False

if cond == True:
    print("Leap Year")
else:
    print("Not Leap")