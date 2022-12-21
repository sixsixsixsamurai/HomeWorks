"""
Вывести треугольник #4 с шириной N с помощью цикла while
"""
n = int(input("Введите число : "))
b = [" "] * n
while n > 0:
    n -= 1
    b.pop(0)
    b.append("*")
    print("".join(b))
