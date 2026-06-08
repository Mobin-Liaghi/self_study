"""Functions to determine if a Triangle is equilateral, isosceles, or scalene. """

def inequality_checker(sides):
    """
    Checks if the sides of a triangle follow Triangle Inequality.
    Triangle Inequality states that the sum of the lengths of any two sides of a triangle must be greater than or equal to the length of the remaining side.

    Input (list): sides - a list of three numbers representing the lengths of the sides of a triangle

    Output (boolean): True if the sides follow Triangle Inequality, False otherwise
    """
    side_a, side_b, side_c = sides
    if ((side_a + side_b >= side_c) and (side_b + side_c >= side_a) and (side_a + side_c >= side_b)) is False:
        # raise ValueError ("The sides side_a, side_b and side_c don't follow Triangle Inequality")
        return False
    return True

def zero_side_check(sides):
    """
    Checks if any side of the triangle has a length of zero.

    Input (list): sides - a list of three numbers representing the lengths of the sides of a triangle

    Output (boolean): True if none of the sides have a length of zero, False otherwise
    """
    side_a, side_b, side_c = sides
    if (side_a == 0) or (side_b == 0) or (side_c == 0):
        return False
    return True

def equilateral(sides):
    """
    Checks if a triangle is equilateral. An equilateral triangle is a triangle in which all three sides are of equal length.

    Input (list): sides - a list of three numbers representing the lengths of the sides of a triangle

    Output (boolean): True if the triangle is equilateral, False otherwise
    """
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return ((side_a==side_b) and (side_b==side_c) and (side_a==side_c))
            


def isosceles(sides):
    """
    Checks if a triangle is isosceles. An isosceles triangle is a triangle in which at least two sides are of equal length.

    Input (list): sides - a list of three numbers representing the lengths of the sides of a triangle

    Output (boolean): True if the triangle is isosceles, False otherwise
    """
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return (side_a==side_b) or (side_b==side_c) or (side_a==side_c)
            


def scalene(sides):
    """
    Checks if a triangle is scalene. A scalene triangle is a triangle in which all three sides are of different lengths.

    Input (list): sides - a list of three numbers representing the lengths of the sides of a triangle

    Output (boolean): True if the triangle is scalene, False otherwise
    """
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return ((side_a!=side_b) and (side_b!=side_c) and (side_a!=side_c))
           