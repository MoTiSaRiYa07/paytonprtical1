def check_divisibility_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

try:
    num = int(input("Enter a number: "))
    if check_divisibility_by_5(num):
        print(f"The number {num} is divisible by 5.")
    else:
        print(f"The number {num} is not divisible by 5.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
