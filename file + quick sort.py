def qs(a):
    lower = []
    bigger = []
    temp_val = []
    temp_list = []
    if len(lower) > 0:
        for i in range(len(a)):
            if a[elem] > a[i]:
                lower.append(a[i])
    elif len(bigger) > 0:
        if a[elem] < a[i]:
            bigger.append(a[i])
    temp_val.append(a[elem])
    qs(lower)
    qs(bigger)
    temp_list = lower + temp_val + bigger
    print(temp_list)
    
            
a = [4, 7, 1, 2]
elem = 0#int(input("Выберете номер элемента в списке:"))
qs(a)