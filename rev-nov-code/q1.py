import datetime

tot_time = 0

for count in range(0, 30):
    name = input('Enter the name of student ' + str(count + 1) + ': ')
    print('Please input time in 24-hr format! Example Input: 16:23:57 (HH:MM:SS)')
    log_on = input('Enter the time at which the student logged on: ')
    date_time_obj_1 = datetime.datetime.strptime(log_on, '%H:%M:%S')
    log_off = input('Enter the time at which the student logged off: ')
    date_time_obj_2 = datetime.datetime.strptime(log_off, '%H:%M:%S')
    calc_time = date_time_obj_2 - date_time_obj_1
    tot_time = tot_time + (calc_time).total_seconds()

avg = float(tot_time) / 30
print('Average length of time per day spent by each student on the internet:', str(datetime.timedelta(seconds=avg)))
