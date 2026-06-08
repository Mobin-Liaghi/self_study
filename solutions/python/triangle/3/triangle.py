def inequality_checker(sides):
    side_a, side_b, side_c = sides
    if ((side_a + side_b >= side_c) and (side_b + side_c >= side_a) and (side_a + side_c >= side_b)) == False:
        # raise ValueError ("The sides side_a, side_b and side_c don't follow Triangle Inequality")
        return False
    return True

def zero_side_check(sides):
    side_a, side_b, side_c = sides
    if (side_a == 0) or (side_b == 0) or (side_c == 0):
        return False
    return True

def equilateral(sides):
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return ((side_a==side_b) and (side_b==side_c) and (side_a==side_c))
            


def isosceles(sides):
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return (side_a==side_b) or (side_b==side_c) or (side_a==side_c)
            


def scalene(sides):
    if inequality_checker(sides) is False:
        return False
    side_a, side_b, side_c = sides
    if zero_side_check(sides) is False:
        return False
    return ((side_a!=side_b) and (side_b!=side_c) and (side_a!=side_c))
            
