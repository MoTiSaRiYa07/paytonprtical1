def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def multiply_numbers(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform operations
        sum_result = add_numbers(num1, num2)
        difference_result = subtract_numbers(num1, num2)
        division_result = divide_numbers(num1, num2)
        multiplication_result = multiply_numbers(num1, num2)
        
        # Display the results
        print("Sum: {:.2f}".format(sum_result))
        print("Difference: {:.2f}".format(difference_result))
        print("Division: {:.2f}".format(division_result))
        print("Multiplication: {:.2f}".format(multiplication_result))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
