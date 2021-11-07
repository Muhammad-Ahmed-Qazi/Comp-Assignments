stat = 1
data = {'bun': 0, 'coffee': 0, 'cake': 0, 'sandwich': 0, 'dessert': 0}

while stat == 1:
    item = input('Enter the item sold: (1: bun, 2: coffee, 3: cake, 4: sandwich, 5: dessert) ')
    if item == '1': data['bun'] += 1
    elif item == '2': data['coffee'] += 1
    elif item == '3': data['cake'] += 1
    elif item == '4': data['sandwich'] += 1
    elif item == '5': data['dessert'] += 1
    elif item == 'end': break

total = (data['bun'] * 0.5) + (data['coffee'] * 1.2) + (data['cake'] * 1.5) + (data['sandwich'] * 2.1) + (data['dessert'] * 4)
print('Total takings for the day:', total)

print(data)
print(sorted(data.values()))

# How to iterate througn a dictionary | Make two lists
for key, val in data.items():
    if val == sorted(data.values())[4]:
        print('Type of item having highest takings:', key.capitalize())