# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

# Работает для многочленов с одинакой max степенью
# Есть идея через словарь: степень - ключ(++ разные степени можно добавлять, порядок не важен)

file_1 = 'test1_dz2_5.txt'
file_2 = 'test2_dz2_5.txt'

def spisok(file_name):
    data = open(file_name, 'r')
    dataRead = data.read()    
    print(dataRead)
    s = ''
    resData = []
    for i in range(len(dataRead)-1):
        if dataRead[i].isdigit():
            s += dataRead[i]  
        elif s != '':
            resData.append(s)
            s = ''
    data.close()
    return resData

resData1 = spisok(file_1)
resData2 = spisok(file_2)

print(resData1)
print(resData2)

with open('res_dz2_5.txt', 'w') as data:
    for i in range(1, len(resData1), 2):
        if i < len(resData1) - 2:
            data.write(f'{int(resData1[i-1]) + int(resData2[i-1])}*x**{resData1[i]} + ')
        else:
            data.write(f'{int(resData1[i-1]) + int(resData2[i-1])}*x + {int(resData1[i]) + int(resData2[i])} = 0')