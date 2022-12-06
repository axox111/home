#302 введите число. сколько в нем уникальных цифр
n = int(input("введите число"))
res = [int(x) for x in str(n)]
print(set(res))