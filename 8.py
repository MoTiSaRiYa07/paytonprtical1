# Swap values using a temporary (third) variable
def swap_with_temp_variable(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Swap values without using a temporary (third) variable
def swap_without_temp_variable(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == "__main__":
    try:
        # Get input from the user
        num1 = float(input("Enter the first number (a): "))
        num2 = float(input("Enter the second number (b): "))

        # Swap values using a temporary variable
        temp_swapped_num1, temp_swapped_num2 = swap_with_temp_variable(num1, num2)

        # Swap values without using a temporary variable
        non_temp_swapped_num1, non_temp_swapped_num2 = swap_without_temp_variable(num1, num2)

        # Display the results
        print("\nUsing a temporary variable:")
        print("Swapped a: {:.2f}, Swapped b: {:.2f}".format(temp_swapped_num1, temp_swapped_num2))

        print("\nWithout using a temporary variable:")
        print("Swapped a: {:.2f}, Swapped b: {:.2f}".format(non_temp_swapped_num1, non_temp_swapped_num2))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
