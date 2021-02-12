taller = 0
shorter = 0

for count in range(0,500):
    height = float(input('Enter the height of the student in metres(m): '))
    if height > 1.45:
        taller += 1
    else:
        shorter += 1

print('This is the number of students that are taller than 1.45m:', taller)
print('This is the number of students that are shorter than 1.45m:', shorter)