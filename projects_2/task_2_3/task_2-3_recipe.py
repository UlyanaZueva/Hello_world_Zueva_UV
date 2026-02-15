nutrient_medium = input("Введите название питательной среды: ")
concentration = input("Введите концентрацию агара (%): ")
temperature = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"\t{nutrient_medium.upper()}\n")
    file.write(f"Концентрация агара (%): {concentration}\n")
    file.write(f"Температура стерилизации (°C): {temperature}")

print("Файл 'recipe.txt' успешно сформирован!")

