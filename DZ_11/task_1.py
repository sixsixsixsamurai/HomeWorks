n = int(input("Введите количество файлов: "))
result = []
files = {}
for i in range(n):
    file, *option = input("Введите имя файла который хотите создать и операции допустимые к этому файлу: ").split()
    files[file] = set(option)
print(files)
m = int(input("Введите количество операций: "))
for i in range(m):
    op, file = input("Введите операцию которую хотите произвести и название файла к которому будет применена операция: ").split()
    if op == "read":
        op = "R"
    elif op == "write":
        op = "W"
    elif op == "execute":
        op = "X"
    if op in files[file]:
        result.append("OK")
    else:
       result.append("Access denied")

for i in result:
    print(i)
