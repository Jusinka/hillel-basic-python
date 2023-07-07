# Користувач вводить число `X`, яке має два знаки після десяткової точки.
# Виведіть його дрібну частину.Виведіть першу цифру після десяткової точки.
user_input = float(input('x з двома знаками після  десятковоі'))

user_number = str(user_input)

part_1 = user_number.split('.')[1]

print(part_1)

part_2 = part_1[0]

print(part_2)

