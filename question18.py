above = 0
below = 0

for count in range(0, 100):
    temp = float(input('Enter the temperature for the day: '))
    if temp >= 20:
        above += 1
    elif temp < 20:
        below += 1

print('Days with temperature 20C or above:', above)
print('Days with temperature below 20C:', below)