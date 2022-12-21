"""
Вывести треугольник #1 с шириной N с помощью цикла while
"""
n = int(input("Введите число : "))
b = ["*"] * n

while len(b) > 0:
    print(''.join(b))
    b.pop()
