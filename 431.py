#431
def h(a, b):
    return (a / (1 + b**2)) + (b / (1 + a**2)) - (a - b)**3

s = 5
t = 2
answer = h(s, t) + max(h(s - t, s * t)**2, h(s - t, s + t)**4) + h(1, 1)
print(answer)