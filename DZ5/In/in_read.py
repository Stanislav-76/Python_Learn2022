def read_book():    
    with open(r'HelloPython\DZ5\Out\book.txt', 'r') as data:        
        return dict(enumerate(val.split() for val in data))                