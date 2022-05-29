import Input
    
def human():
    return input('Введите ФИО: ')

def state():
    position = input('Наименование должности: ')
    salary = input('Зарплата: ')
    return position, salary, 0

def read_human():       
    with open(r'HelloPython\PZ8\BaseData\human.txt', 'r') as data:
        return data.read()

def read_state():       
    with open(r'HelloPython\PZ8\BaseData\state.txt', 'r') as data:
        return data.read()