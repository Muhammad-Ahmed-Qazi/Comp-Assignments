import re

count = 0
fa = 0
sj = 0
ka = 0

while count < 400:
    code = input('Enter the code for flight no.' + str(count + 1) + ': (FA 156) ')
    check = re.match('[A-Z][A-Z] [0-9][0-9][0-9]', code)
    if bool(check):
        airline = code.split(' ')[0]
        if airline == "FA": fa = fa + 1
        elif airline == "SJ": sj = sj + 1
        elif airline == "KA": ka = ka + 1
        count = count + 1
    else:
        continue

print('Flights for: FA:', fa, '| SJ:', sj, '| KA:', ka)
print('Flights for: FA:', str((fa / 100) * 400) + '%' , '| SJ:', str((sj / 100) * 400) + '%' , '| KA:', str((ka / 100) * 400) + '%' )
