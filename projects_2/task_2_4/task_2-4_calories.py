weight_proteins = float(input("Введите массу белков в продукте (г): "))
weight_fats = float(input("Введите массу жиров в продукте (г): "))
weight_carbohydrates = float(input("Введите массу углеводов в продукте (г): "))

caloric_content = (weight_proteins * 4) + (weight_fats * 9) + (weight_carbohydrates * 4)

print(f"Общая калорийность (ккал): {caloric_content} ")
