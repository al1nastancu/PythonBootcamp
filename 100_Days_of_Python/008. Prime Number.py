def prime_checker(number):
    check = True  # is prime
    for i in range(2, int(number / 2)):
        if number % i == 0:
            check = False
    if check == True:
        print(f"{number} is prime.")
    else:
        print(f"{number} is NOT prime.")

prime_checker(int(input("Check the number = ")))
