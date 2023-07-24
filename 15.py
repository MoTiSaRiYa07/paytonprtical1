def check_equality(num1, num2):
    if num1 == num2:
        return True
    else:
        return False

try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if check_equality(num1, num2):
        print("The two integers are equal.")
    else:
        print("The two integers are not equal.")
except ValueError:
    print("Invalid input. Please enter valid integers.")
