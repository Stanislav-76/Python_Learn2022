import Input

  
def add_human(human):    
    print(human)
    id = input('Введите id ')
    human[id] = Input.human()
    with open(r'HelloPython\PZ8\BaseData\human.txt', 'w') as data:
        data.write(str(human))

def add_state(state):    
    print(state)
    id = input('Введите id ')
    state[id] = list(Input.state())
    with open(r'HelloPython\PZ8\BaseData\state.txt', 'w') as data:
        data.write(str(state))

def del_human(human):
    print(human)
    id = input('Введите id ')
    del human[id]
    with open(r'HelloPython\PZ8\BaseData\state.txt', 'w') as data:
        data.write(str(human))

def del_state(state):
    print(state)
    id = input('Введите id ')
    del state[id]
    with open(r'HelloPython\PZ8\BaseData\state.txt', 'w') as data:
        data.write(str(state))

def assign(state, human):
    print(state)
    id_s = input('Введите id ')
    print(human)
    id_h = input('Введите id ')
    state[id_s][2] = id_h
    with open(r'HelloPython\PZ8\BaseData\state.txt', 'w') as data:
        data.write(str(state))
