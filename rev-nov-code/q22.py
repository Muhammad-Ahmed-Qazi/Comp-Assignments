count = 0
total = 0
min_marks = 101
max_marks = 0

while count < 150:
    mark = float(input('Enter the marks for student no.' + str(count + 1) + ': '))
    if mark >= 0 and mark <= 100:
        total += mark
        if mark > max_marks: max_marks = mark
        if mark < min_marks: min_marks = mark
        count = count + 1
    else:
        print('Marks out of range! Re-enter the marks correctly!')
        continue

print('Lowest mark in the exam:', min_marks)
print('Highest mark in the exam:', max_marks)
print('Average mark in the exam:', total/150)