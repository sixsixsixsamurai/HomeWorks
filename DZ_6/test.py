password = input("Введите ваш пароль : ")
for char in password:
    if char == "!" or char == "@" or char == "#":
        print("+")
        break
else:
    print("net !@#$%^&*(")

