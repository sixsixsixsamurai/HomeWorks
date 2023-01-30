a = input("Введите количество файлов: ")
set_conf_user = {}
q = 0


while int(a) > q:
    z = input("Введите имя файла: ")
    x = input(f"Введите допустимые операции с {z} файлом: ").upper()
    set_conf_user[z] = x
    q += 1

input_score = input("Введите количество запросов к файлам: ")
q = 0
user_conf = {}
result = []


while int(input_score) > q:
    input_get_name = input(f"К какому файлу будет запрос? ")
    input_get_value = input(f"Вид операции к {input_get_name} файлу? ").lower()


    if input_get_name in set_conf_user.keys():
        if input_get_value == "read":
            for i in set_conf_user.keys():
                if input_get_name == i:
                    if "R" in set_conf_user.get(i):
                        result.append("OK")
                    else:
                        result.append("Access denied")
        elif input_get_value == "write":
            for i in set_conf_user.keys():
                if input_get_name == i:
                    if "W" in set_conf_user.get(i):
                        result.append("OK")
                    else:
                        result.append("Access denied")
        elif input_get_value == "execute":
            for i in set_conf_user.keys():
                if input_get_name == i:
                    if "X" in set_conf_user.get(i):
                        result.append("OK")
                    else:
                        result.append("Access denied")
    else:
        print(f"{input_get_name} <-- такого файла не существует")
    q += 1

for i in result:
    print(i)