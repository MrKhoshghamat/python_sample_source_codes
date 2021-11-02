"""
It is a Program to calculate the area of a parallel with a function
that get base and height and then return the result as output
"""


# Define the function that get base and height as input
def parallelogram_area(base, height):
    # Calculate the area of parallelogram
    area = base * height
    return area


# Using try catch exception to avoid value error from input
try:

    # Define variable as base of parallelogram and convert it to int
    parallelogram_base = \
        int(input("Please Enter Base of Parallelogram : "))

    # Define variable as height of parallelogram and
    # convert it to int
    parallelogram_height = \
        int(input("Please Enter Height of Parallelogram : "))

    # Define variable as area of parallel and call the define
    # due to parallelogram are calculation
    parallelogram_area = \
        parallelogram_area(
            parallelogram_base, parallelogram_height
        )

    # Print the results
    print(f"\nThe Base of Parallelogram is : {parallelogram_base}\n "
          f"The Height of Parallelogram is : {parallelogram_height}\n "
          f"The Area of Parallelogram is : {parallelogram_area}")

    # This is the exception of value error in order to print a text
    # instead of error if in input bring any value type except int
except ValueError:
    print("\nPlease Enter a Valid Integer Number")
