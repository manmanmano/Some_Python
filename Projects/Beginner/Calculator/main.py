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
    "/": divide
}


def calculator():
    print("\n", logo, "\n")
    n1 = float(input("What is the first number? "))
    should_continue = True
    while should_continue:
        n2 = float(input("What is the next number? "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        calculation = operations[operation_symbol]
        result = calculation(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {result}")

        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' for a new calculation, and else to exit: ").lower()
        if answer == "y":
            n1 = result
        elif answer == "n":
            should_continue = False
            calculator()
        else:
            exit("Goodbye!")


calculator()
