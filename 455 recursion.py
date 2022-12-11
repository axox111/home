def nod(n, m):
    if n % m == 0:
        return m
    if n % m != 0:
        r = n % m
        n = m
        m = r
    return nod(n, m)
    
n = int(input("Введите первое число:"))
m = int(input("Введите второе число:"))
r = 0
print(nod(n, m))