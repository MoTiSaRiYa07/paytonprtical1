def check_number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

try:
    num = float(input("Enter a number: "))
    result = check_number_type(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
