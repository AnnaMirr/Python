# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
## В основе теорема Пифагора 

x1 = int(input('Enter x-number for first point \n'))
y1 = int(input('Enter y-number for first point \n'))
x2 = int(input('Enter x-number for second point \n'))
y2 = int(input('Enter y-number for second point \n'))

ac = y2 - y1
bc = x2 - x1
print(round((ac ** 2 + bc ** 2) ** 0.5, 2))