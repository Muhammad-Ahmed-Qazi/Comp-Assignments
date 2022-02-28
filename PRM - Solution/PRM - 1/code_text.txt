from prettytable import PrettyTable
import math

# Arrays, lists and dictionaries
ticket_type = {'a': 'One Adult', 'b': 'One Child *', 'c': 'One Senior', 'd': 'Family Ticket **', 'e': 'Groups (6 or > 6) ***'}
cost_one = {'a': 20.0, 'b': 12.0, 'c': 16.0, 'd': 60.0, 'e': 15.0}
cost_two = {'a': 30.0, 'b': 18.0, 'c': 24.0, 'd': 90.0, 'e': 22.50}
ext_attract = {'f': 'Lion Feeding', 'g': 'Penguin Feeding', 'h': 'Evening Barbecue'}
ext_cost = {'f': 2.50, 'g': 2.0, 'h': 5.0}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Custom Functions
def sim_people(tno):
    simulation = [0, 0, 0, 0, 0, 0]
    for ticket in tno:
        if ticket.split(' x ')[0] == 'a': simulation[0] += 1 * int(ticket.split(' x ')[1])
        if ticket.split(' x ')[0] == 'b': simulation[1] += 1 * int(ticket.split(' x ')[1])
        if ticket.split(' x ')[0] == 'c': simulation[2] += 1 * int(ticket.split(' x ')[1])
        if ticket.split(' x ')[0] == 'd': simulation[3] += 2 * int(ticket.split(' x ')[1]); simulation[4] += 3 * int(ticket.split(' x ')[1])
        if ticket.split(' x ')[0] == 'e': simulation[5] += 1 * int(ticket.split(' x ')[1])
    simulation[5] += (simulation[0] + simulation[1] + simulation[2] + simulation[3] + simulation[4])
    return simulation

def inp_format(tno_sim):
    tno_sim = tno_sim.lstrip('-').rstrip('-')
    tno_sim = tno_sim.replace('--', ' & ')
    return tno_sim

def cost_sim(tno_sim, duration):
    sim_cost = 0
    if duration == 2: 
        for item in tno_sim:
            sim_cost = sim_cost + cost_two[item.split(' x ')[0]] * int(item.split(' x ')[1])
    elif duration == 1:
        for item in tno_sim:
            sim_cost = sim_cost + cost_one[item.split(' x ')[0]] * int(item.split(' x ')[1])
    return [tno_sim, sim_cost]

def single(adults, children, seniors, duration):
    tno_sim = ''
    # Single ticket solution
    if adults > 0: tno_sim = tno_sim + '-a x ' + str(adults) + '-'
    if children > 0: tno_sim = tno_sim + '-b x ' + str(children) + '-'
    if seniors > 0: tno_sim = tno_sim + '-c x ' + str(seniors) + '-'
    tno_sim = inp_format(tno_sim).split(' & ')
    return cost_sim(tno_sim, duration)

def ft(adults, children, seniors, duration):
    tno_sim = ''
    if (adults + seniors) > children: tno_sim = tno_sim + '-d x ' + str(math.ceil((adults + seniors) / 2)) + '-'
    if children > (adults + seniors): tno_sim = tno_sim + '-d x ' + str(math.ceil(children / 2)) + '-'
    tno_sim = inp_format(tno_sim).split('&')
    return cost_sim(tno_sim, duration)

def ftsingle(adults, children, seniors, duration):
    tno_sim = ''
    ft_quan = 0
    if (adults + seniors) < children: tno_sim = tno_sim + '-d x ' + str(math.floor((adults + seniors) / 2)) + '-'; ft_quan = math.floor((adults + seniors) / 2)
    if children < (adults + seniors): tno_sim = tno_sim + '-d x ' + str(math.floor(children / 3)) + '-'; ft_quan = math.floor((children) / 3)
    if (adults + seniors + children) < 6:
        bv_sim = [(adults - (2 * ft_quan)), (children - (3 * ft_quan)), (seniors - (2 * ft_quan))]
        if bv_sim[0] > 0: tno_sim = tno_sim + '-a x ' + str(bv_sim[0]) + '-'
        if bv_sim[1] > 0: tno_sim = tno_sim + '-b x ' + str(bv_sim[1]) + '-'
        if bv_sim[2] > 0: tno_sim = tno_sim + '-c x ' + str(bv_sim[2]) + '-'
    else:
        bv_sim_two = [((adults + seniors) - (2 * ft_quan)), (children - (3 * ft_quan))]
        people = 0
        for item in bv_sim_two:
            if item > 0: people = people + item
        if people > 0: tno_sim = tno_sim + '-e x ' + str(people) + '-'
    tno_sim = inp_format(tno_sim).split(' & ')
    return cost_sim(tno_sim, duration)
    

