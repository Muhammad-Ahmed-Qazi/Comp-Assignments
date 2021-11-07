highest = 0
total = 0

for count in range(0, 3000):
    for count_s in range(0, 8):
        marks = float(input('Enter marks for subject no.' + str(count + 1) + ': '))
        total += marks
        if marks > highest: highest = marks
    print('Average mark for 8 examinations:', total / 8)

print('Highest marks overall:', highest)