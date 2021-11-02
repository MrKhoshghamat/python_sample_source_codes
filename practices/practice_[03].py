"""
It is a program to calculate the area and the volume of a sphere
by getting a radial from input via their own functions
"""

# Import math module to define pi value and calculate the power
# of a value
import math

# Define a global variable as a pi to define 3.14 to use in
# functions
pi = math.pi


# Define a function to calculate the area of the sphere with it's
# own formula via getting a radial from input
def sphere_area(radial):
    # The formula of calculating the area of the sphere
    area = 4 * (pi * pow(radial, 2))
    return area


# Define a function to calculate the volume of the sphere with
# it's own formula via getting a radial from input
def sphere_volume(radial):
    # The formula of calculating the volume of the sphere
    volume = (4 / 3) * (pi * pow(radial, 3))
    return volume


# Using Try Exception to avoid getting value error like getting
# string instead of integer or float value
try:

    # Define a variable to get the radial of the sphere and convert
    # it to float
    sphere_radial = float(input("Please Enter the Sphere Radial : "))

    # Define a variable to get the output of the sphere_area
    # function
    sphere_area = sphere_area(sphere_radial)

    # Define a variable to get the output of the sphere_volume
    # function
    sphere_volume = sphere_volume(sphere_radial)

    # Print the results
    print(f"\nThe Sphere Radial is : {sphere_radial} mm\n"
          f"The Sphere Area is : {sphere_area} mm^2\n"
          f"The Sphere Volume is : {sphere_volume} mm^3")

# Value error Exception to Print a text instead of getting
# error
except ValueError:
    print("\nPlease Enter a Valid Integer or Float Value")
