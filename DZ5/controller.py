import In
import Out

book = In.read_book()

def view():
    Out.view_data(book)

def create():
    view()    
    id = int(input('Введите id ')) 
    contact = In.data_create()
    book[id] = [contact[0], contact[1]]
    Out.save_book(book)
    print('Контакт добавлен')

def delete():    
    view()
    id = int(input('Введите id '))
    del book[id]
    Out.save_book(book)
    print('Контакт удален')