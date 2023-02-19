n = str(input("Введите текст: "))

with open("data.txt", "w") as f:
    f.write(n)