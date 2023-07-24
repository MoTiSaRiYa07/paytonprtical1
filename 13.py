def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    num = int(input("Enter a number: "))
    result = check_odd_even(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
