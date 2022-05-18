# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


my_list = []
n = int(input('Введите количество элементов: '))
for i in range(n):
    my_list.append(int(input()))
print(my_list)
for i in range(n):
    if my_list.count(my_list[i]) == 1:
        print(my_list[i], end=' ')