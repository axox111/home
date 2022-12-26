#426
import math
    
def t(x):
    accNumerator = 0
    accDenominator = 0
    for k in range(maxRange + 1):
        accNumerator += (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        accDenominator += (x ** (2 * k)) / math.factorial(2 * k)
    return accNumerator / accDenominator
y = int(input("Введите y:"))
maxRange = 10
answer = (1.7 * t(0.25) + 2 * t(1 + y)) / (6 - t(y ** 2 - 1))
print(round(answer, 2))