# Напишите программу, удаляющую из текста все слова, содержащие "абв".

s = 'Чем ниже человек кабвар душой, тем выше абвер задирает нос.\nОн носом чвабва тянется туда, куда абвер душою не дорос.'
# print(s)
my_str = s.split()
for i in my_str:      
    if i.find('абв') != -1:        
        s = s.replace(i, '')
s = s.replace('  ', ' ')
print(s)