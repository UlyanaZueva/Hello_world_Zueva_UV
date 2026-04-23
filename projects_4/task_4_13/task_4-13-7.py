a = [10, 20, 30, 40, 50]
n = len(a)

i = 0
summa = 0

while i < n:
    summa = summa + a[i]
    i = i + 1

average = summa / n

print("Среднее арифметическое массива:", average)
