import time

def qs(a):
    if len(a) <= 1:
        return a
    
    elem = a[0]
    left = list(filter(lambda x: x < elem, a))
    center = [i for i in a if i == elem] 
    right = list(filter(lambda x: x > elem, a))
    return qs(left) + center + qs(right)
    
base_file = open('generated list.txt', 'r')
x = base_file.read().split()
numbers = [int(i) for i in x]
start = time.time()
sorted = qs(numbers)
print(f"жесть чё быстрая сортировка делает за {round(time.time() - start,2)} сек.")
quick_sort_file = open('quick sort file.txt', 'w')
for i in sorted:
    quick_sort_file.write(str(i) + ' ')
