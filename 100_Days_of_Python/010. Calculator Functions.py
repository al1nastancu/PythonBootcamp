def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("---> Invalid Operation!")


operations = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide,
}

def calculator():
    number_1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(number_1, number_2)

        print(f'{number_1} {operation_symbol} {number_2} = {answer}')

        if input(f"More calculations with {answer} ?\nType 'yes' if so, or 'c' to clear and start over: ").lower() == 'yes':
            number_1 = answer
        else:
            should_continue = False
            print("\nGood, let's make some new calculations!")
            calculator()

calculator()
