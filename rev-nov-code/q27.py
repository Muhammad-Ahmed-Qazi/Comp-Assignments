tot_height = 0
tot_weight = 0
count = 0

while count < 1000:
    print(count)
    height = float(input('Enter your height: (m) '))
    weight = float(input('Enter your weight: (kg) '))
    if height < 1 or weight < 1: continue
    tot_height += height
    tot_weight += weight
    count += 1
    
print('Average height:', tot_height / 1000, '| Average weight:', tot_weight / 1000)