total = 0

for count in range(0, 100):
    number = float(input('Enter any number: '))
    total = total + number

print('Average of the hundred numbers entered:', (total / 100))