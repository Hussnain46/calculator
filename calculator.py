def calculator():
    try:
        num1 = int(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = int(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero."
        else:
            return "Invalid operation."
        
        return f"The result is: {result}"
    
    except ValueError:
        return "Invalid input. Please enter numerical values."

print(calculator())
