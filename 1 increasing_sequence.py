# 1. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

import random

def random_list(size):
    return [random.randint(1, 10) for i in range(size)]

def output_list(list):
        return [i for i in set(list)]

size_list = int(input('Введите количество чисел в списке: '))
input_list = random_list(size_list)
print(input_list)
print(output_list(input_list))