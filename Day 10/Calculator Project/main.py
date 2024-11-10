from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    run = True

    number1 = float(input("What is the first number? "))

    while run:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        number2 = float(input("What is the next number? "))

        result = operations[operation](number1, number2)

        print(f"{number1} {operation} {number2} = {result}")
        go_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if go_again == "y":
            number1 = result
        else:
            run = False
            print("\n" * 20)
            calculator()

calculator()