a = []
x = int(input("введите число : "))
while x > 0:
     a.append(int(input("Введите число : ")))
     x -= 1
a.reverse()
print(a)