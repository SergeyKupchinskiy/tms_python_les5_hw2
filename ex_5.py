# Задание 5
# На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# Для каждого параметра: если введенные данные не соответствуют требованиям
# (например, username должен быть длиной от 3 до 20 символов),
# выведите сообщение об ошибке и попросите ввести данные заново.
# Создайте словарь с данными пользователя и выведите его в консоль.


new_dict ={}

while True:
    login = input("Enter your login: ")
    if len(login) >= 6 and len(login) <= 20:
        new_dict["login"] = login
        break
    else:
        print("Wrong login. Please try again.")

while True:
    email = input("Enter your email: ")
    if "@" in email and "." in email:
        new_dict["email"] = email
        break
    else:
        print("Wrong email. Please try again.")

while True:
    name = input("Enter your name: ")
    if  len(name) > 0:
        new_dict["name"] = name
        break
    else:
        print("Wrong name. Please try again.")

while True:
    surname = input("Enter your surname: ")
    if  len(surname) > 0:
        new_dict["surname"] = surname
        break
    else:
        print("Wrong surname. Please try again.")


print("User data:")
print(new_dict)

