'''
Functions Assignment 2
'''

def remove_elements(numbers_list_arg):
    numbers_list_arg.pop(0)
    numbers_list_arg.pop(-1)
    return numbers_list_arg

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
updated_list = remove_elements(numbers_list)
print(updated_list)