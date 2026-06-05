""" Function to check if a given year is a leap year or not. """

def leap_year(year):
    """
    a leap year is defined as:
    - It is divisible by 4 but not divisible by 100, OR
    - It is divisible by 400
    
    input: year (int): The year to check.

    output: bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
