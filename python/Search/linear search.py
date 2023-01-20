def linear_search(lst, elem):
    for i in range(len(numbers) - 1):
        if numbers[i] == elem:
            return print(f"Искомый элемент имеет индекс {i}")
    else:
        return -1

searched_elem = int(input('Введите искомое значение:'))
base_list = open('sorted by quick sort.txt', 'r')
numbers = [int(i) for i in str(base_list.read()).split()]
base_list.close()
print(numbers)
linear_search(numbers, searched_elem)