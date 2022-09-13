values = [[1 - x for x in range(2)] for y in range(6)]
print(values)

sum = 0.0
for row in values:
    for cell in row:
        sum += cell

print(sum)