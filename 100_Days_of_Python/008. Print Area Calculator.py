def paint_calculator(height, width, coverage):
    print(f"Number of cans will be: {(height * width) / coverage}")

h = int(input("Height = "))
w = int(input("Width = "))
c = int(input("Coverage = "))

paint_calculator(h, w, c)
