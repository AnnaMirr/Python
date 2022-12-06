# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

def get_numbers(n, frst, last):
    return [randint(frst, last) for i in range(n)]

n = 9
frst = 1
last = 10

mylist = get_numbers(n, frst, last)
print(mylist)

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) == 1: results.append(numbers[0]**2)       
    return results

print(pairs_mult(mylist))