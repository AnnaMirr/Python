# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input('Enter number:  ')

def summa(x): 

    # for i in str(x):
    # if i.isdigit():
    # number += int(i)
    # return number

    x = abs(float(x))
    number = 0

    # if float(x) < 0:                            
    #     x = float(x) * (-1)
    # number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'The sum of number is {summa(x)}')