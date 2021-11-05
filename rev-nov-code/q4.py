import math

for count in range(0, 30):
    data_inp = input('Enter your ID, weight (kg) and height (m): (E.g. 1889, 48, 1.67) ')
    bmi = float(data_inp.split(', ')[1]) / math.pow(float(data_inp.split(', ')[2]), 2)
    print('ID:', data_inp.split(', ')[0], '| BMI:', round(bmi, 3))
    if bmi > 25: print('Over WEIGHT')
    elif bmi <= 25 and bmi >= 19: print('NORMAL')
    elif bmi < 19: print('UNDER WEIGHT')
