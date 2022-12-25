a = input("Ввод :")
b = 0

for i in a:
    if i.isdigit():
        b += 1
    continue
print(f"Количество цифр в тексте : {b}")