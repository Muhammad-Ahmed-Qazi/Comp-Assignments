data = []
total = 0
best = 0
worst = 1000

for count in range(0, 1000):
    distance = float(input('Enter the distance travelled: (km) '))
    fuel = float(input('Enter the amount of fuel used: (l) '))
    economy = distance / fuel
    data.append(economy)
    total += economy
    if economy > best: best = economy
    if economy < worst: worst = economy

for item in data:
    print('Fuel economy: (km/l)', item)

print('Average fuel economy for all cars input:', total/1000)
print('Best fuel economy:', best)
print('Worst fuel economy:', worst)