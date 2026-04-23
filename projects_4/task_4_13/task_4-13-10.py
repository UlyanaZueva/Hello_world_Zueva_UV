a = [10, 15, 20, 23, 30, 37, 42, 45]
n = len(a)

i = 0
summa = 0

while i < n:
    if i % 2 != 0:
        summa = summa + a[i]
    i = i + 1

print("Сумма элементов с нечётными индексами:", summa)