"""
Вывести треугольник #2 с шириной N с помощью цикла while
"""
n = int(input("Введите число : "))
b = ["*"]

while n > 0:
    n -= 1
    print("".join(b))
    b.append("*")
