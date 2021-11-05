day_tot = 0
year_tot = 0
min_temp = 1000
max_temp = 0

for count in range(0, 365):
    for count_d in range(0, 10):
        temp = float(input('Enter the temperature for day no. ' + str(count + 1) + ': '))
        day_tot = day_tot + temp
        if temp > max_temp: max_temp = temp
        if temp < min_temp: min_temp = temp
    avg = day_tot / 10
    print('Avg. temperature for day no. ' + str(count + 1) + ':', avg)
    year_tot = year_tot + day_tot
    day_tot = 0

print('Avg. temperature for the whole year:', (year_tot / 365))