# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

def encode(path1, path2):
    '''encoding from path1 to path2'''
    with open(path1, 'r') as data:
        s = rle_encode(data.read())
    with open(path2, 'w') as data:
        data.write(s)

def decode(path1, path2):
    '''decoding from path1 to path2'''
    with open(path1, 'r') as data:
        s = rle_decode(data.read())
    with open(path2, 'w') as data:
        data.write(s)

print(rle_encode('aaabccccCCaB'))
print(rle_decode('3a1b4c2C1a1B'))

path1 = 'data_decode_dz3_4.txt'
path2 = 'data_encode_dz3_4.txt'

encode(path1, path2)
# decode(path2, path1)




# Интересное решение

import itertools

def compress(text):
    for char, same in itertools.groupby(text):        
        count = sum(1 for _ in same) # number of repetitions
        yield char if count == 1 else str(count)+char
''.join(compress("aaabccccCCaB")) # 3ab4c2CaB