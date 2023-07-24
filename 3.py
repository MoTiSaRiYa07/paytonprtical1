import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    try:
        # Get input from the user
        radius = float(input("Enter the radius of the circle: "))
        
        # Calculate the area using the function
        area = calculate_circle_area(radius)
        
        # Display the area
        print("The area of the circle with radius {} is: {:.2f}".format(radius, area))
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
