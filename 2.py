# Function to add two numbers and return the sum
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calculate the sum using the function
        result = add_numbers(num1, num2)
        
        # Display the sum
        print("The sum of {} and {} is: {}".format(num1, num2, result))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
