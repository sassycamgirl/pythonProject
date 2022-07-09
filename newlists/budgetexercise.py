spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
low_spendings = []
normal_spendings = []
high_spendings = []

for low in spendings:
    if low < 1000:
        low_spendings.append(low)

for normal in spendings:
    if (normal >= 1000) and (normal <= 2500):
        normal_spendings.append(normal)

for high in spendings:
    if high > 2500:
        high_spendings.append(high)
print('Number of months with low spendings:{', len(low_spendings), '}, normal spendings:{', len(normal_spendings),
      '}, high spendings:{', len(high_spendings), '}.', sep='')


"""
#answer from udemy
low = 0
normal = 0
high = 0

for month in spendings:
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1

print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(
    normal) + ', high spendings: ' + str(high) + '.')
"""