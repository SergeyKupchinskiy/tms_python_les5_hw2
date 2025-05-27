# Задание 1
# Через цикл вывести в консоль все элементы списка.
# Используя цикл, вывести в консоль все элементы списка в обратном порядке.
# Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.


list1 = ['apple', 'banana', 'cherry']

for item in list1:
    print(item)

print("-" * 50)

for item in reversed(list1):
    print(item)

print("-" * 50)

for item in list1:
    print(item[::-1])