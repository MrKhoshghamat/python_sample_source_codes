"""
This program get some arguments from user input to calculate the area
of a polygon with desired sides count and length
"""

import math


def get_polygon_sides():
    """
    This Function get the polygon sides counts from user input
    :return: polygon sides counts
    """
    try:
        polygon_sides = int(input("Please Enter the count of "
                                  "polygon sides : "))
        return polygon_sides
    except ValueError:
        print("\nPlease Enter Valid Integer Number for Polygon Sides : ")


def get_polygon_sides_length():
    """
    This Function gets polygon sides length from user input
    :return: polygon sides length
    """
    try:
        polygon_sides_length = float(input("Please Enter the Length of "
                                           "Polygon Sides : "))
        return polygon_sides_length
    except ValueError:
        print("\nPlease Enter Valid Integer or Float Number for "
              "Polygon Sides Length : ")


def calculate_polygon_area(polygon_sides, polygon_sides_length):
    """
    This Function calculate the polygon area from the arguments below
    then return the area of the polygon
    :param polygon_sides: polygon sides counts
    :param polygon_sides_length: polygon sides length
    :return: polygon area
    """
    pi = math.pi
    polygon_area = \
        polygon_sides * (pow(polygon_sides_length, 2)) / \
        (4 * (math.tan(pi / polygon_sides)))

    return polygon_area


def calculation_result():
    """
    This function show the arguments and the result
    Note: This function use in __main__ for run the main program
    :return: return nothing and just print the result
    """
    polygon_sides = get_polygon_sides()
    polygon_sides_length = get_polygon_sides_length()
    calculation_area_result = calculate_polygon_area(polygon_sides,
                                                     polygon_sides_length)

    print(f"\nThe Polygon Sides Count is : {polygon_sides}\n"
          f"The Polygon Sides Length is : {polygon_sides_length}\n"
          f"The Polygon Area is : {calculation_area_result}")


if __name__ == "__main__":
    calculation_result()
