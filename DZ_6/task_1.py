password = input("Введите ваш пароль : ")
password_score = 0
feedback = " "
#проверка на длину 8+ строк
if len(password) >= 8:
    password_score += 1
else:
    feedback += "\nВаш пароль слишком короткий (используйте 8+ символов)"
    #проверка на хоть одину цифру
for char in password:
    if char.isdigit():
        password_score += 1
        break
else:
        feedback += "\nДобавьте цифры в ваш пароль"
# проверка на верхний регистр
for char in password:
    if char.isupper():
        password_score += 1
        break
else:
    feedback += "\nТребуется хотя бы одна большая буква"
    #провверка на нижний регистр
for char in password:
    if char.islower():
        password_score += 1
        break
else:
    feedback += "\nТребуется хотя бы одна маленькая буква"


print(f"Ваша оценка за пароль {password_score} , вот фид бек : {feedback}")