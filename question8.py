high_sun = 0.00
low_rain = 500.00
tot_sun = 0.00
tot_rain = 0.00

for count_res in range(0, 10):
    for count_day in range(0, 365):
        rain = float(input('Please enter the daily rainfall: '))
        sun = float(input('Please enter the daily hours of sunshine: '))
        tot_rain = tot_rain + rain
        tot_sun = tot_sun + sun
        if rain < low_rain:
            low_rain = rain
        elif sun > high_sun:
            high_sun = sun
    avg_rain = tot_rain / 365
    avg_sun = tot_sun / 365
    print('This is the average rainfall for resort no.' + str(count_res + 1) + ':', avg_rain)
    print('This is the average hours of sunshine for resort no.' + str(count_res + 1) + ':', avg_sun)
    tot_sun = 0
    tot_rain = 0

print('This is the highest number of hours of sunshine over all the 10 resorts:', high_sun)
print('This is the lowest amount of rainfall over all the 10 resorts:', low_rain)