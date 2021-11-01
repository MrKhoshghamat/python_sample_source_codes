"""
It is a program to calculate are and volume of a cylinder via
their own functions
"""

# Import math module to define pi value and calculate the power
# of a value
import math


# Define a function to get radial as input and calculate the area
# of cylinder area via it's own formula
def cylinder_area(radial):
    # Using math.pi module to define 3.14
    pi = math.pi

    # The formula of calculating the area of a circle via pi and pow
    area = pi * (pow(radial, 2))
    return area


# Define a function to get area and height as input then
# calculate the volume of the cylinder via it's own formula
def cylinder_volume(area, height):
    # The formula of calculating the volume of a cylinder
    volume = area * height
    return volume


# Using Try Exception to avoid getting value error like getting
# string instead of integer or float value
try:

    # Define a variable to get the radial from input and convert it
    # to float
    cylinder_radial = float(
        input("Please Enter the Cylinder Radial : ")
    )

    # Define a variable to get the height from input and convert it
    # to float
    cylinder_height = float(
        input("Please Enter the Cylinder Height :")
    )

    # Define a variable to get the output of cylinder_area function
    cylinder_area = cylinder_area(cylinder_radial)

    # Define a variable to get the output of cylinder_volume
    # function
    cylinder_volume = cylinder_volume(
        cylinder_area, cylinder_height)

    # Print th results
    print(f"\nThe Cylinder Radial is : {cylinder_radial} mm\n"
          f"The Cylinder Area is : {cylinder_area} mm^2\n"
          f"The Cylinder Height is : {cylinder_height} mm\n"
          f"The Cylinder Volume is : {cylinder_volume} mm^3")

    # Value error Exception to Print a text instead of getting
    # error
except ValueError:
    print("\nPlease Enter a Valid Integer or Float Value")
