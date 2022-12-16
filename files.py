file = open('rokalo.txt', 'r')
new_value = ''
new_rokalo = 0
for row in file:
    for i in row:
        new_value += str(int(i) * 5)
print(new_value)
new_rokalo = open('new_rokalo.txt', 'w')
new_rokalo.write(new_value)
file.close()
new_rokalo.close()