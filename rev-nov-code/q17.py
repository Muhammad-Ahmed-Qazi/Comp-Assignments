data = []
level = 1
max_level = 0
total = 0

while level != 0:
    level = float(input('Enter sound level: (dB)(0 indicates end of data) '))
    data.append(level)

for item in data:
    total += item
    if item > max_level: max_level = item

print('Average sound level: (dB)', round(total / len(data), 2))
print('Highest recorded sound level: (dB)', max_level)