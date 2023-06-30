# "Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (Прогалини важливі!)"
# Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:
nubmer = int(input(" Please enter an integer number"))
a = nubmer - 1
b = nubmer + 1
print("Previous number for numbe {} is {}".format(nubmer,a))
print("Next number for number {} is {}".format(nubmer,b))