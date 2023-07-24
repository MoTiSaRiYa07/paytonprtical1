def evaluate_expression(expression, a, b, x, y):
    # Define the variables in the expression
    variables = {'a': a, 'b': b, 'x': x, 'y': y}

    # Evaluate the expression
    result = eval(expression, variables)
    return result

if __name__ == "__main__":
    try:
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
        x = float(input("Enter the value of 'x': "))
        y = float(input("Enter the value of 'y': "))

        # Evaluate each equation
        equations = [
            "x + y*z",
            "x*y + a*b**2",
            "a**2 + 2*a*b + b**2",
            "a**2 - 2*a*b + b**2",
            "(a - b)*(a + b)",
            "a**3 + b**3 + 3*a*b*(a + b)",
            "a**3 - b**3 - 3*a*b*(a - b)",
            "(a - b)*(a**2 + a*b + b**2)",
            "(a + b)*(a**2 - a*b + b**2)",
            "3*x*y**3 + 9*x**2*y**3 + 5*y**3*x"
        ]

        for i, equation in enumerate(equations, start=1):
            result = evaluate_expression(equation, a, b, x, y)
            print("Result of equation {} (Expression: {}): {}".format(i, equation, result))

    except ValueError:
        print("Invalid input. Please enter valid numbers for 'a', 'b', 'x', and 'y'.")
