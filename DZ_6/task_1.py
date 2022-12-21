password = input("Введите ваш пароль : ")
password_score = 0
feedback = ""

if len(password) >= 8:
    password_score += 1
else:
    feedback += "\nВаш пароль слишком короткий (используйте 8+ символов)"

for char in password:
    if char.isdigit():
        password_score += 1
        break
else:
        feedback += "\nДобавьте хотя бы одну цифру в ваш пароль"

for char in password:
    if char.isupper():
        password_score += 1
        break
else:
    feedback += "\nДобавьте хотя бы одну большую букву"

for char in password:
    if char.islower():
        password_score += 1
        break
else:
    feedback += "\nДобавьте хотя бы одну маленькую букву"

for char in password:
    if char.isalnum() == False:
        password_score += 1
        break
else:
    feedback +="\nДобавьте хотя бы один спец.символ"

if password_score < 5:
    print(f"Ваша оценка за пароль {password_score} баллов \nВот наши рекомендации для улучшения вашего пароля {feedback}")
else:
    print(f"Ваша оценка за пароль {password_score} баллов , ваш пароль превосходен")