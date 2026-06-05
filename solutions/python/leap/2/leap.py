def leap_year(year):
    """
    Function to check if a given year is a leap year or not.

    input: year (int): The year to check.

    output: bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
