# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка

x = int(input('Enter number for x \n'))
y = int(input('Enter number for y \n'))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
elif x == 0 and y == 0:
    print('Incorrect input')
elif x == 0:
    print('Y-axis')
else:
    print('X-axis')
