import time

file = open('generated list.txt', 'r')
numbers = [int(x) for x in file.read().split()] 
file.close()
lst_of_numbers = ''
file_bbl = open('sort by BUUBLES.txt', 'w')
start = time.time()
for j in range(len(numbers)): 
    for i in range(len(numbers) - 1- j): 
        issorted = True
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]   
# =============================================================================
#             issorted = False
#     if issorted:
#         break
# =============================================================================
end = time.time()
for i in numbers:
    lst_of_numbers += str(i) + ' '
file_bbl.write(lst_of_numbers)
file_bbl.close()
print(f"{round(end - start, 2)} сек.")
print(f"Сложность сортировки - O({(len(numbers) ** 2)})")