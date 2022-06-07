"""Игра: Угадай число от 1 до 100, меньше чем за 20 попыток"""

import random
 
errors = 0
secret = random.randint(0, 20)
 
while errors < 6:
    number = input()
    if number.isdigit():
        number = int(number)
        if number < secret:
            print("Число меньше загаданного!")
        elif number > secret:
            print("Число больше загаданного!")
        else:
            print(f"Вы угадали число - {secret}!")
            break
        errors += 1
    else:
        print("Введено не число")
else:
    print(f"Число: {secret} так и не было угадано!")
