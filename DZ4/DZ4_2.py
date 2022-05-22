# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())

def hi(i):
    global n    
    while n%i == 0:        
        n/=i
        return i           

d = list(filter(hi, [i for i in range(2,int(n**0.5)+1)]))
if n > 2:    
    d.append(int(n))
print(d)