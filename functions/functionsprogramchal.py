"""
Functions Programming Challenge
"""

def fahrenheit_to_celsius_converter(f_degree):
    c_degree = (f_degree - 32) * 5 /9
    return c_degree


def celsius_to_fahrenheit_converter(c_degree):
    f_degree = 9.0 / 5.0 * c_degree + 32
    return f_degree

print(fahrenheit_to_celsius_converter(81))

print(celsius_to_fahrenheit_converter(10))