import math


def get_wind_speed():
    """
    This function gets wind velocity from user input
    :return: wind_speed
    """
    try:
        wind_speed = float(input("Please Enter a wind speed in "
                                 "kilometer / hour : "))
        return wind_speed
    except ValueError:
        print("Invalid Parameter, Please Enter valid float or integer "
              "number in kilometer / hour")


def get_wind_temperature():
    """
    This function gets wind temperature from user input
    :return: wind_temperature
    """
    try:
        wind_temperature = float(input("Please Enter wind temperature "
                                       "in degrees celsius : "))
        return wind_temperature
    except ValueError:
        print("Invalid Parameter, Please Enter a valid float or integer "
              "number in degrees celsius.")


def wind_chill_index_calculation(wind_speed, wind_temperature):
    """
    This function gets wind_speed and wind_temperature as input then
    calculate the wind_chill_index via it's own formula
    :param wind_speed: win_speed
    :param wind_temperature: wind_temperature
    :return: wind_chill_index_result
    """
    wind_chill_index_formula = 13.12 + 0.6215 * \
                               wind_temperature - 11.37 * \
                               math.pow(wind_speed, 0.16) + 0.3965 * \
                               wind_temperature * math.pow(wind_speed, 0.16)
    return wind_chill_index_formula


def wind_chill_index():
    """
    This function show the result of wind_chill_index_calculation
    """
    wind_speed = get_wind_speed()
    wind_temperature = get_wind_temperature()
    wind_chill_index_calc = wind_chill_index_calculation(wind_speed,
                                                         wind_temperature)

    print(f"\nWind Speed is : {wind_speed}\n"
          f"Wind Temperature is : {wind_temperature}\n"
          f"Wind Chill Index is : {wind_chill_index_calc}")


if __name__ == "__main__":
    wind_chill_index()
