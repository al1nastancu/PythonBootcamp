height = float(input("Your height in m = "))
weight = float(input("Your weight in kg = "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obese")
elif bmi > 35:
    print("Clinically obese")