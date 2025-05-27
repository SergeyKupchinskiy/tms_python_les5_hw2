# Задание 6*
# Напишите в коде случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
# Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
# Если пользователь ввел число, которое не попало в диапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
# Если пользователь ввел число больше загаданного, выведите сообщение "Загаданное число меньше".
# Если пользователь ввел число меньше загаданного, выведите сообщение "Загаданное число больше".
# Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.


x = 69

print("Guess a number from 1 to 100: ")

while True:
    y = input("Enter a number: ")

    if not y.isdigit():
        print("its not a number, try again")
        continue

    number = int(y)

    if number < 1 or number > 100:
        print("number out of range, try again")

    elif number > x :
        print("The number guessed is less, try again")

    elif number < x :
        print("The number guessed is greater, try again")

    elif number == x :
        print("You guessed it!!! Congrats!")
        break
