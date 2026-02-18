
total_capsules = int(input("Введите общее количество произведенных капсул: "))
package_capacity = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_capsules // package_capacity
remaining_capsules = total_capsules % package_capacity

print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t\t{remaining_capsules}")
