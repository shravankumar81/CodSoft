def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Cannot modulo by zero"

def exponent(a, b):
    return a ** b

def calculator():
    operations = {
        1: add,
        2: sub,
        3: mul,
        4: div,
        5: modulo,
        6: exponent
    }

    while True:
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulo Division\n6. Exponent\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Program exited!")
            break

        if choice in operations:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            result = operations[choice](a, b)
            print(f"Result: {result}")
        else:
            print("Enter a valid choice!")

calculator()
