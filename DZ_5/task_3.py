"""
Вывести треугольник #3 с шириной N с помощью цикла while
"""
n = int(input("Введите число : "))
b = ["*"] * n
while n > 0:
    print("".join(b))
    n -= 1
    b.pop()
    b.insert(0, " ")
