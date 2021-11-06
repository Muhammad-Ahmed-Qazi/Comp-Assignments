above = 0
below = 0
low = 1000

for count in range(0, 200):
    temp = float(input('Enter the temperature for hour no.' + str(count + 1) + ': '))
    if temp > 20: above += 1
    elif temp < 10: below += 1
    if temp < low: low = temp

print('This many temperatures were above 20C:', above)
print('THis many temperatures were below 10C:', below)
print('This is the lowest temperature recorded:', low)