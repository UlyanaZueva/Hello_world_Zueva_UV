
N = int(input("Введите число N: "))

if N < 0:
    print("Ошибка: N должно быть неотрицательным числом.")
else:
    summa = 0
    i = 1
    
    while i <= N:
        summa = summa + i
        i = i + 1

    print(f"Сумма первых {N} натуральных чисел = {summa}")
    
    