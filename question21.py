pos = 0
zero = 0
neg = 0

for count in range(0, 1000):
    number = float(input('Enter any number: '))
    if number == 0:
        zero += 1
    elif number < 0:
        neg += 1
    elif number > 0:
        pos += 1

print('This many were positive', pos, ', this many were zeroes', zero, 'and this many were negative', neg, '.')