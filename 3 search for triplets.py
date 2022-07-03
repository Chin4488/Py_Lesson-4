# 3.	Вот вам файл с тысячей чисел. 
# https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран.
# Триплетом называются три числа, которые в сумме дают 0.

from itertools import combinations

with open('1Kints.txt') as inp:
    numbers = [int(i) for i in inp.read().split()]

def findTriplets(arr, key):
    def valid(val):
        return sum(val) == key
    return list(filter(valid, list(combinations(arr, 3))))

print(findTriplets(numbers, 0))