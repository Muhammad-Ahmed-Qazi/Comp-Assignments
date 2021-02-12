singapore = 6.00
canada = -10.00
india = 3.5
calc_time = float(0)
visit_time = float(0)

current = float(input('Enter the current time in Russia: (format should be: 01.01 (hh.mm)) '))
visit = input('Please enter the country you are visiting: (Singapore: S, Canada: C, India: I) ')

if visit == 'S':
    calc_time = current + singapore
elif visit == 'C':
    calc_time = current + canada
elif visit == 'I':
    calc_time = current + india

if calc_time > 23.59:
    visit_time = calc_time - 24.00
    print('Current time in your visiting country is:', visit_time, 'and it is a day further than the Russian day!')
else:
    visit_time =  calc_time
    print('Current time in your visiting country is:', visit_time)