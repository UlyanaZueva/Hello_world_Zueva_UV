#!/bin/bash
if [ ! -f students.txt ]; then
    echo "Ошибка: файл students.txt не найден!"
    exit 1
fi
echo "Сумма оценок:"
awk '{sum += $2} END {print sum}' students.txt
echo -e "\nСредняя оценка:"
awk '{sum += $2; count++} END {print sum / count}' students.txt
echo -e "\nМаксимальная оценка:"
awk 'NR==1 {max = $2} $2 > max {max = $2} END {print max}' students.txt


