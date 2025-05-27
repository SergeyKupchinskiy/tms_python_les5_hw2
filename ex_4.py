# Задание 4
# На вход пользователь вводит предложение (использовать функцию input).
# Посчитайте количество слов в предложении и выведите результат в консоль.
# Используя цикл, выведите в консоль все слова предложения в обратном порядке.
# Используя цикл, создайте словарь, где ключами являются длина слов,
#           а значениями - список слов в предложении с такой длиной.

new_str = input("Введите предложение: ")

words_count = len(new_str.split())
print("Количество слов в предложении:", words_count)

print("-" * 50)

for i in reversed(new_str.split()):
    print(i)

print("-" * 50)

words = new_str.split()

new_dict = {}

for i in words:
    lenght = len(i)
    if lenght not in new_dict:
        new_dict[lenght] = [i]
    else:
        new_dict[lenght].append(i)

print("словарь:", new_dict)