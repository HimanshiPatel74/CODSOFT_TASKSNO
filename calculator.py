num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result =", num1 + num2)

elif operation == "-":
    print("Result =", num1 - num2)

elif operation == "*":
    print("Result =", num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not possible.")

else:
    print("Invalid operation.")