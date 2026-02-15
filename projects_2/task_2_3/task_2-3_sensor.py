operator_name = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")


with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("Оператор\tЗначение")
    file.write(f"\n{operator_name}\t\t{pressure}") 


print("Данные успешно сохранены в sensor_log.txt")
