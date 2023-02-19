f = open("for_task1.txt", "r")
numbers = []

for i in f.read():
    if i.isdigit():
        numbers.append(i)

f.close()
print(numbers)