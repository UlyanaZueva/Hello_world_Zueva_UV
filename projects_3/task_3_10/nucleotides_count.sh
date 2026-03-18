#!/bin/bash

echo "Подсчет нуклеотидов в FASTA-файлах..."
echo ""

printf "%-20s %-10s %-10s %-10s %-10s\n" "Файл" "A" "T" "G" "C"
printf "%-20s %-10s %-10s %-10s %-10s\n" "--------------------" "----------" "----------" "----------" "----------"

for file in *.fasta; do
    [ -e "$file" ] || continue
   
    if [ ! -s "$file" ]; then
        echo "Пропущен пустой файл: $file"
        continue
    fi
    у
    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' ')
    
    if [ -z "$sequence" ]; then
        echo "В файле $file нет последовательности (только заголовки)"
        continue
    fi
    
    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)
    
    printf "%-20s %-10s %-10s %-10s %-10s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done

echo ""
echo "Подсчет завершен!"
