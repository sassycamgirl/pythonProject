values = [[3 - x for x in range(2)] for y in range(6)]
print(values)

sum = 0.0
for row in values:
    print(row)
    for cell in row:
        print(cell)
        sum += cell

print(sum)