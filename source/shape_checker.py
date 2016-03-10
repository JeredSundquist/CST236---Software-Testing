"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 3 sides of a triangle is equilateral, scalene or iscoceles
"""


def get_triangle_type(a=0, b=0, c=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int or tuple or list or dict

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(a, (tuple, list)) and len(a) == 3:
        c = a[0]
        b = a[1]
        a = a[2]

    if isinstance(a, dict) and len(a.keys()) == 3:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return "invalid"

    "Check for invalid 0 area or Invalid triangle"
    x = a + b
    y = b + c
    z = a + c

    "Check for negative or side = 0"
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    if x <= c or y <= a or z <= b:
        return "invalid"

    if a == b and b == c:
        return "equilateral"

    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"


def get_square_type(a=0, b=0, c=0, d=0):
    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[0]
        c = a[1]
        b = a[2]
        a = a[3]

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(
            d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == b and b == c and c == d:
        return "square"

    elif a == c and b == d:
        return "rectangle"

    else:
        return "invalid"
        # elif a == c and b == d:
        #     return "rhombus"
