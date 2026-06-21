# Smart Calculator with History using Python

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Cannot divide by zero."

def percentage(a, b):
    return (a / b) * 100

while True:
    print("\n===== SMART CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. View History")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "6":
        print("\n--- Calculation History ---")
        if len(history) == 0:
            print("No history available.")
        else:
            for item in history:
                print(item)
        continue

    elif choice == "7":
        print("Thank you for using Smart Calculator!")
        break

    elif choice in ["1", "2", "3", "4", "5"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            elif choice == "5":
                result = percentage(num1, num2)
                operation = f"({num1}/{num2}) * 100 = {result}%"

            print("Result:", result)
            history.append(operation)

        except ValueError:
            print("Invalid Input! Please enter numbers only.")

    else:
        print("Invalid Choice! Please select between 1 and 7.")
