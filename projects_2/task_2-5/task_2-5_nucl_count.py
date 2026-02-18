print("=== Анализ последовательности ДНК ===\n")
dna_sequence = input("Введите последовательность ДНК: ")
dna_upper = dna_sequence.upper()
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
count_A = dna_upper.count('A')
count_T = dna_upper.count('T')
count_G = dna_upper.count('G')
count_C = dna_upper.count('C')
    
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
    

total_length = len(dna_upper)
print(f"\nОбщая длина: {total_length} нуклеотидов")

if total_length > 0:  
    percent_A = (count_A / total_length) * 100
    percent_T = (count_T / total_length) * 100
    percent_G = (count_G / total_length) * 100
    percent_C = (count_C / total_length) * 100
        
    print("\nПроцентное содержание нуклеотидов:")
    print(f"A: {percent_A:.1f}%")
    print(f"T: {percent_T:.1f}%")
    print(f"G: {percent_G:.1f}%")
    print(f"C: {percent_C:.1f}%")
else:
    print("\nПоследовательность пуста, невозможно вычислить процентное содержание.")