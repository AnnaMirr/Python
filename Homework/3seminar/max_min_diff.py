#  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

from random import uniform

def get_real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(a - int(a), 2) for a in (mynums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
mynums = get_real_nums(n, frst, last)

print (mynums)
print(find_diff(mynums))
print(int(find_diff(mynums) *10) % 10 )