# Надрукувати всі числа, які діляться на 5 без залишку, але не більше 150.

list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

for num in list_of_six:
    if num % 5 == 0 and num <= 150:
        print(num)