"""
while loops
"""

x = 0

"""
 # prints a count starting from 1 up until 10
while x < 10:
    x += 1
    print(x)
"""

"""
will check if x will equal to 6, if so it will continue until its 10
while x < 10:
    x += 1
    if x == 6:
        continue
    print(x)
"""

"""
# 
while x < 10:
    print(x)
    x += 1
else:
    print('x is now equal or larger to 10')
"""

# modula
i = 10

while i <= 10 and i > 5:
    if i % 2 == 0:
        print(f'{i} is divisible by 2')
    else:
        print (f'{i} is not divisible by 2')
    i -= 1
    