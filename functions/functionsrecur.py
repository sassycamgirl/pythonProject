"""
Functions Recursive *Advanced
"""

# 5*4**3*2*1

"""def factorial(x):
    y = 1
    while x > 0:
        y *= x
        x -= 1
    return y

factorial_number = factorial(5)
print(factorial_number)"""

def factorial(x):
    if y == 1:
        return 1
    else:
        print(x)
        return x * factorial(x - 1)
factorial_number = factorial(5)
print(factorial_number)