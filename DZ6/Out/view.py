import Input
import BaseData


def view(data):    
    for key in data:
        print(f'{key} {data[key]}')


def view1(human, state):
    print('  %20s %8s   Кем занята' % ('Должность'.ljust(20), 'Зарплата'))
    for key, val in state.items():
        if val[2] != 0:
            print(f'{key} {state[key][0]:20} {state[key][1]:8}   {human[val[2]]}')
        else:
            print(f'{key} {state[key][0]:20} {state[key][1]:8}')
    