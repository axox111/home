#быстрая сортировка
def sort(x):
    for i in a:
        lower = []
        bigger = []
        for j in range(len(a)):
            if a[0] > a[j]:
                lower.append(a[j])
            else:
                bigger.append(a[j])
            sort(lower)
            sort(bigger)

a = [7, 5, 3, 4, 8, 1, 5]
print(sort(a))


            