tot_temp = 0.00
tot_sun = 0.00

for count in range(0, 365):
    temp = float(input('Enter the temperature for the day: '))
    sun = float(input('Enter the hours of sunshine for the day: (hh.mm) '))
    tot_temp = tot_temp + temp
    tot_sun = tot_sun + sun

avg_temp = tot_temp / 3
avg_sun = tot_sun / 3
print('This is the average temperature for the year:', avg_temp)
print('This is the average no. of hours of sunshine for the year:', avg_sun)