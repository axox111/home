#Числа Фиббоначи
def fib(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    if x > 2:
        return fib(x - 1) + fib(x - 2)

x = 22
print(f"{x} элемент является число {fib(x)}")