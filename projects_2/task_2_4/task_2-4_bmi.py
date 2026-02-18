weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))
bmi = weight / (height ** 2)
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height} см\nВес:\t{weight} кг\nИндекс массы тела пациента: {bmi:.2f}")

