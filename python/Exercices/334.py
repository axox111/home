#334 
#а)
i_min_range = 1
i_max_range = 100
j_min_range = 1
j_max_range = 50
res = 0
for k in range(i_min_range, i_max_range + 1):
    for n in range(j_min_range, j_max_range + 1):
        res += 1 / (k + n ** 2)
print(f"Результат а агонии - {round(res, 2)}")
#г)
i_min_range = 1
i_max_range = 5#100
j_min_range = 1
res = 0
for i in range(i_min_range, i_max_range + 1):
    for j in range(j_min_range, i + 1):
        res += 1 / (2 * j + i)
print(f"Результат г агонии - {round(res, 2)}")