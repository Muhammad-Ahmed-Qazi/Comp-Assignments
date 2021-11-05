for count in range(0, 25):
    mark = float(input('Enter the marks: '))
    if mark > 69: print('DISTINCTION')
    elif mark <= 69 and mark >= 60: print('MERIT')
    elif mark <= 59 and mark >= 50: print('PASS')
    else: print('FAIL')
