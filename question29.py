highest = 0

for count in range(0, 500):
    at = float(input('Enter the time the car passed Point A: (hh.mm) '))
    bt = float(input('Enter the time the car passed Point B: (hh.mm) '))
    integer = bt - at
    seconds = integer * 3600
    speed = 100 / seconds
    if speed >= 27.78:
        print('Speed of car is:', speed, 'm/s')
        print('Speed limit is exceeded!')
        if speed > highest:
            highest = speed
    else:
        print('Speed of car is:', speed, 'm/s')
        if speed > highest:
            highest = speed

print('The highest speed of a car monitored is:', highest, 'm/s')