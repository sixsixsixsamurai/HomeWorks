a = []
c = []
x = 5
while x > 0:
     a.append(int(input("Введите целое число : ")))
     x -= 1

for i in a:
    if int(i) > 5:
        c.append(i)
        continue
print(c)