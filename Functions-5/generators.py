def get_number():
    for i in range(1, 4):
        yield i

generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))
print("\n")

for x in get_number():
    print(x)

numbers = list(get_number())
print("\n", numbers)
