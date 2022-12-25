a = []
x = 3
while x > 0:
     a.append(int(input("Введите число : ")))
     x -= 1

n = int(input("Введите число : "))
print(a.count(n))