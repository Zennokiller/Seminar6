# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int (input("Введите количество элеменотов в прогрессии, n= "))
a1 = int (input("Введите первый лемент прогрессии, a1= "))
d = int (input("Введите разность, d= "))

a = [0]*n  #создали массив из n элементов и заполнили его нулями
for i in range(0, n):
    if i==0:
        a[i] = a1
    else:
        a[i]=a1+((i-1)+1)*d
print(a)