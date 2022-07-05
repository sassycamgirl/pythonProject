'''
Functions part 2
'''

# scope

"""
def my_function():
    year = 1998
    print(year)


year = 2000
print(year)
my_function()
"""

"""
def my_function(*bunch_of_data):
    print(bunch_of_data[-1])

my_function(1, 2, 3, 4, 5, 'a')
# will only print the letter a
"""

"""
def my_function(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

my_function(lowest_number=8, highest_number=10)
"""

"""
def my_function(country= 'Somewhere in the world...'):
    print(country)

my_function('Sweden')
my_function('India')
my_function()
my_function('United States')
"""

"""
def my_function(number_one, number_two):
    return number_one * number_two

mult_num = my_function(10, 5)
print(mult_num)
"""


def my_function(list_of_fruit):
    for fruit in list_of_fruit:
        print(fruit)

fruit = ['Banana', 'Apple', 'Orange']
my_function(fruit)