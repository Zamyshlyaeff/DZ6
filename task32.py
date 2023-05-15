# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random
list1=[random.randint(1,20) for i in range(15)]
print(list1)
list2=[]
for i in range(len(list1)):
    if 5<list1[i]<15:
        list2.append(i)

print(list2)