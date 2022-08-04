"""
might need for and if loop
"""

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
cities = []
time_list = []
summ = 0

for index, (city_from, city_to, time) in enumerate(connections):
  if city_to == 'Rome':
        romecount = len(city_to) + 1
        time_list.append(time)
for t in time_list:
  summ += t
average = summ / romecount
print(romecount, 'connections lead to Rome with an average flight time of', int(average), 'minutes') 

"""
    for time in connections:
        cities.append(time)
"""

