cloudy = 0
rainy = 0
sunny = 0
foggy = 0
highest = 0
lowest = 1000

for count in range(0, 5):
    print('Weather types: CLOUDY, RAINING, SUNNY, FOGGY')
    weather = input('Enter the weather type and temperature: (E.g. CLOUDY, 25) ')
    weather = weather.split(', ')
    if weather[0] == 'CLOUDY': cloudy += 1
    elif weather[0] == 'RAINING': rainy += 1
    elif weather[0] == 'SUNNY': sunny += 1
    elif weather[0] == 'FOGGY': foggy += 1
    if int(weather[1]) > highest: highest = int(weather[1])
    if int(weather[1]) < lowest: lowest = int(weather[1])

print('Cloudy:', cloudy, '| Raining:', rainy, '| Sunny:', sunny, '| Foggy:', foggy)
print('Highest recorded temperature:', highest)
print('Lowest recorded temperature:', lowest)