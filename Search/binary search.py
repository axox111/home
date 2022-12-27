import math

def binary_search(lst, elem, start, end):
    pos = math.ceil((start + end) / 2)
    mid = len(lst) // 2
    if len(lst) == 0:
        return -1
    if lst[mid] == elem:
        return print(f"Индекс искомого элемента {pos}")
    if elem < lst[mid]:
        return binary_search(lst[:mid], elem, start, pos - 1)
    else:
        return binary_search(lst[mid:], elem, pos, end)

base_file = open('quick sort file.txt', 'r')
numbers = [int(i) for i in str(base_file.read()).split()]
base_file.close()
# =============================================================================
# print(numbers) Если есть желание выбрать элемент из списка
# =============================================================================
searched_elem = int(input('Введите искомое знеачение:'))
binary_search(numbers, searched_elem, 0, len(numbers) - 1)