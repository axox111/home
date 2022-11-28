#198 
n = 7 #int(input("n = "))
x = 0
res = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        x = i ** 2
    elif i % 3 == 1:
        x = i
    else:
        x = i / 3
    res += x
print(res)

#279Даны действительные числа а1, ..., аn, b1, ..., bn.
#вычислить (a1 + bn) * (a2 - bn-1) * ... * (an + b1)
n = 10
al = []
bl = []
s = 0
ss = 0
res = 1
for i in range(1, n + 1):
    al.append(i)
    bl.append(i)
bl.reverse()
while s < n:
    ss = al[s] + bl[s]
    res *= ss
    s +=1
print(res)