# Task 1 - Started

while True:
    # Table Initialisation
    table = PrettyTable()
    table_two = PrettyTable()
    table_days = PrettyTable()

    # Miscellaneous variables
    count = 0
    tot_cost = 0
    book_no = 1
    error = False
    tc_cost = 0
    ex_cost = 0

    duration = input('How many days do you want to book for? (1/2)(N --> Bookings are all done)' + '\n' + '>> ')
    if duration == 'N': break
    if duration != 'N': duration = int(duration)
    if duration == 1:
        table.field_names = ['T.no', 'Ticket type', 'Cost for one day', 'E.no', 'Extra attraction', 'Cost per person']
        for key, val in ticket_type.items():
            count += 1
            if count >= 3:
                table.add_row([key, val, ('&' + str(cost_one[key])), '---', '---', '---'])
            else:
                if count == 1: att_choose = 'f'
                elif count == 2: att_choose = 'g'
                table.add_row([key, val, ('&' + str(cost_one[key])), att_choose, ext_attract[att_choose], ext_cost[att_choose]])
    if duration == 2:
        table.field_names = ['T.no', 'Ticket type', 'Cost for two days', 'E.no', 'Extra attraction', 'Cost per person']
        for key, val in ticket_type.items():
            count += 1
            if count >= 4:
                table.add_row([key, val, ('&' + str(cost_two[key])), '---', '---', '---'])
            else:
                if count == 1: att_choose = 'f'
                elif count == 2: att_choose = 'g'
                elif count == 3: att_choose = 'h'
                table.add_row([key, val, ('&' + str(cost_two[key])), att_choose, ext_attract[att_choose], ext_cost[att_choose]])
    table_two.field_names = ['Identifier', 'Explanation']
    table_two.add_row(['*', 'An adult may bring up to two children.'])
    table_two.add_row(['**', 'Up to two adults or seniors, and three children.'])
    table_two.add_row(['***', 'Price per person.'])
    table.align = 'l'
    table_two.align = 'l'
    table_days.align = 'l'
    print(table.get_string())
    print(table_two.get_string(border=False))
    table_days.field_names = ['Days']
    table_days.add_row(['Monday (1) | Tuesday (2) | Wednesday (3) | Thursday (4) | Friday (5) | Saturday (6) | Sunday (7)'])
    print(table_days.get_string(header=False))

