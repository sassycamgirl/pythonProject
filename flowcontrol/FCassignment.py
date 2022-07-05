"""
Flow Control Assignment

"""

grade = 76

"""
 My original answer
if grade >= 90:
    print('You made an A on the test')
elif grade >= 80:
    print('You made a B on the test')
elif grade >= 70:
    print('You made a C on the test')
elif grade >= 60:
    print('You made a D on the test')
else:
    print('You made an F on the test')
"""

# the udemy answer
if grade >= 90:
    print('A')
elif grade >= 80 and grade < 90:
    print ('B')
elif grade >= 70 and grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
else:
    print('F')