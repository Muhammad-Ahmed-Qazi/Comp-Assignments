one_more = 0
seven_more = 0

for count in range(0, 2):
    year =  int(input('Enter the year number of the student: '))
    height = float(input('Enter the height of the student: '))
    if year == 1:
        if height > 135:
            one_more = one_more + 1
    elif year == 7:
        if height > 175:
            seven_more = seven_more + 1

print('This is the number of the students of Year 1:', one_more)
print('This is the number of the students of Year 7:', seven_more)