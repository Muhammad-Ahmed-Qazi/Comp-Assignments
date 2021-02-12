vehicles_exc = 0
highest = 0.00

for count in range(0, 8000):
    time_a = float(input('Enter the time at which the car passed Point A: (hh.mm) '))
    time_b = float(input('Enter the time at which the car passed Point B: (hh.mm) '))
    speed = 0.5 / (time_b - time_a)
    if speed > 100:
        vehicles_exc = vehicles_exc + 1
        if speed > highest:
            highest = speed
        print('The speed of the car is:', speed)
        print('The car exceeded the speed limit!')
    else:
        print('The speed of the car is:', speed)

perc_exc = (vehicles_exc / 8000) * 100
print('This is the number of cars that exceeded the speed limit:', vehicles_exc)
print('This is the percentage of cars that exceeded the speed limit:', perc_exc)
print('This is the highest speed at which a car passed the points:', highest)