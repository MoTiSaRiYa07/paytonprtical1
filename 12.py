import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

try:
    radius = float(input("Enter the radius of the sphere: "))
    if radius < 0:
        print("Radius cannot be negative.")
    else:
        volume = sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} is {volume:.2f} cubic units.")
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")
