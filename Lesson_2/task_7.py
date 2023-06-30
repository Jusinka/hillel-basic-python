# Написати програму "Показати зірки". На вхід приймає звичайне ціле число, має надрукувати кількість зірок:
def show_stars():
    num_stars = int(input("Input number of stars: "))
    stars = "*" * num_stars
    print(stars)

show_stars()