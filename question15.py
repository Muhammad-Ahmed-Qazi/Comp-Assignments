total = 0
tot_all = 0
high = 0

for count_exp in range(0, 5):
    for count_read in range(0, 20):
        reading = float(input('Enter the temperature reading: '))
        if reading > high:
            high = reading
        total = total + reading
        tot_all = tot_all + reading
    avg = total / 2
    print('The average temperature reading for this experiment is:', avg)
    total = 0

avg = tot_all / (2 * 2)
print('This is the average temperature overall:', avg)
print('This is the highest temperature reading overall:', high)