#334 
#а)
i = 1
imax = 100
j = 1
jmax = 50
res = 0
for k in range(i, imax + 1):
    for n in range(j, jmax + 1):
        res += 1 / (k + n ** 2)
print(f"Результат этой агонии - {round(res, 2)}")
#г)
i = 1
imax = 5
j = 1
res = 0
for k in range(i, imax + 1):
    for n in range(j, i + 1):
        res += 1 / (2 * n + k)
    i += 1
print(f"Результат этой агонии - {round(res, 2)}")