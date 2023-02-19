n = int(input("Введите число N: "))

numbers = []
for i in range(n):
    number = input("Введите число: ")
    numbers.append(number)


with open("numbers.txt", "w") as f:
    f.write(" ".join(numbers))