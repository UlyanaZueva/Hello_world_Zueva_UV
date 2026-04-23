a = [10, 15, 20, 23, 30, 37, 42, 45]
n = len(a)

i = 0
summa = 0
count = 0

while i < n:
    if i % 2 == 0:
        summa = summa + a[i]
        count = count + 1
    i = i + 1

if count > 0:
    average = summa / count
    print("Среднее арифметическое элементов с чётными индексами:", average)
else:
    print("В массиве нет элементов с чётными индексами")
    