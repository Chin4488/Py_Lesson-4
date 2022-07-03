# 2.	Создать и заполнить файл случайными целыми значениями.
#  Выполнить сортировку содержимого файла по возрастанию.

from random import randint

size_list = int(input('Введите количество чисел в списке: '))

with open('unsorted_data.txt','w') as write_file:
    for i in range (size_list): write_file.write(str(randint(1,100))+',')

with open('unsorted_data.txt','r') as read_file:
    list = read_file.readline().split(',')
    list.pop()
    print (sorted(map(int, list)))