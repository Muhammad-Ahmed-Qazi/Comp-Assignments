high = 0
total = 0

for count in range(0, 365):
    vehicles = int(input('Enter the number of vehicles/day passing over the bridge: '))
    if vehicles > high:
        high = vehicles
    total = total + vehicles

avg = total / 365
print('This is the average number of vehicles/day:', avg)
print('This is the highest number of vehicles/day:', high)