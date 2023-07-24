def find_max_number(num1, num2, num3):
    return max(num1, num2, num3)

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    max_number = find_max_number(num1, num2, num3)
    print(f"The maximum number among {num1}, {num2}, and {num3} is: {max_number}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
