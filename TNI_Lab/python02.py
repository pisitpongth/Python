def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("[+] [-] [*] [/]")
operation = input("Enter the operation: ")

if operation == "+":
    result = plus(a, b)
elif operation == "-":
    result = minus(a, b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)

print(f"The result of {a} {operation} {b} is: {result}")
