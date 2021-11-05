min_dense = 30000
max_dense = 0
total = 0

for count in range(0, 500):
    population = int(input('Enter the population of country no. ' + str(count + 1) + ': '))
    land = float(input('Enter the land area of country no. ' + str(count + 1) + ': (km^2) '))
    density = population / land
    if density < min_dense: min_dense = density
    if density > max_dense: max_dense = density
    total = total + density

print('Lowest population density: (people per km^2) ', min_dense)
print('Highest population density: (people per km^2) ', max_dense)
print('Average population density: (people per km^2) ', total / 500)