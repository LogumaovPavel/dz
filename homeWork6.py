#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:

def progress(*args):
    for i in range (1,c):
        array.append(a+i*b)
    return array 

a = int (input("введите первый элемент массива: "))
b = int (input("введите разность: "))
c = int (input("введите количество элементов массива: "))
array = []
array.append(a)

print("получился массив ->", progress(a,b,c,array))


# ; Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

a = int(input("введите количество элементов массива: "))
array = []
for i in range (a):
    el = int(input("введите "+str(i)+" элемент массива: "))
    array.append(el)
min = int(input("введите минимальный элемент диапазона: "))
max = int(input("введите максимальный элемент диапазона: "))
new_Array = []
for i in range (len(array)):
    if array[i] >= min and array[i] <= max:
        new_Array.append(i)
print("индекс элементов -> ", new_Array)