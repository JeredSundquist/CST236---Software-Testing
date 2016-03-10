from datetime import datetime
from math import pi, e, sqrt, factorial, fabs
from decimal import Decimal
import getpass

"GET TIME AND DATE"


def date_time():
    return datetime.now().strftime('%m: %d: %y: %H:%M:%S')


"FIBONACCI: Assumes starting with 1"


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


"NTH DIGIT OF PI-(precision is 48 places to the right of the decimal)"


def pi_n(n):
    if n == 1:
        return '3'
    elif n == 0:
        return "invalid"
    else:
        npi = str(Decimal(pi))
        return npi[int(n)]


"OPEN THE DOOR HAL-(should be portable to UNIX and WIN"


def open_door():
    return str('I\'m afraid I can\'t do that ' + getpass.getuser())


"CONVERT METRIC"


def convert_metric(my_num, my_unit, convert_to):
    # local variables to store starting and convert to units
    pow1 = 0
    pow2 = 0

    "dictionary stores keyword and value for metric units"
    unit_dict = {'tera': 6,
                 'giga': 5,
                 'mega': 4,
                 'kilo': 3,
                 'hecto': 2,
                 'deka': 1,
                 'noConvert': 0,
                 'deci': -1,
                 'centi': -2,
                 'milli': -3,
                 'micro': -4,
                 'nano': -5,
                 'pico': -6}

    "starting unit power conversion"
    for myKey in unit_dict.iterkeys():
        if myKey == my_unit:
            pow1 = unit_dict.get(my_unit)
            break
    "unit power to convert to"
    for myKey in unit_dict.iterkeys():
        if myKey == convert_to:
            pow2 = unit_dict.get(convert_to)
            break

    "power difference"
    pow_dif = pow1 - pow2
    pow_pow = 10 ** pow_dif

    return str(my_num * pow_pow) + " " + convert_to


"PRINT UNITS ONE CAN CONVERT BETWEEN"


def convert_ten_units():
    return "tera: 6, giga: 5, mega: 4," \
           "kilo: 3, hecto: 2,deka: 1," \
           "noConvert: 0, deci: -1, centi: -2," \
           "milli: -3, micro: -4, nano: -5, pico: -6"


"FAVORITE NUMBER"


def fav_num(your_num):
    # my favorite number
    my_num = 13.0

    "check your number and my number for match"
    if float(your_num) != my_num:  # no match
        return 'My number ' + str(my_num) + ' is better than your number!'
    else:  # match
        return 'Hey we are favorite number ' + str(my_num) + ' buddies!'


"COLOR MIXER"


def mix_color(color1, color2):
    # match color
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        return 'purple'
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
        return 'orange'
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
        return 'green'
    elif color1 == 'red' and color2 == 'red':
        return 'red'
    elif color1 == 'blue' and color2 == 'blue':
        return 'blue'
    elif color1 == 'yellow' and color2 == 'yellow':
        return 'yellow'


"PRINT COLOR FOR MIXER"


def color_print():
    return 'Red, Yellow, and Blue are the color that can be mixed'


"NTH DIGIT OF e-(precision is 48 places to the right of the decimal)"


def e_n(n):
    if n == 1:  # n is left of decimal
        return '2'
    elif n == 0:  # n is invalid
        return "invalid"
    else:  # n is valid: find number
        ne = str(Decimal(e))
        return ne[int(n)]


"SQUARE ROOT OF N"


def sqrt_n(n):
    return str(sqrt(n))


"N FACTORIAL"


def fact_n(n):
    return str(factorial(n))


"JOKE OF THE DAY"


def joke():
    return 'beer'


"ABSOLUTE VALUE"


def abs_n(n):
    return str(fabs(n))


"HYPOTENUSE"


def hypo_xy(my_x, my_y):
    p = pow(my_x, 2) + pow(my_y, 2)
    return str(sqrt(p))


"ANOTHER STORY"


def may_i_have_another():
    return 'Uuum no...'
