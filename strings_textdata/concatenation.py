"""
strings concatenation

"""

my_name = 'George'
print(my_name + ' ' +'Martinez')
last_name = 'Martinez'
print(my_name + ' ' + last_name)

# formats

first_name = 'George'
last_nametwo = 'Martinez'
hello_text = 'Hello, {first} {last}'.format(first=first_name, last=last_nametwo)
print(hello_text)

# third example

first_nametwo = 'George'
number_of_showstwo = 8
hello_statement = \
    f'{first_nametwo} has {number_of_showstwo} pairs of shoes'
print(hello_statement)
