start = int(input('Enter the starting station number: (1-10) '))
end = int(input('Enter the endign station number: (1-10) '))
passengers = int(input('Enter the number of passengers travelling: '))

stations = end - start

if stations < 0:
    stations *= -1

fare = stations * 2

if passengers > 2:
    fare = fare - (fare * 0.1)

print('This is the total amount to be paid: ($)', fare)

for count in range(0, passengers):
    print('Starting station:', start, '| Ending stations:', end, '| Passenger no.:', count + 1)