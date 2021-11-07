stat = 'y'

while stat == 'y':
    sens_1 = float(input('Enter reading of Sensor 1: (Temp C) '))
    sens_2 = float(input('Enter reading of Sensor 2: (Oxygen) '))
    if sens_1 > 45.0 or sens_2 < 0.19: print('One or more readings are out of range!')
    stat = input('You want to enter more data? (y/N) ')