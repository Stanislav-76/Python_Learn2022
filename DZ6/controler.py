import Input
import Out
import BaseData
import ast


human = {}
state = {}
try:
    human = ast.literal_eval(Input.read_human())
    state = ast.literal_eval(Input.read_state())
except:
    print('Отсутствует файл(ы)')


move = {1:'Добавить сотрудника', 2: 'Вывести список', 3:'Должности', 4:'Удалить сотрудника', 5:'Выход'}

def start():
    while True:
        print('Выберите операцию', move)
        n = int(input())
        if n == 1:
            BaseData.add_human(human)
        if n == 2:
            Out.view(human)
        if n == 3:
            n1 = int(input('Выберите операцию 1: Добавить должность. 2: Вывести должности 3: Удалить должность 4: Назначить\n'))
            if n1 == 1:
                BaseData.add_state(state)
            if n1 == 2:            
                Out.view1(human, state)
            if n1 == 3:
                BaseData.del_state(state)
            if n1 == 4:
                BaseData.assign(state, human)
        if n == 4:        
            print('Введите id ')
            id = input('Введите id')
            BaseData.del_human(human)        
        if n == 5:
            break