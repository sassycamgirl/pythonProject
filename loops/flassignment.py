"""
For Loops assignment

create list variable that ranges from 1 to 8
print all elements to console but get 3 and 7 skipped
"""

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers_list:
    if x == 3 or x == 7:
        continue
    print(x)