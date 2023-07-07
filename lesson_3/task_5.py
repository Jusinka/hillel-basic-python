# Користувач вводить число від 1 до 10, програма генерує рандомне число від 1 до 10, якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'. Дати користувачеві три спроби;)

import random


random_number = random.randint(1, 10)
attempts = 3


while attempts > 0:
    user_input = int(input('Число від 1 до 10'))
    if user_input == random_number :
        print('You Won')
        break
    else:
        print('you lose')
        attempts -= 1

if attempts == 0 :
    print('Не залишилося спроб вдачи внаступний раз')
