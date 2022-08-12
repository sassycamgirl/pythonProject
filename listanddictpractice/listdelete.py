import time
sesame_street = ['Kermit', 'Big Bird', 'Count',
                 'Cookie Monster', 'Oscar', 'Elmo']
time.sleep(1)
print('This is your Sesame Street list:', sesame_street)
time.sleep(5)
del sesame_street[5]
print('This is Sesame Street without Elmo:', sesame_street)
time.sleep(5)
del sesame_street[2]
print('Now this is Sesame Street without the count:', sesame_street)
time.sleep(5)
del sesame_street[1]
del sesame_street[2]
print(sesame_street, 'only remain.')
time.sleep(5)
del sesame_street[1:]
print('Now', *sesame_street, 'is all who\'s left.')
time.sleep(5)
print('Have a good day!')


