slow = 1000
fast = 0
total = 0

for count in range(0, 500):
    time = float(input('Enter the time: (hours) '))
    speed = 200 / time
    print('The final speed:', speed)
    if speed > fast: fast = speed
    if speed < slow: slow = speed
    total += speed

print('Slowest final speed:', slow)
print('Fastest final speed:', fast)
print('Average final speed for all cars:', total / 500)