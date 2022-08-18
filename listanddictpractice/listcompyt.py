"""
list1 = []
for i in range(5):
    list1.append(i*i)
print(list1)
"""

"""
list2 = [i*i for i in range(5)]
print(list2)

def cube(i):
    return i*i*i
cubes = [cube(i) for i in range(5)]
print(cubes)
"""

evens = [i for i in range(20) if i%2==0]
print(evens)

"""
for i in range(5) or i*i for i in range(5)
it means you multiply 0x0,1x1,2x2,3x3,4x4
which would print 0,1,4,9,16
             
"""