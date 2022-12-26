import math

def binary_search(lst, elem, start, end):
    pos = math.ceil((start + end) / 2)
    mid = len(lst) // 2
    if len(lst) == 0:
        return -1
    if lst[mid] == elem:
        return print(f"Индекс искомого элемента {pos}")
    if elem < lst[mid]:
        temp_list = lst[:mid]
        return binary_search(temp_list, elem, start, pos - 1)
    else:
        temp_list = lst[mid:]
        return binary_search(temp_list, elem, pos, end)

base_file = open('sorted by quick sort.txt', 'r')
numbers = [int(i) for i in str(base_file.read()).split()]
base_file.close()
# =============================================================================
# print(numbers) Если есть желание выбрать элемент из списка
# =============================================================================
searched_elem = int(input('Введите искомое знеачение:'))
binary_search(numbers, searched_elem, 0, len(numbers) - 1)