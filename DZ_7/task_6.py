a = []
n = int(input("введите число : "))
while n > 0:
     a.append(int(input("Введите целое число : ")))
     n -= 1

minimum = a[0]
maximum = a[0]
for i in range(0,len(a)):
    if a[i] > maximum:
        maximum = a[i]

for i in range(0,len(a)):
    if a[i] < minimum:
        minimum = a[i]

print(f"Максимальное число {maximum} , минимальное число {minimum}")