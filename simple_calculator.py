# simple_calculator.py

def main():
    # 1. Ask the user for two numbers
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")

    # Basic check to see if the inputs are numbers
    # Note: replace(".") allows us to check for floating-point decimals like "5.5"
    if not (num1_input.replace(".", "", 1).isdigit() and num2_input.replace(".", "", 1).isdigit()):
        print("Error: Invalid numeric input. Please enter valid numbers.")
        return

    # Convert valid inputs to floats to handle both integers and decimals
    num1 = float(num1_input)
    num2 = float(num2_input)

    # 2. Ask the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ")

    # 3. Perform the calculation using if-elif-else
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # Handle division by zero error gracefully
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        # Handle unsupported operations[cite: 3]
        print(f"Error: '{operation}' is an unsupported operation symbol.")
        return

    # Clean up display if numbers are whole integers (e.g., 7.0 -> 7)
    display_num1 = int(num1) if num1.is_integer() else num1
    display_num2 = int(num2) if num2.is_integer() else num2
    display_result = int(result) if isinstance(result, float) and result.is_integer() else result

    # 4. Print the result in a user-friendly way
    print(f"{display_num1} {operation} {display_num2} = {display_result}")


if __name__ == "__main__":
    main()
    ## https://github.com/JorgeMarroquinCorzo/ALAB-315-2-Part-2.git