def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the rate of interest (per annum): "))
        time = float(input("Enter the time period (in years): "))

        # Calculate simple and compound interest
        simple_interest = calculate_simple_interest(principal, rate, time)
        compound_interest = calculate_compound_interest(principal, rate, time)

        # Display the results
        print("\nSimple Interest: {:.2f}".format(simple_interest))
        print("Compound Interest: {:.2f}".format(compound_interest))
    except ValueError:
        print("Invalid input. Please enter valid numbers for the principal amount, rate of interest, and time period.")
