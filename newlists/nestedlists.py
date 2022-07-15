"""
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)

for x in cells:
    for y in x:
        print('Element:', y)

for row in cells:
    for cell in row:
        print(cell, '', end='')
    print()
"""

table = [i for i in range(1, 6) for j in range(4)]
print(table)