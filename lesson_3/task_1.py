# . Користувач вводить трицифрове число. Знайдіть суму його цифр. [опціонально]
a = input("Enter there numb")

result = 0

for num in a:
    if not num.isdigit():
        continue

    result += int(num)

print(result)
