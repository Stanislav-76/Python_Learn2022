# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


n = 2021
if random.randint(0, 1) == 0:
    x = 'Игрок'
else:
    x = 'Бот'
print(f'Игру начинает {x}')    
while n > 0:
    if x == 'Бот':
        if n%29 != 0:
            konfet = n%29
        else:
            konfet = random.randint(1, 28)
        print(f'{x} взял конфет {konfet}')
    else:
        konfet = int(input(f'{x} взял конфет (не более 28): '))    
    if 0 < konfet < 29 and konfet <= n:        
        n -= konfet
        if n == 0:
            break
        print(f'Осталось {n} конфет.')
        if x == 'Игрок':
            x = 'Бот'
        else:
            x = 'Игрок'
    else:
        print('Ошибка. Введите число конфет правильно от 1 до 28.')
print(f'Выиграл {x}')