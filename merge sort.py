def merge_sort(x):
    first_list = []
    second_list=[]
    if len(x) > 1:
        list_middle = len(x) // 2
        for i in range(len(x)):
            if i < list_middle:
                first_list.append(x[i])
            else:
                second_list.append(x[i])
        merge_sort(first_list)
        merge_sort(second_list)
    elif len(x) == 1:
        i = j = 0
        final_list = []
        while i < len(first_list) and j < len(second_list):
            if first_list[i] < second_list[j]:
                final_list.append(first_list[i])
                i += 1
            else:
                final_list.append(second_list[j])
                j += 1
        
        

a = [10, 7, 9, 4, 6, 3, 1]
b = merge_sort(a)