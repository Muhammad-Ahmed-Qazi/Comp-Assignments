import datetime as dt

error_count = 0

for count in range(0, 4):
    stud_id = input('Enter your ID: ')
    start = input('Enter the date of starting school: (YYMMDD --> E.g. 070910) ')
    start = dt.date(int(start[0] + start[1]), int(start[2] + start[3]), int(start[4] + start[5]))
    end = input('Enter the date of ending school: (YYMMDD --> E.g. 120804) ')
    end = dt.date(int(end[0] + end[1]), int(end[2] + end[3]), int(end[4] + end[5]))
    check = str(end - start)
    if check[0] == '-': error_count = error_count + 1
    elif check[0] == '0': error_count = error_count + 1

print(error_count)