# Task 2 - Started

    while True:
        day_st = int(input('Enter the starting day of your booking.' + '\n' + 'Example: 2 (for Tuesday)' + '\n' + '>> ')) - 1
        if duration == 2 and days[day_st] == 'Sunday':
            print('\033[0;33m \n' + 'Dear customer,' + '\n' + 'You want to book for Sunday of this week and Monday of the next week. This is not allowed. Bookings can only be made up to a week in advance.' + '\n' + 'Kindly reconsider your decision.' + '\n\n' + 'Thank you!' + '\n \033[0m')
        else: break
    while True:
        adults = int(input('No. of adults going: (0 --> If no adult!) '))
        children = int(input('No. of children going: (0 --> If no children!) '))
        seniors = int(input('No. of senior going: (0 --> If no senior!) '))
        print('Following are values that you input: \u2193')
        print('Adults:', adults, 'Children', children, 'Seniors:', seniors)
        status = input('Have you verified the values? Do you want to make any changes? (Y/n) ')
        if status != 'Y': break
    while True:
        error = False
        print('Enter whichever ticket you want to purchase. Enter the no. of tickets as well:',  '\n' + 'Example: a x 2 & b x 4 & c x 1')
        tno = input('>> ')
        tno = tno.split(' & ')
        sim_result = sim_people(tno)
        print(sim_result)
        if (adults + children + seniors) > sim_result[5]: print('\033[0;31mERROR!:\033[0m Calculations based on your ticket choices for number of people going are less than the number of people going according to you. Please reconsider your ticket choices!'); error = True
        if sim_result[1] != 0:
            if ((sim_result[0]+ sim_result[2]) / sim_result[1]) < 0.5: print('\033[0;31mERROR!:\033[0m Ratio of adults + seniors to children is greater than 1 : 2 with single person tickets, i.e. a, b or c. Ratio allowed is less than or equal to 1 : 2. Please reconsider your ticket choices!'); error = True
        if error != True: break
    if duration == 1:
        for ticket in tno:
            tot_cost = tot_cost + cost_one[ticket.split(' x ')[0]] * int(ticket.split(' x ')[1])
    else:
        for ticket in tno:
            tot_cost = tot_cost + cost_two[ticket.split(' x ')[0]] * int(ticket.split(' x ')[1])
    tc_cost = tot_cost
    eno = input('Enter whichever extra attraction you want to add: (f)(N --> No attraction)(f & g --> Multiple attraction format)' + '\n' + '>> ')
    if eno != 'N':
        eno = eno.split(' & ')
        for att in eno:
            ex_cost = ex_cost + (ext_cost[att] * (adults + seniors + children))
        tot_cost = tot_cost + ex_cost
    book_id = '000' + str(book_no)
    booking = str(book_id)
    print('\n' + 'Booking ID:', booking)
    print('Ticket(s):', '\u2193')
    for ticket in tno:
        tc_ind = ticket.split(' x ')[0]
        tc_type = ticket_type[tc_ind]
        if tc_ind == 1: tc_type = tc_type[:-2]
        elif tc_ind == 3: tc_type = tc_type[:-3]
        elif tc_ind == 4: tc_type = tc_type[:-4]
        ticket = tc_type + ' (x ' + ticket.split(' x ')[1] + ')'
        print('-', ticket)
    print('Day(s):', '\u2193')
    for count in range(0, int(duration)):
        day = days[day_st + count]
        print('-', day)
    print('Extra attraction(s):', '\u2193')
    if eno != 'N': 
        for att in eno:
            attraction = ext_attract[att]
            print('-', attraction)
    else: print('--')
    cost = '$' + str(tot_cost)
    print('Total Cost:', '\033[1;32m' + cost, '\033[0m\n')

# Task 3  - Started
    
    sim_tc_res = {'a': single(adults, children, seniors, duration)[0], 'b': ft(adults, children, seniors, duration)[0], 'c': ftsingle(adults, children, seniors, duration)[0]}
    sim_cost_res = {'a': single(adults, children, seniors, duration)[1], 'b': ft(adults, children, seniors, duration)[1], 'c': ftsingle(adults, children, seniors, duration)[1]}
    lowest_val = 10000000000000000000000000000
    for key, val in sim_cost_res.items():
        if val < lowest_val:
            lowest_val = val
            lowest_ind = key
    if lowest_val < tc_cost: 
        print('Our simulations predict a better value option for the configuration of people that you have entered. Simulated cost is:', '$' + str(lowest_val) + ' (Without addition of extra attraction cost). The ticket choice is: \u2193')
        for ticket in sim_tc_res[lowest_ind]:
            tc_ind = ticket.split(' x ')[0]
            tc_type = ticket_type[tc_ind]
            if tc_ind == 1: tc_type = tc_type[:-2]
            elif tc_ind == 3: tc_type = tc_type[:-3]
            elif tc_ind == 4: tc_type = tc_type[:-4]
            ticket = tc_type + ' (x ' + ticket.split(' x ')[1] + ')'
            print('-', ticket)
        consent = input('Would you like to change to the better value option? (Y/n) ')
        if consent == 'Y': 
            book_id = '000' + str(book_no)
            booking = str(book_id)
            print('\n' + 'Booking ID:', booking)
            print('Ticket(s):', '\u2193')
            for ticket in sim_tc_res[lowest_ind]:
                tc_ind = ticket.split(' x ')[0]
                tc_type = ticket_type[tc_ind]
                if tc_ind == 1: tc_type = tc_type[:-2]
                elif tc_ind == 3: tc_type = tc_type[:-3]
                elif tc_ind == 4: tc_type = tc_type[:-4]
                ticket = tc_type + ' (x ' + ticket.split(' x ')[1] + ')'
                print('-', ticket)
            print('Day(s):', '\u2193')
            for count in range(0, int(duration)):
                day = days[day_st + count]
                print('-', day)
            print('Extra attraction(s):', '\u2193')
            if eno != 'N': 
                for att in eno:
                    attraction = ext_attract[att]
                    print('-', attraction)
            else: print('--')
            cost = '$' + str(lowest_val + ex_cost)
            print('Total Cost:', '\033[1;32m' + cost, '\033[0m')
    print('\033[1;32m \nCongratulations! Your booking request has been received!\033[0m \n')
    book_no += 1