n = int(input('Enter any positive number: '))
count = 1
multiply = 0

while (count + 1) != n:
    multiply = count * (count + 1)
    count = count + 1

calc = n / multiply
print('This is the answer for the calculation:', calc)