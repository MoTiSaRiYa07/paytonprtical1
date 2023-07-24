def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    # Check for divisors starting from 3 up to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

try:
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"The number {num} is a prime number.")
    else:
        print(f"The number {num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
