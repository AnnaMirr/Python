# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint as ri

def get_list(n, frst, last):
    return [ri(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = 10
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))
