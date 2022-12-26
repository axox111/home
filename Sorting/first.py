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
print(res)1