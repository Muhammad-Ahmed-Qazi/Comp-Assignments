import datetime

name_f = []
name_l = []
vol_list = []
vol_area_list = []
area_names = ['Pier Entrance Gate', 'Gift Shop', 'Painting and Decorating']
date_join = []
pay_status_list = []

name_sponsor = []
message_sponsor = []

def task_1():
    first_name = input('Enter your first name: \n>>> ')
    last_name = input('Enter your last name: \n>>> ')
    volunteer = input('Do you want to work as a volunteer?(Y/n) \n>>> ')
    if volunteer == 'Y':
        vol_area = input('Which area would you like to work at as a volunteer?(Enter serial no. of your choice) \n1. Pier Entrance Gate \n2. Gift Shop \n3. Painting and Decorating \n>>> ')
    else: vol_area = '---'
    join_date = input('Enter your date of joining: (Format: Day-Month-Year | Example: 15-08-2022) \n>>> ').split('-')
    join_date = datetime.datetime(int(join_date[2]), int(join_date[1]), int(join_date[0]))
    pay_status = input('Enter whether you have paid the $75 fee: (Y/n) \n>>> ')

    name_f.append(first_name)
    name_l.append(last_name)
    vol_list.append(volunteer)
    vol_area_list.append(vol_area)
    date_join.append(join_date)
    pay_status_list.append(pay_status)

def task_2():
    print('Categories for data filtration: \n1. Members who have chosen to work as volunteers \n2. Volunteers who would like to work at the pier entrance gate \n3. Volunteers who would like to work in the gift shop \n4. Volunteers who would like to help with painting and decorating tasks \n5. Members whose membership has expired \n6. Members who have not yet paid their $75 fee')
    category = input('Enter the category you want to choose: (Serial No. ) \n>>> ')
    if category == '1':
        for count in range(0, len(name_f)):
            if vol_list[count] == 'Y': print('-', name_f[count], name_l[count])
    elif category == '2':
        for count in range(0, len(name_f)):
            if vol_area_list[count] == '1': print('-', name_f[count], name_l[count])
    elif category == '3':
        for count in range(0, len(name_f)):
            if vol_area_list[count] == '2': print('-', name_f[count], name_l[count])
    elif category == '4':
        for count in range(0, len(name_f)):
            if vol_area_list[count] == '3': print('-', name_f[count], name_l[count])
    elif category == '5':
        for count in range(0, len(name_f)):
            now = datetime.datetime.now()
            if date_join[count] < datetime.datetime(int(now.strftime('%Y')), 1, 1): print('-', name_f[count], name_l[count])
    elif category == '6':
        for count in range(0, len(name_f)):
            if pay_status_list[count] == 'n': print('-', name_f[count], name_l[count])

def task_3():
    while True:
        name_spon = input('Enter your name: \n>>> ')
        message = input('Enter the short message that you would like to have on the sponsored brass plaque: \n>>> ')
        print('Please confirm the following inputs: \n- Name: ' + name_spon, '\n- Short Message:', message)
        verify = input('Enter whether the inputs are correct or not: (Y/n) \n>>> ')
        if verify == 'Y': break
        else: print('Please re-enter the data to avoid errors found in the verification process.'); continue
    name_sponsor.append(name_spon)
    message_sponsor.append(message)
    print('Data has been stored. Your charge: $200')

while True:
    choice = input('Which one of the following actions do you want to perform?(Enter S.no for your choice)(N --> End Program) \n1. Become a new member of Friends of Seaview Pier \n2. Get certain data from the membership data \n3. Sponsor a wooden plank \n>>> ')
    if choice == '1': task_1()
    elif choice == '2': task_2()
    elif choice == '3': task_3()
    elif choice == 'N': break

print('Program Ends!')