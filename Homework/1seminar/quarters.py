# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quart = int(input('Enter the quarter number \n'))
if quart == 1:
    print('x∈(0, ∞) u y∈(0, ∞)')
elif quart == 2:
    print('x∈(0, -∞) u y∈(0, ∞)')
elif quart == 3:
    print('x∈(0, -∞) u y∈(0, -∞)')
elif quart == 4:
    print('x∈(0, ∞) u y∈(0, -∞)')
else:
    print('Incorrect input')
