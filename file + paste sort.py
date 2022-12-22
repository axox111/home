import time

file = open('generated list.txt', 'r')
numbers = [int(x) for x in file.read().split()]
file.close()
file_paste = open("sort by paste.txt", 'w')
temp_val = ''
start = time.time()
for j in range(1, len(numbers)):
    for i in range(j, 0, -1):
        if numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
        else:
            break
end = time.time() - start
for i in numbers:
    temp_val += str(i) + ' '
file_paste.write(temp_val)
file_paste.close()
print(f"А этот код занял {round(end, 2)} секунд.")
print(f"Сложность сортировки - O({round(len(numbers) ** 2, 2)}))")