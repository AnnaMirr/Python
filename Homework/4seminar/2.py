#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.



# a= [1,2,2,2,2,3,1,4]

# print(set(a))

from typing import List

def get_unical_num(num: List[int]) -> List[int]:
    mul = []
    for i in num:
        if not mul.count(i):
        # if i not in mul:
            mul.append(i)
        mul.sort()
    return mul

pos = '1,1,1,2,2,3,3,5,2,7,7,7,8,4,4,4'
num = list(map(int,pos.split(',')))
result = get_unical_num(num)
print(f'Unical list of numbers {num} -> {result}')