def calculate_average(num1, num2):
    return (num1 + num2) / 2

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the average using the function
        average = calculate_average(num1, num2)

        # Display the average
        print("The average of {} and {} is: {:.2f}".format(num1, num2, average))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
