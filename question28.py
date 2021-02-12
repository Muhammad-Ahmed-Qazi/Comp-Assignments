car = 0
bus = 0
lorry = 0
other = 0

for count in range(0, 10000):
    inp = input('Enter the category of the vehicle that passed: (Car: C, Bus: B, Lorry: L, Other: O) ')
    if inp == 'C':
        car += 1
    elif inp == 'B':
        bus += 1
    elif inp == 'L':
        lorry += 1
    elif inp == 'O':
        other += 1

print('These many cars passed the junction:', car)
print('These many buses passed the junction:', bus)
print('These many lorries passed the junction:', lorry)
print('These many other vehicles passed the junction:', other)