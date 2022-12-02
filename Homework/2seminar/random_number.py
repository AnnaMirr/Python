# Составьте алгоритм нахождения случайного числа без использования библиотеки random.

# import datetime 

# min_n = 10
# max_n = 100

# def get_rand():
#     return datetime.datetime.now().microsecond%10

# n = get_rand()

# print(int(len(str(min_n))))
# print(n)

import time

def random(min, max):
    range = max - min
    randomNumber = int(time.time_ns()*1000)
    randomNumber %= range
    randomNumber += min
    return randomNumber

while True:
    try:
        min = int(input('Введите начало диапазона для генерации случайного числа: '))
        max = int(input('Введите конец диапазона для генерации случайного числа: '))
        print(random(min, max))
        break
    except:
        print('Введенное значение не является числом!')