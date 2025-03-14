while True:
    try:
        first_number = input("Enter the first number (or type 'exit' to quit): ")
        if first_number.lower() == 'exit':
            break
        second_number = input("Enter the second number (or type 'exit' to quit): ")
        if second_number.lower() == 'exit':
            break
        operation = input("Enter the operation (+, -, *, /) or type 'exit' to quit: ")
        if operation.lower() == 'exit':
            break

        
        number_1 = float(first_number)
        number_2 = float(second_number)

        if operation == '+':
            result = number_1 + number_2
        elif operation == '-':
            result = number_1 - number_2
        elif operation == '*':
            result = number_1 * number_2
        elif operation == '/':
            if number_2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = number_1 / number_2
        else:
            print("Invalid operation. Please enter one of these: +, -, * or /.")
            continue

        print(f"{number_1} {operation} {number_2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
