a = [10, -5, 20, -8, 30, 0, 15, -3]
n = len(a)

i = 0
count = 0

while i < n:
    if a[i] > 0:
        count = count + 1
    i = i + 1

print("Количество положительных чисел в массиве:", count)
