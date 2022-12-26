#317 Даны действительные числа а1...а10. Вычислить а1 + а2**2 +...+ a10**10
a = int(input("Введите первое число:"))
res = 0
for n in range(1, 10 + 1):
    multiply = 1
    for i in range(n):
        multiply *= a
    res += multiply
    a += 1
print(f"Результат: {res}")