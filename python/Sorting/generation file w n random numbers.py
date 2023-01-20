#сгенерировать в файл n рандоманых чисел. формат "a1 a2 a3 ... an".
import random

a = int(input("Введите число значени:"))
a_min = 0
a_max = 10000
file = open("generated list.txt", 'w')
numbers = [random.randint(a_min, a_max) for x in range(a)]
for i in numbers:
    file.write(str(i) + ' ')
file.close()