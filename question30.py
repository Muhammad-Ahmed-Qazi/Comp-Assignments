passg = int(input('Enter the number of passengers: '))
start = int(input('Enter the station number where you are starting: '))
end = int(input('Enter the station number where you are ending: '))

if start > end:
    if passg > 2:
        fare = (start - end) * 2
        fare = fare * 0.9
    else:
        fare = (start - end) * 2
else:
    if passg > 2:
        fare = (end - start) * 2
        fare = fare * 0.9
    else:
        fare = (end - start) * 2

print('This is your fare for the journey:', fare)