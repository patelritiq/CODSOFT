while True:
    print("\n!!!---------- Arithmetic Calculator ----------!!!")
    print("Please select an arithmetic operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")
    print("6. Integer Division (//)")

    operation_choice = input("Enter the number corresponding to your choice (1-6): ").strip()

    valid_choices = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%", "6": "//"}

    if operation_choice not in valid_choices:
        print("Invalid choice. Please select a number between 1 and 6.")
        continue

    operator = valid_choices[operation_choice]
    operation_names = {
        "+": "addition",
        "-": "subtraction",
        "*": "multiplication",
        "/": "division",
        "%": "modulo",
        "//": "integer division",
    }

    try:
        first_value = float(input("Enter the first number: ").strip())
        second_value = float(input("Enter the second number: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    try:
        if operator == "+":
            result = first_value + second_value
        elif operator == "-":
            result = first_value - second_value
        elif operator == "*":
            result = first_value * second_value
        elif operator == "/":
            result = first_value / second_value
        elif operator == "%":
            result = first_value % second_value
        elif operator == "//":
            result = first_value // second_value
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        continue

    print(f"The result of the {operation_names[operator]} is: {result}")
    print("====================================================================")

    choice = input("Press 'q' to quit or any other key to continue: ").strip().lower()
    if choice == "q":
        break
