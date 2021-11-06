total = 0

for count in range(0, 1000):
    item_type = int(input('Enter the type of item: (1, 2, 3) '))
    p_cost = float(input('Enter the parts cost of above mentioned item: '))
    if item_type == 1: cost = p_cost * 1.5
    elif item_type == 2: cost = p_cost * 2.5
    elif item_type == 3: cost = p_cost * 5.0
    total += cost
    print('This is the item cost:', cost)

print('Average item cost per day:', total/1000)