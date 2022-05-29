def save_book(sl):    
    with open(r'HelloPython\DZ5\Out\book.txt', 'w') as data:
        for val in sl.values():            
            data.write(val[0] + ' ' + val[1] + '\n') #  равнозначно print(val, file=data)