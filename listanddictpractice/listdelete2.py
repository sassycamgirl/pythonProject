import time
fire_emblem_waifus = ['Tharja', 'Lucina', 'Camilla',
                 'Olivia', 'Azura', 'Edelgard', 'Lysithea', 'Hilda']
time.sleep(1)
print('This is your Fire Emblem Waifu list:')
print(fire_emblem_waifus)
time.sleep(4)
print('That\'s', len(fire_emblem_waifus), 'waifus. \n',)

time.sleep(5)
del fire_emblem_waifus[7:]
print('Hilda has been taken out.')
print(fire_emblem_waifus)
time.sleep(4)
print(len(fire_emblem_waifus), 'waifus remain. \n')

time.sleep(5)
del fire_emblem_waifus[1:4]
print('Lucina, Camilla, and Olivia are removed.')
print(fire_emblem_waifus)
time.sleep(4)
print(len(fire_emblem_waifus), 'waifus remain. \n')

time.sleep(5)
del fire_emblem_waifus[-3:]
print('Azura, Edelgard, and Lysithea are gone')
print(fire_emblem_waifus)
time.sleep(4)
print(len(fire_emblem_waifus), 'waifu remains. \n')

time.sleep(5)
print('Have a good day! =)')
time.sleep(5)


