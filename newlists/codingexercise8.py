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

for index, (city_from, city_to, time) in enumerate(connections):
    for time in connections:
        cities.append(time)
    if city_to == 'Rome':
        romecount = len(city_to) + 1
print(romecount, cities)

