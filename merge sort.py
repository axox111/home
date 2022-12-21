def merge_sort(x):
    if len(x) == 1:
        return x
    else:
        elem = len(x) // 2
        first_list = merge_sort(x[:elem])
        second_list = merge_sort(x[elem:])
        return merge_sorting(first_list, second_list)

def merge_sorting(x, y):
    i = j = 0
    final = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            final.append(x[i])
            i += 1
        else:
            final.append(y[j])
            j += 1
    if i < len(x):
        final += x[i:]
    if j < len(y):
        final += y[j:]
    return final
            
a = [10, 7, 9, 4, 6, 3, 1, 2]
print(a)
b = merge_sort(a)
print(b)