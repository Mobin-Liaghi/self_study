def inequality_checker(sides):
    a, b, c = sides
    if ((a + b >= c) and (b + c >= a) and (a + c >= b)) == False:
        # raise ValueError ("The sides a, b and c don't follow Triangle Inequality")
        return False
    return True

def zero_side_check(sides):
    a, b, c = sides
    if (a == 0) or (b == 0) or (c == 0):
        return False
    return True

def equilateral(sides):
    if inequality_checker(sides) is False:
        return False
    a, b, c = sides
    if zero_side_check(sides) is False:
        return False
    return ((a==b) and (b==c) and (a==c))
            


def isosceles(sides):
    if inequality_checker(sides) is False:
        return False
    a, b, c = sides
    if zero_side_check(sides) is False:
        return False
    return (a==b) or (b==c) or (a==c)
            


def scalene(sides):
    if inequality_checker(sides) is False:
        return False
    a, b, c = sides
    if zero_side_check(sides) is False:
        return False
    return ((a!=b) and (b!=c) and (a!=c))
            
