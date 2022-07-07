"""
python_release = 1994
user_input = int(input('When was Python 1.0 released? '))
while user_input > python_release:
    print('It was earlier than that!')
    user_input = int(input('When was Python 1.0 released? '))
    continue
while user_input < python_release:
    print('It was later than that!')
    user_input = int(input('When was Python 1.0 released? '))
    continue
if user_input == python_release:
    print('Correct!')
"""

answer = 0
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break

"changes"



