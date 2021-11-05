import datetime as dt

mexico = -25200
india = 16200
new_zealand = 39600

country = input('Enter the name of the country you are visiting: (Mexico (M), India (I), New Zealand (NZ)) ')
italy_time = input('Enter the time in Italy: (H:M) ')

date_time_obj_1 = dt.datetime.strptime(italy_time, '%H:%M')
print(date_time_obj_1)
date_time_obj_1 = dt.timedelta(0, date_time_obj_1.second, date_time_obj_1.microsecond, 0, date_time_obj_1.minute, date_time_obj_1.hour, 0).total_seconds()

if country == 'M': date_time_obj_1 = date_time_obj_1 + mexico
elif country == 'I': date_time_obj_1 = date_time_obj_1 + india
elif country == 'NZ': date_time_obj_1 =  date_time_obj_1 + new_zealand

print('Time in the country you are visiting is:', str(dt.timedelta(seconds=date_time_obj_1)))