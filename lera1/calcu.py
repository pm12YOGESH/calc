# Simple calculator

while True:
    print("Operations: +, -, *, /")
    op = input("Choose an operation: ")

    if op in ("+", "-", "*", "/"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: division by zero")
                continue
            result = num1 / num2

        print(f"Result: {result}")
    else:
        print("Invalid operation")

    again = input("Do you want to calculate again? (y/n): ").lower()
    if again != "y":
        break
