temperatures = []
max_temp = 0
min_temp = 1022

for count in range(0, 2):
    temp = float(input('Enter the temperature (Celsius) of hour no.' + str(count + 1) + ': '))
    temp = (temp * 9/5) + 32
    temperatures.append(temp)
    if temp > max_temp: max_temp = temp
    if temp < min_temp: min_temp = temp

print('The maximum temperature: (Fahrenheit)', max_temp)
print('The minimum temperature: (Fahrenheit)', min_temp)
print('The average temperature: (Fahrenheit)', round(sum([temp_val for temp_val in temperatures])/len(temperatures), 2))