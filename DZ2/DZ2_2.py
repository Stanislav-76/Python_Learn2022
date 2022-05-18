# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input())
lst = []
for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        lst.append(i)
        n /= i            
    if n == 1:
        break
print(lst)