highest = 0.00
total = 0.00

for count in range(0, 5):
    rain = float(input('Enter the amount of rainfall: '))
    if rain > highest:
        highest = rain
    total = total + rain

avg = total / 5
print('This is the average rainfall:', avg)
print('This is the highest rainfall recorded:', highest)