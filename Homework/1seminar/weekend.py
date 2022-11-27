# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print('This is not a number of a weekday')

def is_number(a):
    while a.isdigit() == False:
        a = input('Enter only numbers from 1 to 7 \n ')
    return int(a)

user_input = is_number(input('Enter number from 1 to 7 \n'))
checkNumber(user_input)