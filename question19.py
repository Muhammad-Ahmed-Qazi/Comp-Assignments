fastest = 0
slowest = 400
total = 0

for count in range(0, 5000):
    speed = float(input('Enter the top speed of the car: (mph) '))
    if speed < slowest:
        slowest = speed
    elif speed > fastest:
        fastest = speed
    total = total + speed

avg = total / 5
print('This is the average speed of all cars:', avg)
print('This is the fastest speed of a car:', fastest)
print('This is the slowest speed of a car:', slowest)