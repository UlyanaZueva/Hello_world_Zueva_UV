#!/bin/bash

if [ ! -f students.txt ]; then
    echo "Ошибка: файл students.txt не найден!"
    exit 1
fi

echo "Студенты с оценкой выше 80:"
awk '$2 > 80' students.txt

echo ""
echo "Студенты с оценкой ниже 70:"
awk '$2 < 70' students.txt

echo ""
echo "Первая строка файла:"
awk 'NR==1' students.txt

