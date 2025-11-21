logo = """
  _____________________
 /  _________________  \\
|  |                 |  |
|  |_________________|  |
|  _________________    |
| | 7 | 8 | 9 | ÷ |    |
| |---+---+---+---|    |
| | 4 | 5 | 6 | × |    |
| |---+---+---+---|    |
| | 1 | 2 | 3 | − |    |
| |---+---+---+---|    |
| | 0 | . | = | + |    |
| |_________________|  |
 \\_____________________/
"""


def add(num1, num2):
    """After receiving two numbers from the user, It adds them."""
    return num1 + num2


def subtract(num1, num2):
    """After receiving two numbers from the user, It subtracts them."""
    return num1 - num2


def multiply(num1, num2):
    """After receiving two numbers from the user, It multiplies them."""
    return num1 * num2


def divide(num1, num2):
    """After receiving two numbers from the user, It divides them."""
    return num1 / num2


arthemetic_operation = {
    "+": add,
    "-": subtract,
    "*":  multiply,
    "/":  divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter first number:\n>>>"))
    continues = True
    while continues:
        for operation in arthemetic_operation:
            print(operation)

        operation_symbol = input("Pick an operation:\n>>>")
        num2 = float(input("Enter next number:\n>>>"))

        calculation = arthemetic_operation[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_or_stop = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n>>> ")
        if continue_or_stop == 'y':
            num1 = answer
        else:
            continues = False
            calculator()


calculator()
