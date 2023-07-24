def find_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    return dividend % divisor

if __name__ == "__main__":
    try:
        dividend = int(input("Enter the dividend (natural number): "))
        divisor = int(input("Enter the divisor (natural number): "))

        # Calculate the remainder using the function
        remainder = find_remainder(dividend, divisor)

        # Display the remainder
        print("The remainder of {} divided by {} is: {}".format(dividend, divisor, remainder))
    except ValueError:
        print("Invalid input. Please enter valid natural numbers for the dividend and divisor.")
